const fs = require('fs');
const path = require('path');

// Function to process input data and generate UI components
function processInputData(data) {
  if (!data || typeof data !== 'object') {
    throw new Error('Invalid input data');
  }

  const componentHTML = `
    <div class="component">
      <h2>${data.title}</h2>
      <p>${data.description}</p>
    </div>
  `;

  return componentHTML;
}

// Function to handle UI generation requests
function generateUIBackend(inputFilePath, outputFilePath) {
  try {
    const inputData = JSON.parse(fs.readFileSync(inputFilePath, 'utf8'));
    const componentHTML = processInputData(inputData);

    const htmlContent = `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated UI</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
          }
          .container {
            text-align: center;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          }
        </style>
      </head>
      <body>
        <div class="container">
          ${componentHTML}
        </div>
      </body>
      </html>
    `;

    fs.writeFileSync(outputFilePath, htmlContent, 'utf8');
    console.log(`HTML page generated at: ${outputFilePath}`);
  } catch (error) {
    console.error('Error generating UI:', error.message);
  }
}

// Example usage
const inputFilePath = path.join(__dirname, 'input-data.json');
const outputFilePath = path.join(__dirname, 'generated-ui-backend.html');
generateUIBackend(inputFilePath, outputFilePath);
