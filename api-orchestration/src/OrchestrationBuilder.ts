import axios from 'axios';

type StepFunction = (request: any, context: any) => Promise<any>;
type TransformFunction = (input: any, context: any) => any;
type ConditionFunction = (response: any) => boolean;
type ErrorHandlerFunction = (error: any, context: any) => Promise<any>;

interface OrchestrationStep {
  name: string;
  execute: StepFunction;
  condition?: ConditionFunction;
  errorHandler?: ErrorHandlerFunction;
}

export class OrchestrationBuilder {
  private name: string;
  private steps: OrchestrationStep[] = [];
  private currentStep: Partial<OrchestrationStep> = {};
  private serviceRegistry: Record<string, string> = {
    // This would typically be loaded from configuration or service discovery
    'inventory-service': 'http://inventory-service-api:8080',
    'payment-service': 'http://payment-service-api:8080',
    'logistics-service': 'http://logistics-service-api:8080',
    'notification-service': 'http://notification-service-api:8080',
  };

  constructor(name: string) {
    this.name = name;
  }

  public step(name: string): OrchestrationBuilder {
    // Save previous step if exists
    if (this.currentStep.name) {
      this.steps.push(this.currentStep as OrchestrationStep);
    }
    
    this.currentStep = { name };
    return this;
  }

  public callService(serviceName: string, endpoint: string): OrchestrationBuilder {
    const serviceUrl = this.serviceRegistry[serviceName];
    
    if (!serviceUrl) {
      throw new Error(`Unknown service: ${serviceName}`);
    }
    
    this.currentStep.execute = async (request: any, context: any) => {
      const url = `${serviceUrl}${endpoint}`;
      const response = await axios.post(url, request);
      return response.data;
    };
    
    return this;
  }

  public withRequestTransform(transform: TransformFunction): OrchestrationBuilder {
    const originalExecute = this.currentStep.execute;
    
    if (!originalExecute) {
      throw new Error('No execute function defined for this step');
    }
    
    this.currentStep.execute = async (request: any, context: any) => {
      const transformedRequest = transform(request, context);
      return originalExecute(transformedRequest, context);
    };
    
    return this;
  }

  public withResponseTransform(transform: TransformFunction): OrchestrationBuilder {
    const originalExecute = this.currentStep.execute;
    
    if (!originalExecute) {
      throw new Error('No execute function defined for this step');
    }
    
    this.currentStep.execute = async (request: any, context: any) => {
      const response = await originalExecute(request, context);
      return transform(response, context);
    };
    
    return this;
  }

  public withResponseCondition(condition: ConditionFunction): OrchestrationBuilder {
    this.currentStep.condition = condition;
    return this;
  }

  public withErrorHandler(handler: ErrorHandlerFunction): OrchestrationBuilder {
    this.currentStep.errorHandler = handler;
    return this;
  }

  public build(): (request: any) => Promise<any> {
    // Add the last step
    if (this.currentStep.name) {
      this.steps.push(this.currentStep as OrchestrationStep);
    }
    
    return async (initialRequest: any) => {
      const context: Record<string, any> = {};
      let request = initialRequest;
      
      for (const step of this.steps) {
        try {
          console.log(`Executing step: ${step.name}`);
          
          // Execute step
          const response = await step.execute(request, context);
          
          // Store response in context using step name
          context[step.name] = response;
          
          // Check condition if exists
          if (step.condition && !step.condition(response)) {
            console.log(`Condition failed for step: ${step.name}`);
            throw new Error(`Condition failed for step: ${step.name}`);
          }
        } catch (error) {
          console.error(`Error in step ${step.name}:`, error);
          
          // Handle error if handler exists
          if (step.errorHandler) {
            await step.errorHandler(error, context);
          } else {
            throw error;
          }
        }
      }
      
      return { 
        success: true,
        result: context
      };
    };
  }
}
