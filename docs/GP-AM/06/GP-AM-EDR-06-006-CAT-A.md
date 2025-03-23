# GP-AM-EDR-06-006-CAT-A: Measurement Point Definitions Table

**Document ID:** GP-AM-EDR-06-006-CAT-A  
**Revision:** A  
**Status:** Released  
**Date:** 2025-02-20  

## 1. Introduction

### 1.1 Purpose and Scope

This Measurement Point Definitions Table establishes the comprehensive catalog of all measurement points, reference locations, and dimensional verification positions for the AMPEL360XWLRGA aircraft. It provides the authoritative reference for all measurement activities throughout the aircraft's lifecycle, from design and manufacturing to maintenance and repair operations. This document serves as the primary reference for identifying, locating, and verifying critical measurement points required for dimensional control, assembly verification, and operational maintenance.

The scope encompasses:
- Primary reference measurement points
- Secondary reference measurement points
- Critical interface measurement points
- Assembly verification measurement points
- System alignment measurement points
- Novel technology measurement points
- Maintenance reference measurement points
- Operational verification measurement points

### 1.2 Document Structure

This document is organized as follows:
- Section 1: Introduction and document overview
- Section 2: Measurement Point Identification System
- Section 3: Primary Reference Measurement Points
- Section 4: Secondary Reference Measurement Points
- Section 5: Critical Interface Measurement Points
- Section 6: Assembly Verification Measurement Points
- Section 7: System Alignment Measurement Points
- Section 8: Novel Technology Measurement Points
- Section 9: Maintenance Reference Measurement Points
- Section 10: Operational Verification Measurement Points

### 1.3 Applicable Documents

The following documents form an integral part of this measurement point definitions table:

- GP-AM-AMPEL-0100-00-001-A: Aircraft General – System Description (ATA 00)
- GP-AM-EDR-00-001-SDD-A: Overall Aircraft System Description Document
- GP-AM-EDR-06-001-CAL-A: Dimensional Data Report
- GP-AM-EDR-06-002-PROC-A: Calibration & Measurement Procedures Document
- GP-AM-EDR-06-003-CAL-A: Structural Integration Analysis Report
- GP-AM-EDR-06-004-DD-A: Internal Compartment Layout Document
- GP-AM-EDR-06-005-CAL-A: Detailed Dimensions and Volume Calculation Report
- GP-AM-DRW-06-007-DWG-A: Cross-Reference Diagram for Measurement Points
- GP-AM-AMPEL-0201-06-002-A: Compartment Layout and Dimensions (ATA 06)
- GP-AM-AMPEL-0201-06-003-A: AMPEL360XWLRGA Measurement Point Definitions (ATA 06)

### 1.4 Terminology and Abbreviations

| Abbreviation | Definition |
|--------------|------------|
| BL | Buttock Line |
| CG | Center of Gravity |
| FS | Fuselage Station |
| IML | Inner Mold Line |
| MP | Measurement Point |
| OML | Outer Mold Line |
| PMP | Primary Measurement Point |
| QPS | Quantum Propulsion System |
| SMP | Secondary Measurement Point |
| WL | Water Line |
| XRS | External Reference System |

## 2. Measurement Point Identification System

### 2.1 Measurement Point Classification

The AMPEL360XWLRGA aircraft measurement points are classified according to the following hierarchy:

1. **Primary Reference Measurement Points (PMP)**:
   - Fundamental reference points that establish the aircraft coordinate system
   - Used for major assembly alignment and integration
   - Highest precision and stability requirements
   - Permanent features on the aircraft structure

2. **Secondary Reference Measurement Points (SMP)**:
   - Derived from primary reference points
   - Used for component alignment and positioning
   - High precision requirements
   - Permanent features on major structural components

3. **Critical Interface Measurement Points (CMP)**:
   - Located at critical structural interfaces
   - Used for verifying proper interface alignment and fit
   - High precision requirements
   - Located at major structural joints and connections

4. **Assembly Verification Measurement Points (AMP)**:
   - Used during assembly to verify proper component positioning
   - Medium to high precision requirements
   - May be temporary or permanent features

5. **System Alignment Measurement Points (SMP)**:
   - Used for aligning and positioning aircraft systems
   - Medium precision requirements
   - Located on system components and mounting structures

6. **Novel Technology Measurement Points (NMP)**:
   - Specialized points for quantum propulsion, hydrogen, and energy systems
   - High precision requirements
   - Located on novel technology components and interfaces

7. **Maintenance Reference Measurement Points (MMP)**:
   - Used during maintenance and repair operations
   - Medium precision requirements
   - Accessible in service configuration

8. **Operational Verification Measurement Points (OMP)**:
   - Used during operational checks and inspections
   - Lower precision requirements
   - Easily accessible in service configuration

### 2.2 Measurement Point Identification Code

Each measurement point is assigned a unique identification code using the following format:

**[Type]-[Zone]-[Sequence]-[Side]**

Where:
- **Type**: Two-letter code indicating the measurement point classification (PMP, SMP, CMP, AMP, SMP, NMP, MMP, OMP)
- **Zone**: Three-digit code indicating the aircraft zone location (per zoning system in GP-AM-EDR-06-004-DD-A)
- **Sequence**: Three-digit sequential number within the zone
- **Side**: Single letter indicating side (L = Left, R = Right, C = Center)

Example: PMP-100-001-C represents the first Primary Measurement Point in Zone 100, located at the center.

### 2.3 Measurement Point Documentation

Each measurement point is documented with the following information:

1. **Identification Code**: Unique identifier as described above
2. **Description**: Brief description of the measurement point
3. **Location**: Precise coordinates (FS, BL, WL) in the aircraft coordinate system
4. **Physical Feature**: Description of the physical feature (hole, target, tooling ball, etc.)
5. **Access**: Information on how to access the measurement point
6. **Precision Requirement**: Required measurement precision
7. **Reference Documents**: Cross-reference to detailed drawings or specifications
8. **Usage**: Primary applications of the measurement point
9. **Notes**: Additional information or special considerations

### 2.4 Measurement Point Marking

Physical marking of measurement points on the aircraft follows these conventions:

1. **Primary Reference Points**: Permanently marked with engraved identification and precision tooling ball receptacles
2. **Secondary Reference Points**: Permanently marked with engraved identification and precision bushings
3. **Critical Interface Points**: Permanently marked with engraved identification
4. **Assembly Verification Points**: Marked with removable targets or semi-permanent markings
5. **System Alignment Points**: Marked according to system requirements
6. **Novel Technology Points**: Specially marked according to technology requirements
7. **Maintenance Reference Points**: Clearly marked for maintenance access
8. **Operational Verification Points**: Marked for operational visibility

## 3. Primary Reference Measurement Points

### 3.1 Fuselage Primary Reference Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| PMP-100-001-C | Nose Reference Point | FS 0.00, BL 0.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Aircraft coordinate system origin reference |
| PMP-100-002-C | Forward Pressure Bulkhead Center | FS 100.00, BL 0.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Forward structure reference |
| PMP-200-001-C | Wing Front Spar Intersection | FS 600.00, BL 0.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing-to-fuselage reference |
| PMP-200-002-C | Wing Rear Spar Intersection | FS 800.00, BL 0.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing-to-fuselage reference |
| PMP-300-001-C | Aft Pressure Bulkhead Center | FS 1700.00, BL 0.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Aft structure reference |
| PMP-300-002-C | Vertical Stabilizer Attachment | FS 1500.00, BL 0.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Empennage reference |
| PMP-300-003-C | Horizontal Stabilizer Attachment | FS 1550.00, BL 0.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Empennage reference |
| PMP-400-001-C | Main Landing Gear Trunnion Center | FS 900.00, BL 0.00, WL 50.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Landing gear reference |
| PMP-400-002-C | Nose Landing Gear Trunnion Center | FS 150.00, BL 0.00, WL 50.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Landing gear reference |
| PMP-800-001-C | Quantum Propulsion System Center | FS 1250.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Propulsion system reference |

### 3.2 Wing Primary Reference Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| PMP-600-001-L | Left Wing Root Front Spar | FS 600.00, BL -150.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-001-R | Right Wing Root Front Spar | FS 600.00, BL 150.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-002-L | Left Wing Root Rear Spar | FS 800.00, BL -150.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-002-R | Right Wing Root Rear Spar | FS 800.00, BL 150.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-003-L | Left Wing Tip Front Spar | FS 810.00, BL -750.00, WL 187.50 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-003-R | Right Wing Tip Front Spar | FS 810.00, BL 750.00, WL 187.50 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-004-L | Left Wing Tip Rear Spar | FS 910.00, BL -750.00, WL 187.50 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |
| PMP-600-004-R | Right Wing Tip Rear Spar | FS 910.00, BL 750.00, WL 187.50 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Wing alignment reference |

### 3.3 Empennage Primary Reference Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| PMP-700-001-L | Left Horizontal Stabilizer Root Front Spar | FS 1550.00, BL -50.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Horizontal stabilizer reference |
| PMP-700-001-R | Right Horizontal Stabilizer Root Front Spar | FS 1550.00, BL 50.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Horizontal stabilizer reference |
| PMP-700-002-L | Left Horizontal Stabilizer Root Rear Spar | FS 1650.00, BL -50.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Horizontal stabilizer reference |
| PMP-700-002-R | Right Horizontal Stabilizer Root Rear Spar | FS 1650.00, BL 50.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Horizontal stabilizer reference |
| PMP-700-003-L | Left Horizontal Stabilizer Tip Front Spar | FS 1610.00, BL -300.00, WL 339.50 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Horizontal stabilizer reference |
| PMP-700-003-R | Right Horizontal Stabilizer Tip Front Spar | FS 1610.00, BL 300.00, WL 339.50 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Horizontal stabilizer reference |
| PMP-700-004-C | Vertical Stabilizer Root Front Spar | FS 1500.00, BL 0.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Vertical stabilizer reference |
| PMP-700-005-C | Vertical Stabilizer Root Rear Spar | FS 1600.00, BL 0.00, WL 325.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Vertical stabilizer reference |
| PMP-700-006-C | Vertical Stabilizer Tip Front Spar | FS 1680.00, BL 0.00, WL 625.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Vertical stabilizer reference |
| PMP-700-007-C | Vertical Stabilizer Tip Rear Spar | FS 1800.00, BL 0.00, WL 625.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Vertical stabilizer reference |

## 4. Secondary Reference Measurement Points

### 4.1 Fuselage Secondary Reference Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| SMP-100-001-C | Forward Cabin Floor Reference | FS 300.00, BL 0.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Cabin interior reference |
| SMP-100-002-L | Forward Left Door Frame Reference | FS 350.00, BL -120.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation reference |
| SMP-100-002-R | Forward Right Door Frame Reference | FS 350.00, BL 120.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation reference |
| SMP-200-001-C | Mid Cabin Floor Reference | FS 800.00, BL 0.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Cabin interior reference |
| SMP-200-002-L | Left Emergency Exit Frame Reference | FS 800.00, BL -120.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Emergency exit reference |
| SMP-200-002-R | Right Emergency Exit Frame Reference | FS 800.00, BL 120.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Emergency exit reference |
| SMP-300-001-C | Aft Cabin Floor Reference | FS 1300.00, BL 0.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Cabin interior reference |
| SMP-300-002-L | Aft Left Door Frame Reference | FS 1350.00, BL -120.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation reference |
| SMP-300-002-R | Aft Right Door Frame Reference | FS 1350.00, BL 120.00, WL 125.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation reference |
| SMP-400-001-L | Forward Cargo Door Frame Reference | FS 400.00, BL -120.00, WL 50.00 | Bushing | ±0.010 in (±0.254 mm) | Cargo door reference |
| SMP-400-002-L | Aft Cargo Door Frame Reference | FS 1100.00, BL -120.00, WL 50.00 | Bushing | ±0.010 in (±0.254 mm) | Cargo door reference |

### 4.2 Wing Secondary Reference Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| SMP-600-001-L | Left Wing Mid Span Front Spar | FS 705.00, BL -450.00, WL 156.25 | Bushing | ±0.010 in (±0.254 mm) | Wing assembly reference |
| SMP-600-001-R | Right Wing Mid Span Front Spar | FS 705.00, BL 450.00, WL 156.25 | Bushing | ±0.010 in (±0.254 mm) | Wing assembly reference |
| SMP-600-002-L | Left Wing Mid Span Rear Spar | FS 855.00, BL -450.00, WL 156.25 | Bushing | ±0.010 in (±0.254 mm) | Wing assembly reference |
| SMP-600-002-R | Right Wing Mid Span Rear Spar | FS 855.00, BL 450.00, WL 156.25 | Bushing | ±0.010 in (±0.254 mm) | Wing assembly reference |
| SMP-600-003-L | Left Aileron Hinge Line Reference | FS 877.50, BL -660.00, WL 177.50 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |
| SMP-600-003-R | Right Aileron Hinge Line Reference | FS 877.50, BL 660.00, WL 177.50 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |
| SMP-600-004-L | Left Flap Hinge Line Reference | FS 855.00, BL -300.00, WL 140.00 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |
| SMP-600-004-R | Right Flap Hinge Line Reference | FS 855.00, BL 300.00, WL 140.00 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |

### 4.3 Empennage Secondary Reference Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| SMP-700-001-L | Left Elevator Hinge Line Reference | FS 1650.00, BL -175.00, WL 325.00 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |
| SMP-700-001-R | Right Elevator Hinge Line Reference | FS 1650.00, BL 175.00, WL 325.00 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |
| SMP-700-002-C | Rudder Hinge Line Reference | FS 1600.00, BL 0.00, WL 475.00 | Bushing | ±0.010 in (±0.254 mm) | Control surface reference |
| SMP-700-003-L | Left Horizontal Stabilizer Mid Span | FS 1580.00, BL -175.00, WL 332.25 | Bushing | ±0.010 in (±0.254 mm) | Horizontal stabilizer reference |
| SMP-700-003-R | Right Horizontal Stabilizer Mid Span | FS 1580.00, BL 175.00, WL 332.25 | Bushing | ±0.010 in (±0.254 mm) | Horizontal stabilizer reference |
| SMP-700-004-C | Vertical Stabilizer Mid Height | FS 1550.00, BL 0.00, WL 475.00 | Bushing | ±0.010 in (±0.254 mm) | Vertical stabilizer reference |

## 5. Critical Interface Measurement Points

### 5.1 Wing-to-Fuselage Interface Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| CMP-200-001-L | Left Front Spar Lower Attachment | FS 600.00, BL -150.00, WL 100.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-001-R | Right Front Spar Lower Attachment | FS 600.00, BL 150.00, WL 100.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-002-L | Left Front Spar Upper Attachment | FS 600.00, BL -150.00, WL 150.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-002-R | Right Front Spar Upper Attachment | FS 600.00, BL 150.00, WL 150.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-003-L | Left Rear Spar Lower Attachment | FS 800.00, BL -150.00, WL 100.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-003-R | Right Rear Spar Lower Attachment | FS 800.00, BL 150.00, WL 100.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-004-L | Left Rear Spar Upper Attachment | FS 800.00, BL -150.00, WL 150.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-004-R | Right Rear Spar Upper Attachment | FS 800.00, BL 150.00, WL 150.00 | Bushing | ±0.005 in (±0.127 mm) | Wing attachment verification |
| CMP-200-005-L | Left Wing Upper Skin Splice | FS 700.00, BL -150.00, WL 175.00 | Bushing | ±0.010 in (±0.254 mm) | Wing skin splice verification |
| CMP-200-005-R | Right Wing Upper Skin Splice | FS 700.00, BL 150.00, WL 175.00 | Bushing | ±0.010 in (±0.254 mm) | Wing skin splice verification |
| CMP-200-006-L | Left Wing Lower Skin Splice | FS 700.00, BL -150.00, WL 75.00 | Bushing | ±0.010 in (±0.254 mm) | Wing skin splice verification |
| CMP-200-006-R | Right Wing Lower Skin Splice | FS 700.00, BL 150.00, WL 75.00 | Bushing | ±0.010 in (±0.254 mm) | Wing skin splice verification |

### 5.2 Empennage-to-Fuselage Interface Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| CMP-300-001-C | Vertical Stabilizer Front Spar Lower Attachment | FS 1500.00, BL 0.00, WL 325.00 | Bushing | ±0.005 in (±0.127 mm) | Vertical stabilizer attachment verification |
| CMP-300-002-C | Vertical Stabilizer Rear Spar Lower Attachment | FS 1600.00, BL 0.00, WL 325.00 | Bushing | ±0.005 in (±0.127 mm) | Vertical stabilizer attachment verification |
| CMP-300-003-L | Left Horizontal Stabilizer Front Spar Attachment | FS 1550.00, BL -50.00, WL 325.00 | Bushing | ±0.005 in (±0.127 mm) | Horizontal stabilizer attachment verification |
| CMP-300-003-R | Right Horizontal Stabilizer Front Spar Attachment | FS 1550.00, BL 50.00, WL 325.00 | Bushing | ±0.005 in (±0.127 mm) | Horizontal stabilizer attachment verification |
| CMP-300-004-L | Left Horizontal Stabilizer Rear Spar Attachment | FS 1650.00, BL -50.00, WL 325.00 | Bushing | ±0.005 in (±0.127 mm) | Horizontal stabilizer attachment verification |
| CMP-300-004-R | Right Horizontal Stabilizer Rear Spar Attachment | FS 1650.00, BL 50.00, WL 325.00 | Bushing | ±0.005 in (±0.127 mm) | Horizontal stabilizer attachment verification |
| CMP-300-005-C | Vertical Stabilizer Skin Splice | FS 1550.00, BL 0.00, WL 375.00 | Bushing | ±0.010 in (±0.254 mm) | Vertical stabilizer skin splice verification |
| CMP-300-006-L | Left Horizontal Stabilizer Skin Splice | FS 1600.00, BL -50.00, WL 325.00 | Bushing | ±0.010 in (±0.254 mm) | Horizontal stabilizer skin splice verification |
| CMP-300-006-R | Right Horizontal Stabilizer Skin Splice | FS 1600.00, BL 50.00, WL 325.00 | Bushing | ±0.010 in (±0.254 mm) | Horizontal stabilizer skin splice verification |

### 5.3 Landing Gear-to-Structure Interface Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| CMP-400-001-C | Nose Gear Trunnion Left Attachment | FS 150.00, BL -10.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Nose gear attachment verification |
| CMP-400-002-C | Nose Gear Trunnion Right Attachment | FS 150.00, BL 10.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Nose gear attachment verification |
| CMP-400-003-C | Nose Gear Drag Strut Attachment | FS 175.00, BL 0.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Nose gear attachment verification |
| CMP-400-004-L | Left Main Gear Trunnion Forward Attachment | FS 900.00, BL -180.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Main gear attachment verification |
| CMP-400-004-R | Right Main Gear Trunnion Forward Attachment | FS 900.00, BL 180.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Main gear attachment verification |
| CMP-400-005-L | Left Main Gear Trunnion Aft Attachment | FS 900.00, BL -170.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Main gear attachment verification |
| CMP-400-005-R | Right Main Gear Trunnion Aft Attachment | FS 900.00, BL 170.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Main gear attachment verification |
| CMP-400-006-L | Left Main Gear Drag Strut Attachment | FS 925.00, BL -180.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Main gear attachment verification |
| CMP-400-006-R | Right Main Gear Drag Strut Attachment | FS 925.00, BL 180.00, WL 50.00 | Bushing | ±0.005 in (±0.127 mm) | Main gear attachment verification |

### 5.4 Door and Window Interface Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| CMP-100-001-L | Forward Left Door Upper Hinge | FS 350.00, BL -120.00, WL 155.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-100-001-R | Forward Right Door Upper Hinge | FS 350.00, BL 120.00, WL 155.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-100-002-L | Forward Left Door Lower Hinge | FS 350.00, BL -120.00, WL 95.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-100-002-R | Forward Right Door Lower Hinge | FS 350.00, BL 120.00, WL 95.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-300-001-L | Aft Left Door Upper Hinge | FS 1350.00, BL -120.00, WL 155.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-300-001-R | Aft Right Door Upper Hinge | FS 1350.00, BL 120.00, WL 155.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-300-002-L | Aft Left Door Lower Hinge | FS 1350.00, BL -120.00, WL 95.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-300-002-R | Aft Right Door Lower Hinge | FS 1350.00, BL 120.00, WL 95.00 | Bushing | ±0.010 in (±0.254 mm) | Door installation verification |
| CMP-400-001-L | Forward Cargo Door Upper Hinge | FS 400.00, BL -120.00, WL 80.00 | Bushing | ±0.010 in (±0.254 mm) | Cargo door installation verification |
| CMP-400-002-L | Forward Cargo Door Lower Hinge | FS 400.00, BL -120.00, WL 20.00 | Bushing | ±0.010 in (±0.254 mm) | Cargo door installation verification |

## 6. Assembly Verification Measurement Points

### 6.1 Fuselage Assembly Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| AMP-100-001-C | Forward Fuselage Section Join Forward | FS 200.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-100-002-L | Forward Fuselage Section Join Left | FS 200.00, BL -120.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-100-002-R | Forward Fuselage Section Join Right | FS 200.00, BL 120.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-200-001-C | Mid Fuselage Section Join Forward | FS 500.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-200-002-L | Mid Fuselage Section Join Left | FS 500.00, BL -120.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-200-002-R | Mid Fuselage Section Join Right | FS 500.00, BL 120.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-300-001-C | Aft Fuselage Section Join Forward | FS 1200.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-300-002-L | Aft Fuselage Section Join Left | FS 1200.00, BL -120.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-300-002-R | Aft Fuselage Section Join Right | FS 1200.00, BL 120.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |
| AMP-300-003-C | Tail Cone Join | FS 1600.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Fuselage section join verification |

### 6.2 Wing Assembly Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| AMP-600-001-L | Left Wing Panel Join Outer | FS 705.00, BL -300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Wing panel join verification |
| AMP-600-001-R | Right Wing Panel Join Outer | FS 705.00, BL 300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Wing panel join verification |
| AMP-600-002-L | Left Wing Leading Edge Join | FS 652.50, BL -300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Wing leading edge verification |
| AMP-600-002-R | Right Wing Leading Edge Join | FS 652.50, BL 300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Wing leading edge verification |
| AMP-600-003-L | Left Wing Trailing Edge Join | FS 855.00, BL -300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Wing trailing edge verification |
| AMP-600-003-R | Right Wing Trailing Edge Join | FS 855.00, BL 300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Wing trailing edge verification |
| AMP-600-004-L | Left Aileron Installation | FS 877.50, BL -660.00, WL 177.50 | Target | ±0.020 in (±0.508 mm) | Aileron installation verification |
| AMP-600-004-R | Right Aileron Installation | FS 877.50, BL 660.00, WL 177.50 | Target | ±0.020 in (±0.508 mm) | Aileron installation verification |
| AMP-600-005-L | Left Flap Installation | FS 855.00, BL -300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Flap installation verification |
| AMP-600-005-R | Right Flap Installation | FS 855.00, BL 300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Flap installation verification |

### 6.3 Empennage Assembly Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| AMP-700-001-L | Left Horizontal Stabilizer Panel Join | FS 1580.00, BL -175.00, WL 325.00 | Target | ±0.020 in (±0.508 mm) | Horizontal stabilizer panel join verification |
| AMP-700-001-R | Right Horizontal Stabilizer Panel Join | FS 1580.00, BL 175.00, WL 325.00 | Target | ±0.020 in (±0.508 mm) | Horizontal stabilizer panel join verification |
| AMP-700-002-L | Left Elevator Installation | FS 1650.00, BL -175.00, WL 325.00 | Target | ±0.020 in (±0.508 mm) | Elevator installation verification |
| AMP-700-002-R | Right Elevator Installation | FS 1650.00, BL 175.00, WL 325.00 | Target | ±0.020 in (±0.508 mm) | Elevator installation verification |
| AMP-700-003-C | Vertical Stabilizer Panel Join | FS 1550.00, BL 0.00, WL 475.00 | Target | ±0.020 in (±0.508 mm) | Vertical stabilizer panel join verification |
| AMP-700-004-C | Rudder Installation | FS 1600.00, BL 0.00, WL 475.00 | Target | ±0.020 in (±0.508 mm) | Rudder installation verification |

## 7. System Alignment Measurement Points

### 7.1 Flight Control System Alignment Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| SMP-100-001-C | Cockpit Control Column Reference | FS 165.00, BL 0.00, WL 135.00 | Target | ±0.020 in (±0.508 mm) | Control column alignment verification |
| SMP-100-002-C | Rudder Pedal Reference | FS 140.00, BL 0.00, WL 110.00 | Target | ±0.020 in (±0.508 mm) | Rudder pedal alignment verification |
| SMP-200-001-L | Left Aileron Control Actuator | FS 855.00, BL -570.00, WL 156.25 | Target | ±0.020 in (±0.508 mm) | Aileron actuator alignment verification |
| SMP-200-001-R | Right Aileron Control Actuator | FS 855.00, BL 570.00, WL 156.25 | Target | ±0.020 in (±0.508 mm) | Aileron actuator alignment verification |
| SMP-200-002-L | Left Flap Control Actuator | FS 855.00, BL -300.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Flap actuator alignment verification |
| SMP-200-002-R | Right Flap Control Actuator | FS 855.00, BL 300.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Flap actuator alignment verification |
| SMP-300-001-L | Left Elevator Control Actuator | FS 1650.00, BL -100.00, WL 325.00 | Target | ±0.020 in (±0.508 mm) | Elevator actuator alignment verification |
| SMP-300-001-R | Right Elevator Control Actuator | FS 1650.00, BL 100.00, WL 325.00 | Target | ±0.020 in (±0.508 mm) | Elevator actuator alignment verification |
| SMP-300-002-C | Rudder Control Actuator | FS 1600.00, BL 0.00, WL 400.00 | Target | ±0.020 in (±0.508 mm) | Rudder actuator alignment verification |

### 7.2 Environmental Control System Alignment Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| SMP-200-003-C | Air Conditioning Pack | FS 700.00, BL 0.00, WL 50.00 | Target | ±0.050 in (±1.270 mm) | ECS pack alignment verification |
| SMP-200-004-L | Left Air Distribution Duct Reference | FS 700.00, BL -60.00, WL 175.00 | Target | ±0.050 in (±1.270 mm) | Air duct alignment verification |
| SMP-200-004-R | Right Air Distribution Duct Reference | FS 700.00, BL 60.00, WL 175.00 | Target | ±0.050 in (±1.270 mm) | Air duct alignment verification |
| SMP-200-005-C | Cabin Pressure Controller | FS 750.00, BL 0.00, WL 50.00 | Target | ±0.050 in (±1.270 mm) | Pressure controller alignment verification |
| SMP-200-006-C | Outflow Valve | FS 1500.00, BL 0.00, WL 125.00 | Target | ±0.050 in (±1.270 mm) | Outflow valve alignment verification |

### 7.3 Electrical System Alignment Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| SMP-300-003-C | Main Power Distribution Center | FS 1400.00, BL 0.00, WL 50.00 | Target | ±0.050 in (±1.270 mm) | Power distribution alignment verification |
| SMP-300-004-L | Left Battery Installation | FS 1450.00, BL -40.00, WL 50.00 | Target | ±0.050 in (±1.270 mm) | Battery installation verification |
| SMP-300-004-R | Right Battery Installation | FS 1450.00, BL 40.00, WL 50.00 | Target | ±0.050 in (±1.270 mm) | Battery installation verification |
| SMP-300-005-C | APU Generator | FS 1700.00, BL 0.00, WL 100.00 | Target | ±0.050 in (±1.270 mm) | APU generator alignment verification |
| SMP-300-006-C | Emergency Power System | FS 1450.00, BL -60.00, WL 50.00 | Target | ±0.050 in (±1.270 mm) | Emergency power system alignment verification |

## 8. Novel Technology Measurement Points

### 8.1 Quantum Propulsion System Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| NMP-800-001-C | Quantum Core Center | FS 1250.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Quantum core alignment verification |
| NMP-800-002-C | Quantum Field Generator | FS 1225.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Field generator alignment verification |
| NMP-800-003-C | Cryogenic Cooling System | FS 1275.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Cooling system alignment verification |
| NMP-800-004-C | Quantum Control Unit | FS 1200.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Control unit alignment verification |
| NMP-800-005-F | Forward Quantum Shielding Reference | FS 1200.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Shielding alignment verification |
| NMP-800-005-A | Aft Quantum Shielding Reference | FS 1300.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Shielding alignment verification |
| NMP-800-005-L | Left Quantum Shielding Reference | FS 1250.00, BL -60.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Shielding alignment verification |
| NMP-800-005-R | Right Quantum Shielding Reference | FS 1250.00, BL 60.00, WL 175.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Shielding alignment verification |
| NMP-800-005-T | Top Quantum Shielding Reference | FS 1250.00, BL 0.00, WL 235.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Shielding alignment verification |
| NMP-800-005-B | Bottom Quantum Shielding Reference | FS 1250.00, BL 0.00, WL 115.00 | Tooling Ball Receptacle | ±0.001 in (±0.025 mm) | Shielding alignment verification |

### 8.2 Hydrogen Fuel System Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| NMP-800-006-C | Hydrogen Storage Tank Center | FS 1350.00, BL 0.00, WL 100.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Hydrogen tank alignment verification |
| NMP-800-007-L | Left Fuel Cell Stack | FS 1300.00, BL -25.00, WL 100.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Fuel cell alignment verification |
| NMP-800-007-R | Right Fuel Cell Stack | FS 1300.00, BL 25.00, WL 100.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Fuel cell alignment verification |
| NMP-800-008-C | Hydrogen Distribution Manifold | FS 1275.00, BL 0.00, WL 100.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Distribution system alignment verification |
| NMP-800-009-L | Left Thermal Management System | FS 1325.00, BL -25.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Thermal system alignment verification |
| NMP-800-009-R | Right Thermal Management System | FS 1325.00, BL 25.00, WL 125.00 | Tooling Ball Receptacle | ±0.005 in (±0.127 mm) | Thermal system alignment verification |

### 8.3 Advanced Energy Harvesting System Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| NMP-800-010-C | Energy Conversion Module Center | FS 1500.00, BL 0.00, WL 225.00 | Tooling Ball Receptacle | ±0.010 in (±0.254 mm) | Energy conversion alignment verification |
| NMP-800-011-C | Energy Storage Unit Center | FS 1500.00, BL 0.00, WL 200.00 | Tooling Ball Receptacle | ±0.010 in (±0.254 mm) | Energy storage alignment verification |
| NMP-800-012-C | Energy Management Controller | FS 1500.00, BL 0.00, WL 175.00 | Tooling Ball Receptacle | ±0.010 in (±0.254 mm) | Controller alignment verification |
| NMP-800-013-L | Left Wing Collection Surface Reference | FS 700.00, BL -300.00, WL 156.25 | Tooling Ball Receptacle | ±0.010 in (±0.254 mm) | Collection surface alignment verification |
| NMP-800-013-R | Right Wing Collection Surface Reference | FS 700.00, BL 300.00, WL 156.25 | Tooling Ball Receptacle | ±0.010 in (±0.254 mm) | Collection surface alignment verification |
| NMP-800-013-T | Top Fuselage Collection Surface Reference | FS 900.00, BL 0.00, WL 240.00 | Tooling Ball Receptacle | ±0.010 in (±0.254 mm) | Collection surface alignment verification |

### 8.4 Self-Healing Structure Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| NMP-800-014-F | Forward Fuselage Self-Healing Reference | FS 300.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Self-healing system verification |
| NMP-800-014-M | Mid Fuselage Self-Healing Reference | FS 900.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Self-healing system verification |
| NMP-800-014-A | Aft Fuselage Self-Healing Reference | FS 1500.00, BL 0.00, WL 125.00 | Target | ±0.020 in (±0.508 mm) | Self-healing system verification |
| NMP-800-015-L | Left Wing Self-Healing Reference | FS 700.00, BL -300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Self-healing system verification |
| NMP-800-015-R | Right Wing Self-Healing Reference | FS 700.00, BL 300.00, WL 140.00 | Target | ±0.020 in (±0.508 mm) | Self-healing system verification |
| NMP-800-016-C | Vertical Stabilizer Self-Healing Reference | FS 1550.00, BL 0.00, WL 475.00 | Target | ±0.020 in (±0.508 mm) | Self-healing system verification |

## 9. Maintenance Reference Measurement Points

### 9.1 Engine Access Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| MMP-800-001-C | QPS Access Hatch Reference | FS 1250.00, BL 0.00, WL 240.00 | Target | ±0.050 in (±1.270 mm) | QPS maintenance access verification |
| MMP-800-002-L | Left QPS Component Access | FS 1250.00, BL -60.00, WL 175.00 | Target | ±0.050 in (±1.270 mm) | QPS maintenance access verification |
| MMP-800-002-R | Right QPS Component Access | FS 1250.00, BL 60.00, WL 175.00 | Target | ±0.050 in (±1.270 mm) | QPS maintenance access verification |
| MMP-800-003-C | Quantum Core Removal Path | FS 1250.00, BL 0.00, WL 300.00 | Target | ±0.050 in (±1.270 mm) | QPS component removal verification |
| MMP-800-004-C | Hydrogen System Access Hatch | FS 1350.00, BL 0.00, WL 150.00 | Target | ±0.050 in (±1.270 mm) | Hydrogen system maintenance access verification |

### 9.2 Landing Gear Maintenance Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| MMP-400-001-C | Nose Gear Bay Access | FS 150.00, BL 0.00, WL 100.00 | Target | ±0.050 in (±1.270 mm) | Nose gear maintenance access verification |
| MMP-400-002-L | Left Main Gear Bay Access | FS 900.00, BL -180.00, WL 100.00 | Target | ±0.050 in (±1.270 mm) | Main gear maintenance access verification |
| MMP-400-002-R | Right Main Gear Bay Access | FS 900.00, BL 180.00, WL 100.00 | Target | ±0.050 in (±1.270 mm) | Main gear maintenance access verification |
| MMP-400-003-C | Nose Gear Removal Path | FS 150.00, BL 0.00, WL 0.00 | Target | ±0.050 in (±1.270 mm) | Nose gear removal verification |
| MMP-400-004-L | Left Main Gear Removal Path | FS 900.00, BL -180.00, WL 0.00 | Target | ±0.050 in (±1.270 mm) | Main gear removal verification |
| MMP-400-004-R | Right Main Gear Removal Path | FS 900.00, BL 180.00, WL 0.00 | Target | ±0.050 in (±1.270 mm) | Main gear removal verification |

### 9.3 System Access Measurement Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| MMP-100-001-C | Forward Equipment Bay Access | FS 150.00, BL 0.00, WL 75.00 | Target | ±0.050 in (±1.270 mm) | Equipment bay access verification |
| MMP-200-001-C | Mid Equipment Bay Access | FS 750.00, BL 0.00, WL 75.00 | Target | ±0.050 in (±1.270 mm) | Equipment bay access verification |
| MMP-300-001-C | Aft Equipment Bay Access | FS 1450.00, BL 0.00, WL 75.00 | Target | ±0.050 in (±1.270 mm) | Equipment bay access verification |
| MMP-500-001-C | Crown Access Panel Reference | FS 900.00, BL 0.00, WL 240.00 | Target | ±0.050 in (±1.270 mm) | Crown area access verification |
| MMP-400-005-C | Cargo Floor Access Panel Reference | FS 750.00, BL 0.00, WL 85.00 | Target | ±0.050 in (±1.270 mm) | Below floor access verification |

### 9.4 Control Surface Maintenance Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| MMP-600-001-L | Left Aileron Hinge Access | FS 877.50, BL -660.00, WL 177.50 | Target | ±0.050 in (±1.270 mm) | Aileron maintenance access verification |
| MMP-600-001-R | Right Aileron Hinge Access | FS 877.50, BL 660.00, WL 177.50 | Target | ±0.050 in (±1.270 mm) | Aileron maintenance access verification |
| MMP-600-002-L | Left Flap Track Access | FS 855.00, BL -300.00, WL 140.00 | Target | ±0.050 in (±1.270 mm) | Flap maintenance access verification |
| MMP-600-002-R | Right Flap Track Access | FS 855.00, BL 300.00, WL 140.00 | Target | ±0.050 in (±1.270 mm) | Flap maintenance access verification |
| MMP-700-001-L | Left Elevator Hinge Access | FS 1650.00, BL -175.00, WL 325.00 | Target | ±0.050 in (±1.270 mm) | Elevator maintenance access verification |
| MMP-700-001-R | Right Elevator Hinge Access | FS 1650.00, BL 175.00, WL 325.00 | Target | ±0.050 in (±1.270 mm) | Elevator maintenance access verification |
| MMP-700-002-C | Rudder Hinge Access | FS 1600.00, BL 0.00, WL 475.00 | Target | ±0.050 in (±1.270 mm) | Rudder maintenance access verification |

## 10. Operational Verification Measurement Points

### 10.1 Flight Control Rigging Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| OMP-600-001-L | Left Aileron Neutral Position | FS 877.50, BL -660.00, WL 177.50 | Target | ±0.100 in (±2.540 mm) | Aileron rigging verification |
| OMP-600-001-R | Right Aileron Neutral Position | FS 877.50, BL 660.00, WL 177.50 | Target | ±0.100 in (±2.540 mm) | Aileron rigging verification |
| OMP-600-002-L | Left Flap Retracted Position | FS 855.00, BL -300.00, WL 140.00 | Target | ±0.100 in (±2.540 mm) | Flap rigging verification |
| OMP-600-002-R | Right Flap Retracted Position | FS 855.00, BL 300.00, WL 140.00 | Target | ±0.100 in (±2.540 mm) | Flap rigging verification |
| OMP-700-001-L | Left Elevator Neutral Position | FS 1650.00, BL -175.00, WL 325.00 | Target | ±0.100 in (±2.540 mm) | Elevator rigging verification |
| OMP-700-001-R | Right Elevator Neutral Position | FS 1650.00, BL 175.00, WL 325.00 | Target | ±0.100 in (±2.540 mm) | Elevator rigging verification |
| OMP-700-002-C | Rudder Neutral Position | FS 1600.00, BL 0.00, WL 475.00 | Target | ±0.100 in (±2.540 mm) | Rudder rigging verification |

### 10.2 Landing Gear Rigging Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| OMP-400-001-C | Nose Gear Down Lock | FS 150.00, BL 0.00, WL 25.00 | Target | ±0.100 in (±2.540 mm) | Nose gear down lock verification |
| OMP-400-002-C | Nose Gear Up Lock | FS 150.00, BL 0.00, WL 75.00 | Target | ±0.100 in (±2.540 mm) | Nose gear up lock verification |
| OMP-400-003-L | Left Main Gear Down Lock | FS 900.00, BL -180.00, WL 25.00 | Target | ±0.100 in (±2.540 mm) | Main gear down lock verification |
| OMP-400-003-R | Right Main Gear Down Lock | FS 900.00, BL 180.00, WL 25.00 | Target | ±0.100 in (±2.540 mm) | Main gear down lock verification |
| OMP-400-004-L | Left Main Gear Up Lock | FS 900.00, BL -180.00, WL 100.00 | Target | ±0.100 in (±2.540 mm) | Main gear up lock verification |
| OMP-400-004-R | Right Main Gear Up Lock | FS 900.00, BL 180.00, WL 100.00 | Target | ±0.100 in (±2.540 mm) | Main gear up lock verification |

### 10.3 Door Rigging Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| OMP-100-001-L | Forward Left Door Closed Position | FS 350.00, BL -120.00, WL 125.00 | Target | ±0.100 in (±2.540 mm) | Door rigging verification |
| OMP-100-001-R | Forward Right Door Closed Position | FS 350.00, BL 120.00, WL 125.00 | Target | ±0.100 in (±2.540 mm) | Door rigging verification |
| OMP-300-001-L | Aft Left Door Closed Position | FS 1350.00, BL -120.00, WL 125.00 | Target | ±0.100 in (±2.540 mm) | Door rigging verification |
| OMP-300-001-R | Aft Right Door Closed Position | FS 1350.00, BL 120.00, WL 125.00 | Target | ±0.100 in (±2.540 mm) | Door rigging verification |
| OMP-400-001-L | Forward Cargo Door Closed Position | FS 400.00, BL -120.00, WL 50.00 | Target | ±0.100 in (±2.540 mm) | Cargo door rigging verification |
| OMP-400-002-L | Aft Cargo Door Closed Position | FS 1100.00, BL -120.00, WL 50.00 | Target | ±0.100 in (±2.540 mm) | Cargo door rigging verification |

### 10.4 Novel Technology Operational Verification Points

| ID | Description | Location (FS, BL, WL) | Physical Feature | Precision Requirement | Usage |
|----|-------------|------------------------|------------------|------------------------|-------|
| OMP-800-001-C | Quantum Propulsion System Operational Reference | FS 1250.00, BL 0.00, WL 175.00 | Target | ±0.100 in (±2.540 mm) | QPS operational verification |
| OMP-800-002-C | Hydrogen Fuel System Operational Reference | FS 1350.00, BL 0.00, WL 100.00 | Target | ±0.100 in (±2.540 mm) | Hydrogen system operational verification |
| OMP-800-003-C | Energy Harvesting System Operational Reference | FS 1500.00, BL 0.00, WL 200.00 | Target | ±0.100 in (±2.540 mm) | Energy system operational verification |
| OMP-800-004-C | Self-Healing Structure Operational Reference | FS 900.00, BL 0.00, WL 125.00 | Target | ±0.100 in (±2.540 mm) | Self-healing system operational verification |

## 11. Conclusion

This Measurement Point Definitions Table establishes the comprehensive catalog of all measurement points, reference locations, and dimensional verification positions for the AMPEL360XWLRGA aircraft. It provides the authoritative reference for all measurement activities throughout the aircraft's lifecycle, from design and manufacturing to maintenance and repair operations.

The document defines the measurement point identification system, primary reference measurement points, secondary reference measurement points, critical interface measurement points, assembly verification measurement points, system alignment measurement points, novel technology measurement points, maintenance reference measurement points, and operational verification measurement points.

All measurement points specified in this document shall be used as the primary reference for identifying, locating, and verifying critical measurement points required for dimensional control, assembly verification, and operational maintenance. Any deviations from these specifications must be approved through the formal engineering change process.

---

**Document Control**

| Revision | Date | Description | Author | Approver |
|----------|------|-------------|--------|----------|
| A | 2025-02-20 | Initial Release | GAIA Air Engineering | Chief Engineer |
| - | 2025-01-25 | Draft for Review | GAIA Air Engineering | - |
| - | 2024-12-28 | Initial Draft | GAIA Air Engineering | - |

**Appendices**

- Appendix A: Measurement Point Location Diagrams (Electronic Format)
- Appendix B: Measurement Point Access Instructions (Electronic Format)
- Appendix C: Measurement Equipment Requirements (Electronic Format)
- Appendix D: Measurement Point Verification Procedures (Electronic Format)