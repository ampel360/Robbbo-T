
# Document: AMPEL360 Hydraulic System Overview and Procedures

**DMC:** DMC-GAIAPULSE-AMPEL-0201-29-001-A-001-00_EN-US  
**File:** GPAM-AMPEL-0201-29-001-A.md

*Please follow every step in the procedure below to verify the reliability and proper operation of each module’s component in the hydraulic system.*

---

## 1. Hydraulic System Components

### 1.1 Data and Specifications

- **Main Hydraulic Pump (AMPEL-HYD-PUMP-100):**  
  - **Description:** Provides high-pressure fluid to the flight control and actuation systems.  
  - **Operational Pressure:** 3000 PSI  
  - **Flow Rate:** 10 GPM  

- **System Control Unit (AMPEL-HSCU-200):**  
  - **Description:** Controls and monitors hydraulic system operations.  
  - **Verification:** Must be tested and monitored following protocol 19-201.

- **Additional Components:**  
  - **Reservoir (AMPEL-HYD-RES-100):** Supports system flow by supplying fluid.  
  - **Accumulator (AMPEL-ACC-100):** Provides backup pressure to maintain system integrity.

### 1.2 System Overview Diagram

```mermaid
graph TB
    %% Overview Block
    subgraph Overview
        A[AMPEL360 Hydraulic System Overview]:::central
    end

    %% Main Components
    subgraph MainComponents
        direction LR
        Pump[Main Hydraulic Pump\nAMPEL-HYD-PUMP-100]:::component
        Reservoir[Reservoir\nAMPEL-HYD-RES-100]:::component
        Accumulator[Accumulator\nAMPEL-ACC-100]:::component
        HSCU[System Control Unit\nAMPEL-HSCU-200]:::component
    end

    %% Monitoring Elements
    subgraph Monitoring
        direction TB
        M1[Pressure Sensors\n2900-3100 PSI]:::component
        M2[Temperature Sensors\n-40°C to +120°C]:::component
        M3[Fluid Level Sensors\nMIN/MAX]:::component
        M4[Filter Status\nΔP Indicators]:::component
    end

    %% Connections
    A --> HSCU
    HSCU -- "Command Signals" --> FlightControls[Flight Controls\nPrimary/Secondary]:::subsystem
    HSCU -- "Command Signals" --> LandingGear[Landing Gear\nExtension/Retraction]:::subsystem
    HSCU -- "Command Signals" --> BrakeSystem[Brake System\nNormal/Emergency]:::subsystem
    HSCU -- "Command Signals" --> NoseWheel[Nose Wheel Steering]:::subsystem

    HSCU -.-> M1 & M2 & M3 & M4
    Pump -- "Pressure Line\n(3000 PSI)" --> FlightControls & LandingGear & BrakeSystem & NoseWheel
    Reservoir -- "Supply" --> Pump
    Accumulator -- "Backup" --> FlightControls & LandingGear & BrakeSystem & NoseWheel

    %% Tooltip definitions for cross-references
    classDef control fill:#f9f,stroke:#333,stroke-width:2px;
    classDef pumpRef fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef reservoirRef fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef accumulatorRef fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef sensor fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef temperature fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef level fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef filter fill:#e0f7fa,stroke:#333,stroke-width:1px;

    %% Apply tooltips
    class HSCU control;
    class Pump pumpRef;
    class Reservoir reservoirRef;
    class Accumulator accumulatorRef;
    class M1 sensor;
    class M2 temperature;
    class M3 level;
    class M4 filter;

    %% Styling
    classDef central fill:#f9f,stroke:#333,stroke-width:2px;
    classDef component fill:#e0f7fa,stroke:#333,stroke-width:1px;
    classDef subsystem fill:#dfd,stroke:#333,stroke-width:2px;

```

---

### 1.3 Pre-Test Checklist

- [ ] **Aircraft Secured:** Ensure the aircraft is powered down and secured.
- [ ] **System Depressurized:** Verify the hydraulic system is fully depressurized.
- [ ] **Access Panels:** Remove all necessary access panels (Ref: AMM 52-20).
- [ ] **Equipment Check:** Confirm hydraulic pressure gauge (0–5000 PSI, ±1% accuracy) is calibrated.
- [ ] **Visual Inspection:** Check for cracks, dents, or loose fittings. *(Refer to CMM-AMPEL-HYD-PUMP-100, Section 3.2)*
- [ ] **Record Findings:** Document any deviations from standard specifications.

---

## 2. Test Protocols (HYD-100 Series)

### 2.1 Testing Steps

1. **Pressure Verification:**  
   - Use the hydraulic test stand to validate that the pump outputs between 2900–3100 PSI.  
   - **Reference:** [CMM-AMPEL-HYD-PUMP-100, Section 4.1](#cross-reference-to-CMM-AMPEL-HYD-PUMP-100).  
   - *Note:* Document any discrepancies.

2. **Functional Checks:**  
   - Verify actuator movement and control responses as per protocol.  
   - Record the test data for further analysis.

3. **Action on Failure:**  
   - If any test fails, initiate corrective procedures (e.g., replace faulty actuators).  
   - Log the corrective action for sign-off.

### 2.2 Documentation and Sign-off

- **Maintenance Log:** Record test results and any maintenance actions performed.
- **Approval:** Ensure a supervisor reviews and signs off on completed tests before reactivating the system.

---

## 3. System Procedures & Documentation

### 3.1 GPAM Hydraulic System Information

- **Function:**  
  - This document provides step-by-step tasks for inspections, leak checks, and component verification.  
  - **Reference:** GPAM-AMPEL-0201-28-001-A: Hydraulic System Leak Check and Component Inspection (ATA 29, S1000D Format).

### 3.2 Next Steps

- **Corrective Actions:**  
  - If discrepancies are found, follow the outlined repair procedures (e.g., replace components or seals).
- **Documentation:**  
  - Log all test data and corrective actions.  
  - Update the system maintenance records accordingly.

---

## 4. Structured Test Data (Example)

### YAML Example

```yaml
components:
  - name: "Main Hydraulic Pump"
    partNumber: "AMPEL-HYD-PUMP-100"
    description: "Provides high-pressure fluid to the hydraulic system."
    criticality: "High"
    maintenanceInterval: "1000 FH"
    test_procedure:
      - "Connect to test stand"
      - "Verify pressure output (2900-3100 PSI)"
      - "Record test data"
```

### TOML Example

```toml
title = "AMPEL360 Hydraulic System"
version = "1.0"

[overview]
short = "High-level overview"
long = "A detailed guide for test procedures and maintenance for the hydraulic system."

[components.pump]
name = "Main Hydraulic Pump"
part_number = "AMPEL-HYD-PUMP-100"
description = "Provides high-pressure fluid to the flight control and actuation systems."
maintenance_interval = "1000 FH"
test_procedure = ["Connect to test stand", "Verify pressure output (2900-3100 PSI)", "Record test data"]

[[checklist]]
test = "Verify power on"
result = "Power stable"

[[checklist]]
test = "Check for leaks"
result = "No leaks"
```

---

## 5. Detailed Task Cards for Common Procedures

### TC-HYD-003: Hydraulic Filter Replacement

**Applicability:** All configurations  
**Interval:** 1000 FH or 12 months  
**Skill Level:** Level 2

#### Prerequisites
- [ ] Aircraft powered down
- [ ] System depressurized
- [ ] Access panels removed (Ref: AMM 52-10)
- [ ] Maintenance stands positioned

#### Required Tools

| Tool           | Part Number   | Calibration Required |
|----------------|---------------|----------------------|
| Filter Wrench  | TOOL-HYD-101  | No                   |
| Torque Wrench  | TOOL-TQ-250   | Yes                  |
| O-ring Pick    | TOOL-ORG-001  | No                   |

#### Required Parts

| Description      | Part Number   | Quantity |
|------------------|---------------|----------|
| Filter Element   | FILT-HYD-100  | 1        |
| O-ring Set       | SEAL-HYD-100  | 1        |
| Lockwire         | LOCK-SS-032   | As required |

#### Safety Precautions
1. **WARNING:** Residual pressure may exist.
2. **CAUTION:** Maintain cleanliness to prevent contamination.
3. **NOTE:** Document filter condition.

#### Procedure Steps
1. **Preparation**
   - [ ] Verify system pressure is zero.
   - [ ] Place drain container.
   - [ ] Clean area around filter.
2. **Removal**
   - [ ] Remove safety wire.
   - [ ] Loosen filter bowl (using TOOL-HYD-101).
   - [ ] Collect fluid in container.
   - [ ] Remove filter element.
3. **Inspection**
   - [ ] Check bowl condition.
   - [ ] Inspect mounting threads.
   - [ ] Check bypass indicator.
   - [ ] Document filter condition.
4. **Installation**
   - [ ] Install new O-rings.
   - [ ] Lubricate O-rings.
   - [ ] Insert new filter element.
   - [ ] Torque bowl (25 ±2 ft-lbs).
   - [ ] Install safety wire per specification.

#### Acceptance Test
1. **System Preparation**
   - [ ] Close drain valves.
   - [ ] Connect hydraulic cart.
   - [ ] Fill system as required.
2. **Pressure Test**
   - [ ] Apply system pressure.
   - [ ] Check for leaks.
   - [ ] Verify bypass indicator.

#### Documentation
- [ ] Record part numbers.
- [ ] Log filter condition.
- [ ] Update maintenance records.

---

### TC-HYD-004: Hydraulic Accumulator Service

**Applicability:** All configurations  
**Interval:** 500 FH or 6 months  
**Skill Level:** Level 2

#### Required Tools

| Tool             | Part Number   | Calibration Required |
|------------------|---------------|----------------------|
| Nitrogen Cart    | TOOL-N2-100   | Yes                  |
| Pressure Gauge   | TOOL-PG-500   | Yes                  |
| Charging Adapter | TOOL-ACC-101  | No                   |

#### Safety Precautions
1. **WARNING:** High-pressure nitrogen.
2. **CAUTION:** Use only dry nitrogen.
3. **NOTE:** Record pre-charge pressure.

#### Procedure Steps
1. **System Depressurization**
   - [ ] Release hydraulic pressure.
   - [ ] Verify zero system pressure.
   - [ ] Isolate accumulator.
2. **Pre-charge Check**
   - [ ] Connect pressure gauge.
   - [ ] Record pressure: _____ PSI.
   - [ ] Compare to specifications.
3. **Nitrogen Charging**
   - [ ] Connect nitrogen cart.
   - [ ] Set regulator (600 ±10 PSI).
   - [ ] Charge accumulator.
   - [ ] Allow temperature stabilization.
   - [ ] Verify final pressure.

#### Acceptance Criteria

| Parameter   | Specification | Measured |
|-------------|---------------|----------|
| Pre-charge  | 600 ±10 PSI   | _______  |
| Temperature | 15-35°C       | _______  |
| Leak Rate   | 0 PSI/24hr    | _______  |

---

### TC-HYD-005: Return Line Pressure Check

**Applicability:** All configurations  
**Interval:** 300 FH  
**Skill Level:** Level 2

#### Required Equipment

| Equipment         | Part Number    | Calibration Due |
|-------------------|----------------|-----------------|
| Pressure Gauge    | TEST-HYD-002   | (Specify)       |
| Test Adapter      | TEST-HYD-003   | N/A             |
| Temperature Probe | TEST-TEMP-001  | (Specify)       |

#### Test Conditions

- **Fluid Temperature:** 40°C ±5°C  
- **System Pressure:** 3000 PSI  
- **Engine Speed:** Ground Idle

#### Procedure Steps
1. **Setup**
   - [ ] Install test equipment.
   - [ ] Warm up system.
   - [ ] Verify test conditions.
2. **Measurements**
   - [ ] Record static pressure.
   - [ ] Record dynamic pressure.
   - [ ] Monitor temperature.

#### Acceptance Criteria

| Parameter         | Limit         | Measured |
|-------------------|---------------|----------|
| Static Pressure   | <100 PSI      | _______  |
| Dynamic Pressure  | <150 PSI      | _______  |
| Temperature Rise  | <25°C         | _______  |

---

## 6. Configuration Management Templates

### 6.1 Configuration Status Record

#### Basic Information

| Field         | Value        |
|---------------|--------------|
| Aircraft S/N  | __________   |
| Config Code   | __________   |
| Last Update   | __________   |

#### Installed Components

| Component    | Part Number  | Serial Number  | Time Since New |
|--------------|--------------|----------------|----------------|
| Main Pump    | __________   | __________     | __________     |
| Aux Pump     | __________   | __________     | __________     |
| Actuator 1   | __________   | __________     | __________     |
| Actuator 2   | __________   | __________     | __________     |

#### Modification Status

| Mod Number | Description    | Compliance Date | Due Date   |
|------------|----------------|-----------------|------------|
| MOD-001    | __________     | __________      | __________ |
| MOD-002    | __________     | __________      | __________ |

---

### 6.2 Configuration Change Record

#### Change Details

| Field               | Value        |
|---------------------|--------------|
| Change Number       | __________   |
| Type                | [Major/Minor/Critical] |
| Implementation Date | __________   |

#### Affected Documentation

- [ ] AMM Chapter: __________
- [ ] IPC Section: __________
- [ ] CMM Reference: __________
- [ ] Task Cards: __________

#### Parts Affected

| Old P/N   | New P/N   | Quantity | Location   |
|-----------|-----------|----------|------------|
| ________  | ________  | _______  | ________   |
| ________  | ________  | _______  | ________   |

---

## 7. Actions & Recommendations

- **Tooltips & Cross-References:**  
  - Validate that tooltips display correctly in your Markdown renderer.  
  - Ensure each tooltip contains actionable information for quick reference.

- **Integration with S1000D:**  
  - Use the structured data (YAML/TOML) to automate or generate checklists and test reports.  
  - Link the diagrams directly to the S1000D documentation sections for seamless navigation.

- **Next Steps:**  
  - **Test Tables & Data:** Finalize structured test data to cover all modules.  
  - **Actionable Workflow:** Decide whether to further refine one component (e.g., pump) or integrate all components into one unified workflow.  
  - **Feedback Loop:** Ensure maintenance personnel test the document in their environment and provide feedback for future iterations.

---

## Final Thoughts

This document provides a comprehensive, actionable workflow for the AMPEL360 Hydraulic System. It integrates detailed system overviews, pre-test checklists, test protocols, structured test data, and component-specific task cards—all formatted in Markdown for ease of use and integration into an S1000D-compliant framework.

Would you like to proceed with further refinements on any specific section, or is this iteration ready for implementation?

---

*End of Document*
```

---

This Markdown document is now fully formatted and ready to be used as a centralized maintenance manual for the hydraulic system. Let me know if you need any further adjustments or additional details!
