
# GAIA Documentation Ecosystem - Unified Overview & Master Index (v1.3 - Fully Expanded)

> **Disclaimer - GenAI Proposal Status**: Esta documentación representa una propuesta generada mediante tecnologías de Inteligencia Artificial Generativa y está sujeta a revisión y validación por expertos del dominio antes de su implementación.

## Document Information

| Field           | Value                                        |
| :-------------- | :------------------------------------------- |
| Document ID     | GAIA-DOC-ECOSYSTEM-INDEX-v1.3              |
| Revision        | 1.3                                          |
| Date            | 2025-05-04                                   |
| Status          | DRAFT                                        |
| Applicability   | GAIA AIR & SPACE PROGRAMS (All Platforms)    |

## 1. Purpose & Scope

This document provides the master overview and unified index for the entire GAIA Documentation Ecosystem, encompassing both GAIA AIR and GAIA SPACE programs. It integrates the structural organization defined by the Air Table of Contents (AToC - based on ATA chapters) and the Space Table of Contents (SToC - based on SNS chapters) with the semantic definitions from the GAIA Aerospace Table of Program Content Ontology (GASTOP-CO2).

The purpose is to establish a single entry point for navigating all technical documentation, standards, and project artifacts, ensuring consistency, traceability, and support for advanced knowledge management, including AI agent integration, across all GAIA platforms.

## 2. Foundational Framework Components

The GAIA Documentation Ecosystem is built upon the following core components:

*   **Air Table of Contents (AToC):** Organizes GAIA AIR documentation based on ATA chapters (00-99) and additional common parts. *(See Section 5)*
*   **Space Table of Contents (SToC):** Organizes GAIA SPACE documentation based on a Space Numbering System (SNS) with parts covering Spacecraft Systems (SS), Mission Operations (MO), Environment (SE), Launch (LS), Project Management (PM), and Research (SR). *(See Section 6)*
*   **GAIA Aerospace Table of Program Content Ontology (GASTOP-CO2):** Provides the semantic layer defining the *meaning* and *relationships* between different content types across both domains. *(Refer to `GASToP-CO2` document for full details)*
*   **GAIA-CO-ASD-LIB Standard:** Defines common standards for file formats, naming conventions, and metadata applicable to all documents. *(See Section 4)*
*   **Unified INFOCODE Index:** A common set of codes classifying document purpose across both AToC and SToC. *(See Section 3)*

## 3. Unified INFOCODE-INDEX

| Code   | Description                        | File Format       | AToC | SToC |
| :----- | :--------------------------------- | :---------------- | :--: | :--: |
| OV     | Overview                           | Markdown (.md)    | ✓    | ✓    |
| SPEC   | Specification                      | YAML (.yaml)      | ✓    | ✓    |
| SDD    | System Design Description          | YAML (.yaml)      | ✓    | ✓    |
| ICD    | Interface Control Document         | YAML (.yaml)      | ✓    | ✓    |
| PROC   | Procedure                          | Markdown (.md)    | ✓    | ✓    |
| DWG    | Drawing                            | SVG (.svg)        | ✓    | ✓    |
| LIST   | List                               | CSV (.csv)        | ✓    | ✓    |
| REQ    | Requirements                       | YAML (.yaml)      | ✓    | ✓    |
| GLO    | Glossary                           | Markdown (.md)    | ✓    | ✓    |
| PLAN   | Plan                               | Markdown (.md)    | ✓    | ✓    |
| ARCH   | Architecture                       | YAML (.yaml) + SVG (.svg) | ✓    | ✓    |
| SEC    | Security                           | YAML (.yaml)      | ✓    | ✓    |
| TEST   | Test Documentation                 | YAML (.yaml)      | ✓    | ✓    |
| TRN    | Training Material                  | Markdown (.md)    | ✓    | ✓    |
| UG     | User Guide                         | Markdown (.md)    | ✓    | ✓    |
| CAL    | Calculation / Analysis Report      | Markdown (.md)    | ✓    | ✓    |
| RPT    | Report                             | Markdown (.md)    | ✓    | ✓    |
| RES    | Research Document                  | Markdown (.md)    | ✓    | ✓    |
| MAN    | Manual                             | Markdown (.md)    | ✓    | ✓    |
| CAT    | Catalog / Parts List               | CSV (.csv)        | ✓    | ✓    |
| FIG    | Figure / Illustration              | SVG (.svg)        | ✓    | ✓    |
| CONOPS | Concept of Operations              | Markdown (.md)    | ✓    | ✓    |
| WBS    | Work Breakdown Structure           | Markdown (.md)    | ✓    | ✓    |
| JSON   | JSON Data / Schema                 | JSON (.json)      | ✓    | ✓    |
| BOM    | Bill of Materials                  | CSV (.csv)        | ✓    | ✓    |
| SWD    | Software Documentation (Container) | Markdown (.md)    | ✓    | ✓    |
| ADMIN  | Administrative Document            | Markdown (.md)    | ✓    | ✓    |
| REF    | Reference Document / Pointer       | Markdown (.md)    | ✓    | ✓    |
| IDX    | Index Document                     | Markdown (.md)    | ✓    | ✓    |
| MPD    | Maintenance Planning Document      | YAML (.yaml)      | ✓    | ✓    |
| WDM    | Wiring Diagram Manual              | Markdown (.md)    | ✓    | ✗    |
| CERT   | Certification Document             | Markdown (.md)    | ✓    | ✓    |
| PRES   | Presentation                       | Markdown (.md)    | ✓    | ✓    |
| BASE   | Baseline Document                  | Markdown (.md)    | ✓    | ✓    |
| MD     | Markdown Document (Generic)        | Markdown (.md)    | ✓    | ✓    |
| SCRIPT | Script / Code                      | (Various)         | ✓    | ✓    |
| NB     | Notebook (e.g., Jupyter)           | (Various)         | ✓    | ✓    |
| ORB    | Orbital Analysis                   | YAML (.yaml)      | ✗    | ✓    |
| RAD    | Radiation Analysis                 | YAML (.yaml)      | ✗    | ✓    |
| THERM  | Thermal Analysis                   | YAML (.yaml)      | ✓    | ✓    |
| SIM    | Simulation                         | YAML (.yaml)      | ✓    | ✓    |
| AERO   | Aerodynamic Analysis               | YAML (.yaml)      | ✓    | ✗    |
| PROP   | Propulsion Analysis                | YAML (.yaml)      | ✓    | ✓    |
| STRUCT | Structural Analysis                | YAML (.yaml)      | ✓    | ✓    |
| AVION  | Avionics Analysis                  | YAML (.yaml)      | ✓    | ✓    |
| XDOM   | Cross-Domain Reference             | Markdown (.md)    | ✓    | ✓    |

## 4. GAIA-CO-ASD-LIB Standard (Unified)

### File Formats

- **YAML (.yaml)**: Structured technical specifications, system descriptions, interface definitions, requirements, analysis inputs/outputs.
- **Markdown (.md)**: Narrative documentation, procedures, user guides, reports, manuals, glossaries, plans, administrative docs, reference pointers, indices.
- **SVG (.svg)**: Diagrams, drawings, figures.
- **CSV (.csv)**: Tabular data, lists, catalogs, BOMs.
- **JSON (.json)**: Machine-readable data structures, configuration, schemas.
- **Various:** Scripts, Notebooks (specific extension depends on language/tool).

### Naming Convention (Unified)
plaintext
[Project]-[Domain]-[Chapter]-[Section]-[Subject]-[InfoCode]-[Variant].[ext]
- **`[Project]`**: e.g., `GAIA`
- **`[Domain]`**: `AIR`, `SPACE`, or `COMMON`
- **`[Chapter]`**: ATA Chapter (e.g., `21`) for AIR, SNS Chapter (e.g., `SS-21`) for SPACE, or Functional Code (e.g., `PROP`) for COMMON.
- **`[Section]`**: e.g., `10` (ATA/SNS section)
- **`[Subject]`**: Descriptive subject identifier (e.g., `PropulsionSys`)
- **`[InfoCode]`**: Code from the INFOCODE-INDEX (e.g., `SDD`)
- **`[Variant]`**: e.g., `A` (AMPEL360XWLRGA variant), `B`, etc.
- **`.[ext]`**: File extension based on InfoCode/Format (e.g., `.yaml`, `.md`)

**Examples:**
- `GAIA-AIR-21-10-EnvCtrlSys-SDD-A.yaml`
- `GAIA-SPACE-SS-21-10-PropulsionSys-SDD-A.yaml`
- `GAIA-COMMON-PROP-00-PropulsionPrinciples-OV-A.md`

### Metadata (Unified Standard Example)

Each document must include the following standardized metadata header (example shown for YAML, adapt for Markdown):
yaml
---
# GAIA-CO-ASD-LIB Metadata Block v1.0
title: Document Title
documentID: GAIA-[Domain]-[Chapter]-[Section]-[Subject]-[InfoCode]-[Variant]
revision: X.X
date: YYYY-MM-DD # Effective date of this revision
status: [DRAFT|REVIEW|APPROVED|RELEASED|OBSOLETE] # Current status
applicability: # Structured Applicability
  platforms: [Platform1, Platform2] # e.g., [AMPEL360, AMPEL360+] or [AMPEL-SPACE]
  serial_numbers: [ALL | Range | List]
  modifications: [ModID1, ModID2 | ALL | NONE]
authors: # List of contributors to this revision
  - Author Name <email@example.com>
  - AI Agent Name (Model Version)
securityClass: [UNCLASSIFIED|RESTRICTED|CONFIDENTIAL|SECRET]
distribution: Distribution Statement (e.g., Distribution A)
export_control: Export Control Rating (e.g., EAR99, ITAR)
keywords: # Relevant search keywords
  - Keyword1
  - Keyword2
references: # Links to external standards or internal foundational docs
  - documentID: Referenced_Standard_ID
    title: Title of Referenced Standard
  - documentID: Foundational_Doc_ID
    title: Title of Foundational Document
related_documents: # Links to other GAIA documents within the ecosystem
  - documentID: Related_Doc_ID_1
    title: Title of Related Document 1
    relationship: [PARENT|CHILD|REFERENCES|IMPLEMENTS|VERIFIES|CONSTRAINS|...]
  - documentID: Related_Doc_ID_2
    title: Title of Related Document 2
    relationship: ...
revision_history:
  - revision: X.X
    date: YYYY-MM-DD
    author: Author Name
    summary: Description of changes in this revision
  - revision: X.Y
    date: YYYY-MM-DD
    author: Author Name
    summary: Description of changes in previous revision
---

# Document Title (for Markdown)

(... Document Content Starts Here ...)
---

## 5. Master Index Part I: GAIA AIR (AToC Structure)

*This section outlines the structure based on ATA chapters for Air Systems.*

<details>
<summary><strong>Expand Part I: ATA Chapters (00-99) Outline</strong></summary>

#### ATA 00: General
<details><summary>Expand ATA 00 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-00-00-00-General-OV-A.md](docs/air/00/GAIA-AIR-00-00-00-General-OV-A.md) | ATA 00 - General Information Overview       | Overview                     | DRAFT    |
| [GAIA-AIR-00-00-001-GeneralSpecs-SPEC-A.yaml](docs/air/00/GAIA-AIR-00-00-001-GeneralSpecs-SPEC-A.yaml) | General Specifications                      | Specification                | DRAFT    |
| [GAIA-AIR-00-00-002-Glossary-GLO-A.md](docs/air/00/GAIA-AIR-00-00-002-Glossary-GLO-A.md) | GAIA AIR Glossary                           | Glossary                     | DRAFT    |
| [GAIA-AIR-00-10-001-ReqMgmt-SPEC-A.yaml](docs/air/00/GAIA-AIR-00-10-001-ReqMgmt-SPEC-A.yaml) | Requirements Management Framework           | Specification                | DRAFT    |
| [GAIA-AIR-00-20-001-StdPractices-PROC-A.md](docs/air/00/GAIA-AIR-00-20-001-StdPractices-PROC-A.md) | Standard Practices - Airframe             | Procedure                    | DRAFT    |
| [GAIA-AIR-00-30-001-AircraftDim-DWG-A.svg](docs/air/00/GAIA-AIR-00-30-001-AircraftDim-DWG-A.svg) | Aircraft Dimensions and Areas               | Drawing                      | DRAFT    |
| [GAIA-AIR-00-40-001-LiftingProc-PROC-A.md](docs/air/00/GAIA-AIR-00-40-001-LiftingProc-PROC-A.md) | Aircraft Lifting Procedures                 | Procedure                    | DRAFT    |
| [GAIA-AIR-00-50-001-WeighingProc-PROC-A.md](docs/air/00/GAIA-AIR-00-50-001-WeighingProc-PROC-A.md) | Aircraft Weighing Procedures                | Procedure                    | DRAFT    |
| [GAIA-AIR-00-60-001-GroundHandling-PROC-A.md](docs/air/00/GAIA-AIR-00-60-001-GroundHandling-PROC-A.md) | Ground Handling Procedures                  | Procedure                    | DRAFT    |
| [GAIA-AIR-00-70-001-EnginePractices-PROC-A.md](docs/air/00/GAIA-AIR-00-70-001-EnginePractices-PROC-A.md) | Standard Practices - Engines                | Procedure                    | DRAFT    |
| [GAIA-AIR-00-80-001-SystemsPractices-PROC-A.md](docs/air/00/GAIA-AIR-00-80-001-SystemsPractices-PROC-A.md) | Standard Practices - Systems                | Procedure                    | DRAFT    |
| [GAIA-AIR-00-90-001-Integration-ICD-A.yaml](docs/air/00/GAIA-AIR-00-90-001-Integration-ICD-A.yaml) | GAIA AIR Systems Integration                | Interface Control Document | DRAFT    |
</details>

#### ATA 01: Aircraft General
<details><summary>Expand ATA 01 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-01-00-00-AircraftGeneral-OV-A.md](docs/air/01/GAIA-AIR-01-00-00-AircraftGeneral-OV-A.md) | ATA 01 - Aircraft General Overview          | Overview                     | DRAFT    |
</details>

#### ATA 02: Operations Information
<details><summary>Expand ATA 02 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-02-00-00-Operations-OV-A.md](docs/air/02/GAIA-AIR-02-00-00-Operations-OV-A.md) | ATA 02 - Operations Information Overview    | Overview                     | DRAFT    |
</details>

#### ATA 03: Performance
<details><summary>Expand ATA 03 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-03-00-00-Performance-OV-A.md](docs/air/03/GAIA-AIR-03-00-00-Performance-OV-A.md) | ATA 03 - Performance Overview               | Overview                     | DRAFT    |
</details>

#### ATA 04: Airworthiness
<details><summary>Expand ATA 04 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-04-00-00-Airworthiness-OV-A.md](docs/air/04/GAIA-AIR-04-00-00-Airworthiness-OV-A.md) | ATA 04 - Airworthiness Overview             | Overview                     | DRAFT    |
</details>

#### ATA 05: Time Limits / Maintenance Checks
<details><summary>Expand ATA 05 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-05-00-00-TimeLimits-OV-A.md](docs/air/05/GAIA-AIR-05-00-00-TimeLimits-OV-A.md) | ATA 05 - Time Limits / Maint. Checks Overview | Overview                     | DRAFT    |
| [GAIA-AIR-05-20-00-MaintPlanning-MPD-A.yaml](docs/air/05/GAIA-AIR-05-20-00-MaintPlanning-MPD-A.yaml) | Maintenance Planning Document               | Maintenance Planning Doc     | DRAFT    |
</details>

#### ATA 06: Dimensions & Areas
<details><summary>Expand ATA 06 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-06-00-00-Dimensions-OV-A.md](docs/air/06/GAIA-AIR-06-00-00-Dimensions-OV-A.md) | ATA 06 - Dimensions & Areas Overview        | Overview                     | DRAFT    |
</details>

#### ATA 07: Lifting & Shoring
<details><summary>Expand ATA 07 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-07-00-00-LiftingShoring-OV-A.md](docs/air/07/GAIA-AIR-07-00-00-LiftingShoring-OV-A.md) | ATA 07 - Lifting & Shoring Overview         | Overview                     | DRAFT    |
</details>

#### ATA 08: Leveling & Weighing
<details><summary>Expand ATA 08 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-08-00-00-LevelingWeighing-OV-A.md](docs/air/08/GAIA-AIR-08-00-00-LevelingWeighing-OV-A.md) | ATA 08 - Leveling & Weighing Overview       | Overview                     | DRAFT    |
</details>

#### ATA 09: Towing & Taxiing
<details><summary>Expand ATA 09 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-09-00-00-TowingTaxiing-OV-A.md](docs/air/09/GAIA-AIR-09-00-00-TowingTaxiing-OV-A.md) | ATA 09 - Towing & Taxiing Overview          | Overview                     | DRAFT    |
</details>

#### ATA 10: Parking, Mooring, Storage
<details><summary>Expand ATA 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-10-00-00-ParkingStorage-OV-A.md](docs/air/10/GAIA-AIR-10-00-00-ParkingStorage-OV-A.md) | ATA 10 - Parking, Mooring, Storage Overview | Overview                     | DRAFT    |
</details>

#### ATA 11: Placards & Markings
<details><summary>Expand ATA 11 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-11-00-00-PlacardsMarkings-OV-A.md](docs/air/11/GAIA-AIR-11-00-00-PlacardsMarkings-OV-A.md) | ATA 11 - Placards & Markings Overview       | Overview                     | DRAFT    |
</details>

#### ATA 12: Servicing – Routine
<details><summary>Expand ATA 12 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-12-00-00-Servicing-OV-A.md](docs/air/12/GAIA-AIR-12-00-00-Servicing-OV-A.md) | ATA 12 - Routine Servicing Overview         | Overview                     | DRAFT    |
</details>

#### ATA 13: Hydraulic Power (Minimal/EHA)
<details><summary>Expand ATA 13 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-13-00-00-HydraulicMinimal-OV-A.md](docs/air/13/GAIA-AIR-13-00-00-HydraulicMinimal-OV-A.md) | ATA 13 - Hydraulic Power (Minimal) Overview | Overview                     | DRAFT    |
</details>

#### ATA 14: Pneumatic Power (Minimal)
<details><summary>Expand ATA 14 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-14-00-00-PneumaticMinimal-OV-A.md](docs/air/14/GAIA-AIR-14-00-00-PneumaticMinimal-OV-A.md) | ATA 14 - Pneumatic Power (Minimal) Overview | Overview                     | DRAFT    |
</details>

#### ATA 15-17: (Merged into ATA 21)
<details><summary>Expand ATA 15-17 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-15-00-00-RefToATA21-REF-A.md](docs/air/15/GAIA-AIR-15-00-00-RefToATA21-REF-A.md) | ATA 15-17 Reference to ATA 21               | Reference Document           | DRAFT    |
</details>

#### ATA 18: Vibration & Noise Control
<details><summary>Expand ATA 18 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-18-00-00-VibrationNoise-OV-A.md](docs/air/18/GAIA-AIR-18-00-00-VibrationNoise-OV-A.md) | ATA 18 - Vibration & Noise Control Overview | Overview                     | DRAFT    |
</details>

#### ATA 19: Reserved for Future Use
<details><summary>Expand ATA 19 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-19-00-00-Reserved-REF-A.md](docs/air/19/GAIA-AIR-19-00-00-Reserved-REF-A.md) | ATA 19 - Reserved                           | Reference Document           | DRAFT    |
</details>

#### ATA 20: Standard Practices – Airframe
<details><summary>Expand ATA 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-20-00-00-StdPracticesAF-OV-A.md](docs/air/20/GAIA-AIR-20-00-00-StdPracticesAF-OV-A.md) | ATA 20 - Standard Practices Airframe Overview | Overview                     | DRAFT    |
| *(... Specific practices documents from comprehensive structure ...)* | | | |
</details>

#### ATA 21: Air Conditioning & Pressurization (ECS)
<details><summary>Expand ATA 21 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-21-00-00-ECS-OV-A.md](docs/air/21/GAIA-AIR-21-00-00-ECS-OV-A.md) | ATA 21 - ECS Overview                       | Overview                     | DRAFT    |
| [GAIA-AIR-21-10-EnvCtrlSys-SDD-A.yaml](docs/air/21/GAIA-AIR-21-10-EnvCtrlSys-SDD-A.yaml) | Environmental Control System SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-21-20-PressCtrlSys-SDD-A.yaml](docs/air/21/GAIA-AIR-21-20-PressCtrlSys-SDD-A.yaml) | Pressurization Control System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-21-30-AirDistribution-SDD-A.yaml](docs/air/21/GAIA-AIR-21-30-AirDistribution-SDD-A.yaml) | Air Distribution SDD                    | System Design Description    | DRAFT    |
| [GAIA-AIR-21-40-TempCtrl-SDD-A.yaml](docs/air/21/GAIA-AIR-21-40-TempCtrl-SDD-A.yaml) | Temperature Control SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-21-50-AirQuality-SDD-A.yaml](docs/air/21/GAIA-AIR-21-50-AirQuality-SDD-A.yaml) | Air Quality SDD                         | System Design Description    | DRAFT    |
| [GAIA-AIR-21-60-Refrigeration-SDD-A.yaml](docs/air/21/GAIA-AIR-21-60-Refrigeration-SDD-A.yaml) | Refrigeration SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-21-70-HumidityCtrl-SDD-A.yaml](docs/air/21/GAIA-AIR-21-70-HumidityCtrl-SDD-A.yaml) | Humidity Control SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-21-80-IntegratedECS-SDD-A.yaml](docs/air/21/GAIA-AIR-21-80-IntegratedECS-SDD-A.yaml) | Integrated ECS SDD                    | System Design Description    | DRAFT    |
| [GAIA-AIR-21-90-AIEnhancedClimateCtrl-SDD-A.yaml](docs/air/21/GAIA-AIR-21-90-AIEnhancedClimateCtrl-SDD-A.yaml) | AI Enhanced Climate Control SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-21-10-EnvCtrlSys-DWG-A.svg](docs/air/21/GAIA-AIR-21-10-EnvCtrlSys-DWG-A.svg) | Environmental Control System Drawing      | Drawing                      | DRAFT    |
| [GAIA-AIR-21-20-PressCtrlSys-DWG-A.svg](docs/air/21/GAIA-AIR-21-20-PressCtrlSys-DWG-A.svg) | Pressurization Control System Drawing     | Drawing                      | DRAFT    |
| [GAIA-AIR-21-00-ECSTroubleshooting-PROC-A.md](docs/air/21/GAIA-AIR-21-00-ECSTroubleshooting-PROC-A.md) | ECS Troubleshooting Procedure         | Procedure                    | DRAFT    |
| [GAIA-AIR-21-00-PressSystemCalibration-PROC-A.md](docs/air/21/GAIA-AIR-21-00-PressSystemCalibration-PROC-A.md) | Pressurization Calibration Procedure    | Procedure                    | DRAFT    |
| [GAIA-AIR-21-00-AirConditioningMaintenance-PROC-A.md](docs/air/21/GAIA-AIR-21-00-AirConditioningMaintenance-PROC-A.md) | Air Conditioning Maintenance Procedure  | Procedure                    | DRAFT    |
</details>

#### ATA 22: Auto Flight
<details><summary>Expand ATA 22 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-22-00-00-Autoflight-OV-A.md](docs/air/22/GAIA-AIR-22-00-00-Autoflight-OV-A.md) | ATA 22 - Auto Flight Overview               | Overview                     | DRAFT    |
| [GAIA-AIR-22-00-01-AmedeoCore-SDD-A.yaml](docs/air/22/GAIA-AIR-22-00-01-AmedeoCore-SDD-A.yaml) | AMEDEO_Core Module Specification            | System Design Description    | DRAFT    |
| [GAIA-AIR-22-00-02-SmaieModule-SDD-A.yaml](docs/air/22/GAIA-AIR-22-00-02-SmaieModule-SDD-A.yaml) | SMAIE_Module Specification                  | System Design Description    | DRAFT    |
| [GAIA-AIR-22-00-03-GaiaTaskflow-SDD-A.yaml](docs/air/22/GAIA-AIR-22-00-03-GaiaTaskflow-SDD-A.yaml) | GAIA_TASKFLOW Module Specification          | System Design Description    | DRAFT    |
| [GAIA-AIR-22-10-001-AutopilotInterface-ICD-A.yaml](docs/air/22/GAIA-AIR-22-10-001-AutopilotInterface-ICD-A.yaml) | Autopilot System Interface                  | Interface Control Document | DRAFT    |
| [GAIA-AIR-22-20-001-FlightDirector-SPEC-A.yaml](docs/air/22/GAIA-AIR-22-20-001-FlightDirector-SPEC-A.yaml) | Flight Director System Specification        | Specification                | DRAFT    |
| [GAIA-AIR-22-30-001-Autothrottle-SPEC-A.yaml](docs/air/22/GAIA-AIR-22-30-001-Autothrottle-SPEC-A.yaml) | Autothrottle System Specification           | Specification                | DRAFT    |
| [GAIA-AIR-22-40-001-AI-FCS-SPEC-A.yaml](docs/air/22/GAIA-AIR-22-40-001-AI-FCS-SPEC-A.yaml) | AI-Enhanced Flight Control System Spec      | Specification                | DRAFT    |
| [GAIA-AIR-22-00-001-AutoflightTest-TEST-A.yaml](docs/air/22/GAIA-AIR-22-00-001-AutoflightTest-TEST-A.yaml) | Auto Flight System Test Plan                | Test Documentation           | DRAFT    |
| [GAIA-AIR-22-00-001-AutoflightSecurity-SEC-A.yaml](docs/air/22/GAIA-AIR-22-00-001-AutoflightSecurity-SEC-A.yaml) | Auto Flight Security Analysis               | Security                     | DRAFT    |
</details>

#### ATA 23: Communications
<details><summary>Expand ATA 23 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-23-00-00-Communications-OV-A.md](docs/air/23/GAIA-AIR-23-00-00-Communications-OV-A.md) | ATA 23 - Communications Overview            | Overview                     | DRAFT    |
| [GAIA-AIR-23-00-01-GaiaSensorgrid-SDD-A.yaml](docs/air/23/GAIA-AIR-23-00-01-GaiaSensorgrid-SDD-A.yaml) | GAIA_SENSORGRID Module Specification        | System Design Description    | DRAFT    |
| [GAIA-AIR-23-10-001-RadioInterface-ICD-A.yaml](docs/air/23/GAIA-AIR-23-10-001-RadioInterface-ICD-A.yaml) | Radio Communication Interface               | Interface Control Document | DRAFT    |
| [GAIA-AIR-23-20-001-DataLink-SPEC-A.yaml](docs/air/23/GAIA-AIR-23-20-001-DataLink-SPEC-A.yaml) | Data Link System Specification              | Specification                | DRAFT    |
| [GAIA-AIR-23-30-001-Intercom-SPEC-A.yaml](docs/air/23/GAIA-AIR-23-30-001-Intercom-SPEC-A.yaml) | Intercom System Specification               | Specification                | DRAFT    |
| [GAIA-AIR-23-40-001-QuantumComm-SPEC-A.yaml](docs/air/23/GAIA-AIR-23-40-001-QuantumComm-SPEC-A.yaml) | Quantum Communication System Spec           | Specification                | DRAFT    |
</details>

#### ATA 24: Electrical Power
<details><summary>Expand ATA 24 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-24-00-00-ElectricalPower-OV-A.md](docs/air/24/GAIA-AIR-24-00-00-ElectricalPower-OV-A.md) | ATA 24 - Electrical Power Overview          | Overview                     | DRAFT    |
| [GAIA-AIR-24-00-01-NetzeroEngine-SDD-A.yaml](docs/air/24/GAIA-AIR-24-00-01-NetzeroEngine-SDD-A.yaml) | NETZERO_ENGINE Module Specification         | System Design Description    | DRAFT    |
| [GAIA-AIR-24-10-001-GeneratorSystem-SPEC-A.yaml](docs/air/24/GAIA-AIR-24-10-001-GeneratorSystem-SPEC-A.yaml) | Generator System Specification              | Specification                | DRAFT    |
| [GAIA-AIR-24-20-001-DistributionSystem-SPEC-A.yaml](docs/air/24/GAIA-AIR-24-20-001-DistributionSystem-SPEC-A.yaml) | Power Distribution System Specification     | Specification                | DRAFT    |
| [GAIA-AIR-24-30-001-BatterySystem-SPEC-A.yaml](docs/air/24/GAIA-AIR-24-30-001-BatterySystem-SPEC-A.yaml) | Battery System Specification                | Specification                | DRAFT    |
| [GAIA-AIR-24-40-001-ExternalPower-SPEC-A.yaml](docs/air/24/GAIA-AIR-24-40-001-ExternalPower-SPEC-A.yaml) | External Power System Specification         | Specification                | DRAFT    |
</details>

#### ATA 25: Equipment / Furnishings
<details><summary>Expand ATA 25 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-25-00-00-EquipmentFurnish-OV-A.md](docs/air/25/GAIA-AIR-25-00-00-EquipmentFurnish-OV-A.md) | ATA 25 - Equipment/Furnishings Overview   | Overview                     | DRAFT    |
| [GAIA-AIR-25-10-FlightDeck-SDD-A.yaml](docs/air/25/GAIA-AIR-25-10-FlightDeck-SDD-A.yaml) | Flight Deck Furnishings SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-25-20-Cabin-SDD-A.yaml](docs/air/25/GAIA-AIR-25-20-Cabin-SDD-A.yaml)      | Cabin Furnishings SDD                   | System Design Description    | DRAFT    |
| [GAIA-AIR-25-30-Lavatories-SDD-A.yaml](docs/air/25/GAIA-AIR-25-30-Lavatories-SDD-A.yaml) | Lavatories SDD                          | System Design Description    | DRAFT    |
| [GAIA-AIR-25-40-Cargo-SDD-A.yaml](docs/air/25/GAIA-AIR-25-40-Cargo-SDD-A.yaml)      | Cargo Furnishings SDD                   | System Design Description    | DRAFT    |
| [GAIA-AIR-25-50-ServiceAreas-SDD-A.yaml](docs/air/25/GAIA-AIR-25-50-ServiceAreas-SDD-A.yaml) | Service Areas SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-25-60-EmergencyEquip-SDD-A.yaml](docs/air/25/GAIA-AIR-25-60-EmergencyEquip-SDD-A.yaml) | Emergency Equipment SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-25-70-IFE-SDD-A.yaml](docs/air/25/GAIA-AIR-25-70-IFE-SDD-A.yaml)        | In-Flight Entertainment SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-25-80-SmartCabin-SDD-A.yaml](docs/air/25/GAIA-AIR-25-80-SmartCabin-SDD-A.yaml)   | Smart Cabin SDD                         | System Design Description    | DRAFT    |
| [GAIA-AIR-25-90-AdaptiveInteriors-SDD-A.yaml](docs/air/25/GAIA-AIR-25-90-AdaptiveInteriors-SDD-A.yaml) | Adaptive Interiors SDD                | System Design Description    | DRAFT    |
</details>

#### ATA 26: Fire Protection
<details><summary>Expand ATA 26 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-26-00-00-FireProtection-OV-A.md](docs/air/26/GAIA-AIR-26-00-00-FireProtection-OV-A.md) | ATA 26 - Fire Protection Overview           | Overview                     | DRAFT    |
| [GAIA-AIR-26-10-Detection-SDD-A.yaml](docs/air/26/GAIA-AIR-26-10-Detection-SDD-A.yaml)  | Fire Detection System SDD               | System Design Description    | DRAFT    |
| [GAIA-AIR-26-20-Extinguishing-SDD-A.yaml](docs/air/26/GAIA-AIR-26-20-Extinguishing-SDD-A.yaml) | Fire Extinguishing System SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-26-30-ExplosionSuppression-SDD-A.yaml](docs/air/26/GAIA-AIR-26-30-ExplosionSuppression-SDD-A.yaml) | Explosion Suppression System SDD      | System Design Description    | DRAFT    |
| [GAIA-AIR-26-40-Warning-SDD-A.yaml](docs/air/26/GAIA-AIR-26-40-Warning-SDD-A.yaml)    | Fire Warning System SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-26-50-AIFireRisk-SDD-A.yaml](docs/air/26/GAIA-AIR-26-50-AIFireRisk-SDD-A.yaml) | AI Fire Risk Assessment SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-26-10-FireDetectionDwg-DWG-A.svg](docs/air/26/GAIA-AIR-26-10-FireDetectionDwg-DWG-A.svg) | Fire Detection System Drawing           | Drawing                      | DRAFT    |
| [GAIA-AIR-26-20-ExtinguishingDwg-DWG-A.svg](docs/air/26/GAIA-AIR-26-20-ExtinguishingDwg-DWG-A.svg) | Fire Extinguishing System Drawing       | Drawing                      | DRAFT    |
| [GAIA-AIR-26-00-FireSystemCheck-PROC-A.md](docs/air/26/GAIA-AIR-26-00-FireSystemCheck-PROC-A.md) | Fire System Check Procedure             | Procedure                    | DRAFT    |
| [GAIA-AIR-26-00-EmergencyProcedures-PROC-A.md](docs/air/26/GAIA-AIR-26-00-EmergencyProcedures-PROC-A.md) | Fire Emergency Procedures             | Procedure                    | DRAFT    |
</details>

#### ATA 27: Flight Controls
<details><summary>Expand ATA 27 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-27-00-00-FlightControls-OV-A.md](docs/air/27/GAIA-AIR-27-00-00-FlightControls-OV-A.md) | ATA 27 - Flight Controls Overview           | Overview                     | DRAFT    |
| [GAIA-AIR-27-10-Aileron-SDD-A.yaml](docs/air/27/GAIA-AIR-27-10-Aileron-SDD-A.yaml)    | Aileron System SDD                      | System Design Description    | DRAFT    |
| [GAIA-AIR-27-20-Rudder-SDD-A.yaml](docs/air/27/GAIA-AIR-27-20-Rudder-SDD-A.yaml)     | Rudder System SDD                       | System Design Description    | DRAFT    |
| [GAIA-AIR-27-30-Elevator-SDD-A.yaml](docs/air/27/GAIA-AIR-27-30-Elevator-SDD-A.yaml)   | Elevator System SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-27-40-HorizontalStab-SDD-A.yaml](docs/air/27/GAIA-AIR-27-40-HorizontalStab-SDD-A.yaml) | Horizontal Stabilizer Control SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-27-50-Flaps-SDD-A.yaml](docs/air/27/GAIA-AIR-27-50-Flaps-SDD-A.yaml)      | Flaps Control System SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-27-60-Spoilers-SDD-A.yaml](docs/air/27/GAIA-AIR-27-60-Spoilers-SDD-A.yaml)   | Spoiler Control System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-27-70-GustLock-SDD-A.yaml](docs/air/27/GAIA-AIR-27-70-GustLock-SDD-A.yaml)   | Gust Lock & Damper System SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-27-80-LiftAugmentation-SDD-A.yaml](docs/air/27/GAIA-AIR-27-80-LiftAugmentation-SDD-A.yaml) | Lift Augmentation System SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-27-90-FlyByWire-SDD-A.yaml](docs/air/27/GAIA-AIR-27-90-FlyByWire-SDD-A.yaml)   | Fly-By-Wire System SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-27-95-AIFlightControl-SDD-A.yaml](docs/air/27/GAIA-AIR-27-95-AIFlightControl-SDD-A.yaml) | AI Flight Control System SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-27-10-AileronDwg-DWG-A.svg](docs/air/27/GAIA-AIR-27-10-AileronDwg-DWG-A.svg)    | Aileron System Drawing                  | Drawing                      | DRAFT    |
| [GAIA-AIR-27-90-FlyByWireDwg-DWG-A.svg](docs/air/27/GAIA-AIR-27-90-FlyByWireDwg-DWG-A.svg)  | Fly-By-Wire System Drawing              | Drawing                      | DRAFT    |
| [GAIA-AIR-27-00-FCSCalibration-PROC-A.md](docs/air/27/GAIA-AIR-27-00-FCSCalibration-PROC-A.md) | Flight Control System Calibration Proc  | Procedure                    | DRAFT    |
| [GAIA-AIR-27-00-ControlSurfaceInsp-PROC-A.md](docs/air/27/GAIA-AIR-27-00-ControlSurfaceInsp-PROC-A.md) | Control Surface Inspection Procedure  | Procedure                    | DRAFT    |
</details>

#### ATA 28: Fuel (Hybrid H2/SAF)
<details><summary>Expand ATA 28 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-28-00-00-FuelSystem-OV-A.md](docs/air/28/GAIA-AIR-28-00-00-FuelSystem-OV-A.md) | ATA 28 - Fuel System (Hybrid) Overview      | Overview                     | DRAFT    |
| [GAIA-AIR-28-10-Storage-SDD-A.yaml](docs/air/28/GAIA-AIR-28-10-Storage-SDD-A.yaml)        | Fuel Storage System SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-28-20-Distribution-SDD-A.yaml](docs/air/28/GAIA-AIR-28-20-Distribution-SDD-A.yaml)   | Fuel Distribution System SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-28-30-Dump-SDD-A.yaml](docs/air/28/GAIA-AIR-28-30-Dump-SDD-A.yaml)         | Fuel Dump System SDD                    | System Design Description    | DRAFT    |
| [GAIA-AIR-28-40-FuelIndication-SDD-A.yaml](docs/air/28/GAIA-AIR-28-40-FuelIndication-SDD-A.yaml) | Fuel Indication System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-28-50-SyntheticFuels-SDD-A.yaml](docs/air/28/GAIA-AIR-28-50-SyntheticFuels-SDD-A.yaml) | Synthetic Fuels System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-28-60-HydrogenFuel-SDD-A.yaml](docs/air/28/GAIA-AIR-28-60-HydrogenFuel-SDD-A.yaml)   | Hydrogen Fuel System SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-28-70-FuelManagement-SDD-A.yaml](docs/air/28/GAIA-AIR-28-70-FuelManagement-SDD-A.yaml) | Fuel Management System SDD              | System Design Description    | DRAFT    |
</details>

#### ATA 29: Hydraulic Power (Actuation Focus)
<details><summary>Expand ATA 29 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-29-00-00-HydraulicAct-OV-A.md](docs/air/29/GAIA-AIR-29-00-00-HydraulicAct-OV-A.md)  | ATA 29 - Hydraulic Power (Actuation) Overview | Overview                     | DRAFT    |
| [GAIA-AIR-29-10-MainSystem-SDD-A.yaml](docs/air/29/GAIA-AIR-29-10-MainSystem-SDD-A.yaml)     | Main Hydraulic System SDD               | System Design Description    | DRAFT    |
| [GAIA-AIR-29-20-AuxiliarySystem-SDD-A.yaml](docs/air/29/GAIA-AIR-29-20-AuxiliarySystem-SDD-A.yaml) | Auxiliary Hydraulic System SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-29-30-Indication-SDD-A.yaml](docs/air/29/GAIA-AIR-29-30-Indication-SDD-A.yaml)    | Hydraulic Indication System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-29-40-ElectroHydrostatic-SDD-A.yaml](docs/air/29/GAIA-AIR-29-40-ElectroHydrostatic-SDD-A.yaml) | Electro-Hydrostatic Actuation SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-29-50-SmartActuators-SDD-A.yaml](docs/air/29/GAIA-AIR-29-50-SmartActuators-SDD-A.yaml)  | Smart Hydraulic Actuators SDD         | System Design Description    | DRAFT    |
</details>

#### ATA 30: Ice & Rain Protection
<details><summary>Expand ATA 30 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-30-00-00-IceRainProt-OV-A.md](docs/air/30/GAIA-AIR-30-00-00-IceRainProt-OV-A.md)  | ATA 30 - Ice & Rain Protection Overview     | Overview                     | DRAFT    |
| [GAIA-AIR-30-10-Airfoil-SDD-A.yaml](docs/air/30/GAIA-AIR-30-10-Airfoil-SDD-A.yaml)        | Airfoil Ice Protection SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-30-20-AirIntakes-SDD-A.yaml](docs/air/30/GAIA-AIR-30-20-AirIntakes-SDD-A.yaml)     | Air Intake Ice Protection SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-30-30-PitotStatic-SDD-A.yaml](docs/air/30/GAIA-AIR-30-30-PitotStatic-SDD-A.yaml)    | Pitot/Static Ice Protection SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-30-40-Windows-SDD-A.yaml](docs/air/30/GAIA-AIR-30-40-Windows-SDD-A.yaml)        | Windows Ice/Rain Protection SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-30-50-Antennas-SDD-A.yaml](docs/air/30/GAIA-AIR-30-50-Antennas-SDD-A.yaml)       | Antennas Ice Protection SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-30-60-PropellerRotors-SDD-A.yaml](docs/air/30/GAIA-AIR-30-60-PropellerRotors-SDD-A.yaml) | Propeller/Rotors Ice Protection SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-30-70-WaterLine-SDD-A.yaml](docs/air/30/GAIA-AIR-30-70-WaterLine-SDD-A.yaml)      | Water Line Ice Protection SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-30-80-IceDetection-SDD-A.yaml](docs/air/30/GAIA-AIR-30-80-IceDetection-SDD-A.yaml)   | Ice Detection System SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-30-90-SmartDeicing-SDD-A.yaml](docs/air/30/GAIA-AIR-30-90-SmartDeicing-SDD-A.yaml)   | Smart De-icing System SDD               | System Design Description    | DRAFT    |
</details>

#### ATA 31: Indicating/Recording Systems
<details><summary>Expand ATA 31 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-31-00-00-IndicatingRecording-OV-A.md](docs/air/31/GAIA-AIR-31-00-00-IndicatingRecording-OV-A.md) | ATA 31 - Indicating/Recording Overview      | Overview                     | DRAFT    |
| [GAIA-AIR-31-00-01-EnvAnalyzer-SDD-A.yaml](docs/air/31/GAIA-AIR-31-00-01-EnvAnalyzer-SDD-A.yaml) | ENV_ANALYZER Module Specification           | System Design Description    | DRAFT    |
| [GAIA-AIR-31-10-InstrumentPanels-SDD-A.yaml](docs/air/31/GAIA-AIR-31-10-InstrumentPanels-SDD-A.yaml) | Instrument Panels SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-31-20-IndependentInstruments-SDD-A.yaml](docs/air/31/GAIA-AIR-31-20-IndependentInstruments-SDD-A.yaml) | Independent Instruments SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-31-30-Recorders-SDD-A.yaml](docs/air/31/GAIA-AIR-31-30-Recorders-SDD-A.yaml)    | Recorders SDD                         | System Design Description    | DRAFT    |
| [GAIA-AIR-31-40-CentralDisplaySys-SDD-A.yaml](docs/air/31/GAIA-AIR-31-40-CentralDisplaySys-SDD-A.yaml) | Central Display System SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-31-50-CentralAlertSys-SDD-A.yaml](docs/air/31/GAIA-AIR-31-50-CentralAlertSys-SDD-A.yaml) | Central Alert System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-31-60-InfoSystems-SDD-A.yaml](docs/air/31/GAIA-AIR-31-60-InfoSystems-SDD-A.yaml)    | Information Systems SDD               | System Design Description    | DRAFT    |
| [GAIA-AIR-31-70-AutomaticLogSys-SDD-A.yaml](docs/air/31/GAIA-AIR-31-70-AutomaticLogSys-SDD-A.yaml) | Automatic Log System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-31-80-AugmentedReality-SDD-A.yaml](docs/air/31/GAIA-AIR-31-80-AugmentedReality-SDD-A.yaml) | Augmented Reality Display SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-31-90-AIAssistant-SDD-A.yaml](docs/air/31/GAIA-AIR-31-90-AIAssistant-SDD-A.yaml)    | AI Assistant Interface SDD            | System Design Description    | DRAFT    |
</details>

#### ATA 32: Landing Gear
<details><summary>Expand ATA 32 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-32-00-00-LandingGear-OV-A.md](docs/air/32/GAIA-AIR-32-00-00-LandingGear-OV-A.md)   | ATA 32 - Landing Gear Overview              | Overview                     | DRAFT    |
| [GAIA-AIR-32-10-MainGear-SDD-A.yaml](docs/air/32/GAIA-AIR-32-10-MainGear-SDD-A.yaml)         | Main Landing Gear SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-32-20-NoseGear-SDD-A.yaml](docs/air/32/GAIA-AIR-32-20-NoseGear-SDD-A.yaml)         | Nose Landing Gear SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-32-30-ExtensionRetraction-SDD-A.yaml](docs/air/32/GAIA-AIR-32-30-ExtensionRetraction-SDD-A.yaml) | Extension & Retraction System SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-32-40-Wheels-SDD-A.yaml](docs/air/32/GAIA-AIR-32-40-Wheels-SDD-A.yaml)           | Wheels SDD                            | System Design Description    | DRAFT    |
| [GAIA-AIR-32-50-Brakes-SDD-A.yaml](docs/air/32/GAIA-AIR-32-50-Brakes-SDD-A.yaml)           | Brakes System SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-32-60-Steering-SDD-A.yaml](docs/air/32/GAIA-AIR-32-60-Steering-SDD-A.yaml)         | Steering System SDD                   | System Design Description    | DRAFT    |
| [GAIA-AIR-32-70-PositionWarning-SDD-A.yaml](docs/air/32/GAIA-AIR-32-70-PositionWarning-SDD-A.yaml)  | Position & Warning System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-32-80-DragBrace-SDD-A.yaml](docs/air/32/GAIA-AIR-32-80-DragBrace-SDD-A.yaml)        | Drag Brace System SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-32-90-AdaptiveLandingGear-SDD-A.yaml](docs/air/32/GAIA-AIR-32-90-AdaptiveLandingGear-SDD-A.yaml) | Adaptive Landing Gear System SDD      | System Design Description    | DRAFT    |
</details>

#### ATA 33: Lights
<details><summary>Expand ATA 33 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-33-00-00-Lights-OV-A.md](docs/air/33/GAIA-AIR-33-00-00-Lights-OV-A.md)         | ATA 33 - Lights Overview                    | Overview                     | DRAFT    |
| [GAIA-AIR-33-10-FlightCompartment-SDD-A.yaml](docs/air/33/GAIA-AIR-33-10-FlightCompartment-SDD-A.yaml) | Flight Compartment Lighting SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-33-20-PassengerCompartment-SDD-A.yaml](docs/air/33/GAIA-AIR-33-20-PassengerCompartment-SDD-A.yaml) | Passenger Compartment Lighting SDD    | System Design Description    | DRAFT    |
| [GAIA-AIR-33-30-CargoCompartment-SDD-A.yaml](docs/air/33/GAIA-AIR-33-30-CargoCompartment-SDD-A.yaml) | Cargo Compartment Lighting SDD        | System Design Description    | DRAFT    |
| [GAIA-AIR-33-40-Exterior-SDD-A.yaml](docs/air/33/GAIA-AIR-33-40-Exterior-SDD-A.yaml)       | Exterior Lighting SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-33-50-Emergency-SDD-A.yaml](docs/air/33/GAIA-AIR-33-50-Emergency-SDD-A.yaml)      | Emergency Lighting SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-33-60-SmartLighting-SDD-A.yaml](docs/air/33/GAIA-AIR-33-60-SmartLighting-SDD-A.yaml)  | Smart Lighting System SDD             | System Design Description    | DRAFT    |
</details>

#### ATA 34: Navigation
<details><summary>Expand ATA 34 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-34-00-00-Navigation-OV-A.md](docs/air/34/GAIA-AIR-34-00-00-Navigation-OV-A.md)     | ATA 34 - Navigation Overview                | Overview                     | DRAFT    |
| [GAIA-AIR-34-00-01-Amppath-SDD-A.yaml](docs/air/34/GAIA-AIR-34-00-01-Amppath-SDD-A.yaml)           | AMPPATH Module Specification                | System Design Description    | DRAFT    |
| [GAIA-AIR-34-10-FlightEnvironment-SDD-A.yaml](docs/air/34/GAIA-AIR-34-10-FlightEnvironment-SDD-A.yaml) | Flight Environment Data System SDD      | System Design Description    | DRAFT    |
| [GAIA-AIR-34-20-AttitudeDirection-SDD-A.yaml](docs/air/34/GAIA-AIR-34-20-AttitudeDirection-SDD-A.yaml) | Attitude & Direction System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-34-30-LandingApproach-SDD-A.yaml](docs/air/34/GAIA-AIR-34-30-LandingApproach-SDD-A.yaml) | Landing & Approach Aids SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-34-40-IndependentPosition-SDD-A.yaml](docs/air/34/GAIA-AIR-34-40-IndependentPosition-SDD-A.yaml) | Independent Position System SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-34-50-DependentPosition-SDD-A.yaml](docs/air/34/GAIA-AIR-34-50-DependentPosition-SDD-A.yaml) | Dependent Position System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-34-60-FlightManagement-SDD-A.yaml](docs/air/34/GAIA-AIR-34-60-FlightManagement-SDD-A.yaml) | Flight Management System SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-34-70-QuantumNavigation-SDD-A.yaml](docs/air/34/GAIA-AIR-34-70-QuantumNavigation-SDD-A.yaml) | Quantum Navigation System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-34-80-AINavAssistant-SDD-A.yaml](docs/air/34/GAIA-AIR-34-80-AINavAssistant-SDD-A.yaml)   | AI Navigation Assistant SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-34-90-SensorFusion-SDD-A.yaml](docs/air/34/GAIA-AIR-34-90-SensorFusion-SDD-A.yaml)     | Navigation Sensor Fusion SDD          | System Design Description    | DRAFT    |
</details>

#### ATA 35: Oxygen
<details><summary>Expand ATA 35 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-35-00-00-Oxygen-OV-A.md](docs/air/35/GAIA-AIR-35-00-00-Oxygen-OV-A.md)         | ATA 35 - Oxygen System Overview             | Overview                     | DRAFT    |
| [GAIA-AIR-35-10-CrewSystem-SDD-A.yaml](docs/air/35/GAIA-AIR-35-10-CrewSystem-SDD-A.yaml)     | Crew Oxygen System SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-35-20-PassengerSystem-SDD-A.yaml](docs/air/35/GAIA-AIR-35-20-PassengerSystem-SDD-A.yaml) | Passenger Oxygen System SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-35-30-PortableSystem-SDD-A.yaml](docs/air/35/GAIA-AIR-35-30-PortableSystem-SDD-A.yaml)  | Portable Oxygen System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-35-40-IndicationSystem-SDD-A.yaml](docs/air/35/GAIA-AIR-35-40-IndicationSystem-SDD-A.yaml) | Oxygen Indication System SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-35-50-SmartOxygenMgmt-SDD-A.yaml](docs/air/35/GAIA-AIR-35-50-SmartOxygenMgmt-SDD-A.yaml)  | Smart Oxygen Management SDD           | System Design Description    | DRAFT    |
</details>

#### ATA 36: Pneumatic
<details><summary>Expand ATA 36 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-36-00-00-Pneumatic-OV-A.md](docs/air/36/GAIA-AIR-36-00-00-Pneumatic-OV-A.md)      | ATA 36 - Pneumatic System Overview          | Overview                     | DRAFT    |
| [GAIA-AIR-36-10-Distribution-SDD-A.yaml](docs/air/36/GAIA-AIR-36-10-Distribution-SDD-A.yaml)   | Pneumatic Distribution System SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-36-20-Indication-SDD-A.yaml](docs/air/36/GAIA-AIR-36-20-Indication-SDD-A.yaml)    | Pneumatic Indication System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-36-30-SmartPneumatics-SDD-A.yaml](docs/air/36/GAIA-AIR-36-30-SmartPneumatics-SDD-A.yaml) | Smart Pneumatics System SDD             | System Design Description    | DRAFT    |
</details>

#### ATA 37: Vacuum
<details><summary>Expand ATA 37 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-37-00-00-Vacuum-OV-A.md](docs/air/37/GAIA-AIR-37-00-00-Vacuum-OV-A.md)         | ATA 37 - Vacuum System Overview             | Overview                     | DRAFT    |
</details>

#### ATA 38: Water / Waste
<details><summary>Expand ATA 38 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-38-00-00-WaterWaste-OV-A.md](docs/air/38/GAIA-AIR-38-00-00-WaterWaste-OV-A.md)    | ATA 38 - Water / Waste System Overview      | Overview                     | DRAFT    |
| [GAIA-AIR-38-10-PotableWater-SDD-A.yaml](docs/air/38/GAIA-AIR-38-10-PotableWater-SDD-A.yaml)   | Potable Water System SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-38-20-WasteDisposal-SDD-A.yaml](docs/air/38/GAIA-AIR-38-20-WasteDisposal-SDD-A.yaml)  | Waste Disposal System SDD               | System Design Description    | DRAFT    |
| [GAIA-AIR-38-30-WaterRecycling-SDD-A.yaml](docs/air/38/GAIA-AIR-38-30-WaterRecycling-SDD-A.yaml) | Water Recycling System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-38-40-SmartWaterMgmt-SDD-A.yaml](docs/air/38/GAIA-AIR-38-40-SmartWaterMgmt-SDD-A.yaml) | Smart Water Management SDD            | System Design Description    | DRAFT    |
</details>

#### ATA 39: Electrical/Electronic Panels
<details><summary>Expand ATA 39 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-39-00-00-ElecPanels-OV-A.md](docs/air/39/GAIA-AIR-39-00-00-ElecPanels-OV-A.md)    | ATA 39 - Electrical/Electronic Panels Overview | Overview                     | DRAFT    |
</details>

#### ATA 41: Water Ballast
<details><summary>Expand ATA 41 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-41-00-00-WaterBallast-OV-A.md](docs/air/41/GAIA-AIR-41-00-00-WaterBallast-OV-A.md)  | ATA 41 - Water Ballast System Overview      | Overview                     | DRAFT    |
</details>

#### ATA 42: Integrated Modular Avionics
<details><summary>Expand ATA 42 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-42-00-00-IMA-OV-A.md](docs/air/42/GAIA-AIR-42-00-00-IMA-OV-A.md)            | ATA 42 - IMA Overview                       | Overview                     | DRAFT    |
| [GAIA-AIR-42-00-001-IMAArchitecture-ARCH-A.yaml](docs/air/42/GAIA-AIR-42-00-001-IMAArchitecture-ARCH-A.yaml) | IMA System Architecture                     | Architecture                 | DRAFT    |
| [GAIA-AIR-42-10-GeneralArchitecture-SDD-A.yaml](docs/air/42/GAIA-AIR-42-10-GeneralArchitecture-SDD-A.yaml) | IMA General Architecture SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-42-20-ProcessingModules-SDD-A.yaml](docs/air/42/GAIA-AIR-42-20-ProcessingModules-SDD-A.yaml) | IMA Processing Modules SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-42-30-NetworkComponents-SDD-A.yaml](docs/air/42/GAIA-AIR-42-30-NetworkComponents-SDD-A.yaml) | IMA Network Components SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-42-40-GatewayModules-SDD-A.yaml](docs/air/42/GAIA-AIR-42-40-GatewayModules-SDD-A.yaml)  | IMA Gateway Modules SDD               | System Design Description    | DRAFT    |
| [GAIA-AIR-42-50-QuantumComputing-SDD-A.yaml](docs/air/42/GAIA-AIR-42-50-QuantumComputing-SDD-A.yaml) | IMA Quantum Computing Integration SDD   | System Design Description    | DRAFT    |
| [GAIA-AIR-42-60-AIAccelerators-SDD-A.yaml](docs/air/42/GAIA-AIR-42-60-AIAccelerators-SDD-A.yaml)  | IMA AI Accelerators Integration SDD   | System Design Description    | DRAFT    |
| [GAIA-AIR-42-70-CyberphysicalModules-SDD-A.yaml](docs/air/42/GAIA-AIR-42-70-CyberphysicalModules-SDD-A.yaml) | IMA Cyberphysical Modules SDD         | System Design Description    | DRAFT    |
</details>

#### ATA 44: Cabin Systems
<details><summary>Expand ATA 44 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-44-00-00-CabinSystems-OV-A.md](docs/air/44/GAIA-AIR-44-00-00-CabinSystems-OV-A.md)  | ATA 44 - Cabin Systems Overview             | Overview                     | DRAFT    |
| [GAIA-AIR-44-10-CabinCore-SDD-A.yaml](docs/air/44/GAIA-AIR-44-10-CabinCore-SDD-A.yaml)          | Cabin Core System SDD                   | System Design Description    | DRAFT    |
| [GAIA-AIR-44-20-InFlightEntertainment-SDD-A.yaml](docs/air/44/GAIA-AIR-44-20-InFlightEntertainment-SDD-A.yaml) | In-Flight Entertainment System SDD    | System Design Description    | DRAFT    |
| [GAIA-AIR-44-30-CabinIntercommunication-SDD-A.yaml](docs/air/44/GAIA-AIR-44-30-CabinIntercommunication-SDD-A.yaml) | Cabin Intercommunication System SDD   | System Design Description    | DRAFT    |
| [GAIA-AIR-44-40-ExternalCommunication-SDD-A.yaml](docs/air/44/GAIA-AIR-44-40-ExternalCommunication-SDD-A.yaml) | External Communication System SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-44-50-CabinMonitoring-SDD-A.yaml](docs/air/44/GAIA-AIR-44-50-CabinMonitoring-SDD-A.yaml)     | Cabin Monitoring System SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-44-60-MiscellaneousCabin-SDD-A.yaml](docs/air/44/GAIA-AIR-44-60-MiscellaneousCabin-SDD-A.yaml)  | Miscellaneous Cabin Systems SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-44-70-AIPassengerExperience-SDD-A.yaml](docs/air/44/GAIA-AIR-44-70-AIPassengerExperience-SDD-A.yaml) | AI Passenger Experience SDD           | System Design Description    | DRAFT    |
</details>

#### ATA 45: Central Maintenance System
<details><summary>Expand ATA 45 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-45-00-00-CMS-OV-A.md](docs/air/45/GAIA-AIR-45-00-00-CMS-OV-A.md)            | ATA 45 - Central Maintenance System Overview| Overview                     | DRAFT    |
| [GAIA-AIR-45-00-01-GaiaChaincore-SDD-A.yaml](docs/air/45/GAIA-AIR-45-00-01-GaiaChaincore-SDD-A.yaml) | GAIA_CHAINCORE Module Specification         | System Design Description    | DRAFT    |
| [GAIA-AIR-45-10-CMSArchitecture-SDD-A.yaml](docs/air/45/GAIA-AIR-45-10-CMSArchitecture-SDD-A.yaml)   | CMS Architecture SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-45-20-FaultProcessing-SDD-A.yaml](docs/air/45/GAIA-AIR-45-20-FaultProcessing-SDD-A.yaml)  | CMS Fault Processing SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-45-30-MaintenanceProcessing-SDD-A.yaml](docs/air/45/GAIA-AIR-45-30-MaintenanceProcessing-SDD-A.yaml) | CMS Maintenance Processing SDD        | System Design Description    | DRAFT    |
| [GAIA-AIR-45-40-CMSInterfaces-SDD-A.yaml](docs/air/45/GAIA-AIR-45-40-CMSInterfaces-SDD-A.yaml)    | CMS Interfaces SDD                    | System Design Description    | DRAFT    |
| [GAIA-AIR-45-50-PredictiveMaintenance-SDD-A.yaml](docs/air/45/GAIA-AIR-45-50-PredictiveMaintenance-SDD-A.yaml) | Predictive Maintenance Integration SDD | System Design Description    | DRAFT    |
| [GAIA-AIR-45-60-AIMaintenance-SDD-A.yaml](docs/air/45/GAIA-AIR-45-60-AIMaintenance-SDD-A.yaml)      | AI Maintenance Assistant SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-45-70-DigitalTwin-SDD-A.yaml](docs/air/45/GAIA-AIR-45-70-DigitalTwin-SDD-A.yaml)      | CMS Digital Twin Integration SDD      | System Design Description    | DRAFT    |
| [GAIA-AIR-45-00-CMSUserGuide-UG-A.md](docs/air/45/GAIA-AIR-45-00-CMSUserGuide-UG-A.md)          | CMS User Guide                        | User Guide                   | DRAFT    |
| [GAIA-AIR-45-00-TroubleshootingFlows-PROC-A.md](docs/air/45/GAIA-AIR-45-00-TroubleshootingFlows-PROC-A.md) | CMS Troubleshooting Procedures        | Procedure                    | DRAFT    |
</details>

#### ATA 46: Information Systems
<details><summary>Expand ATA 46 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-46-00-00-InfoSystems-OV-A.md](docs/air/46/GAIA-AIR-46-00-00-InfoSystems-OV-A.md) | ATA 46 - Information Systems Overview     | Overview                     | DRAFT    |
| [GAIA-AIR-46-00-01-Ethicflow-SDD-A.yaml](docs/air/46/GAIA-AIR-46-00-01-Ethicflow-SDD-A.yaml)         | ETHICFLOW Module Specification              | System Design Description    | DRAFT    |
| [GAIA-AIR-46-10-AIAirAssistant-SDD-A.yaml](docs/air/46/GAIA-AIR-46-10-AIAirAssistant-SDD-A.yaml)   | AI Air Assistant SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-46-20-AircraftNetworks-SDD-A.yaml](docs/air/46/GAIA-AIR-46-20-AircraftNetworks-SDD-A.yaml) | Aircraft Networks SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-46-30-FlightOperationsSys-SDD-A.yaml](docs/air/46/GAIA-AIR-46-30-FlightOperationsSys-SDD-A.yaml) | Flight Operations Systems SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-46-40-MaintenanceInfo-SDD-A.yaml](docs/air/46/GAIA-AIR-46-40-MaintenanceInfo-SDD-A.yaml) | Maintenance Information System SDD    | System Design Description    | DRAFT    |
| [GAIA-AIR-46-50-ElecLibrary-SDD-A.yaml](docs/air/46/GAIA-AIR-46-50-ElecLibrary-SDD-A.yaml)    | Electronic Library System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-46-60-DataAnalytics-SDD-A.yaml](docs/air/46/GAIA-AIR-46-60-DataAnalytics-SDD-A.yaml)  | Data Analytics Platform SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-46-70-QuantumDataProcessing-SDD-A.yaml](docs/air/46/GAIA-AIR-46-70-QuantumDataProcessing-SDD-A.yaml) | Quantum Data Processing SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-46-80-EdgeComputing-SDD-A.yaml](docs/air/46/GAIA-AIR-46-80-EdgeComputing-SDD-A.yaml)    | Edge Computing Platform SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-46-90-AIDataIntegration-SDD-A.yaml](docs/air/46/GAIA-AIR-46-90-AIDataIntegration-SDD-A.yaml) | AI Data Integration SDD               | System Design Description    | DRAFT    |
</details>

#### ATA 47: Nitrogen Generation System (NGS)
<details><summary>Expand ATA 47 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-47-00-00-NGS-OV-A.md](docs/air/47/GAIA-AIR-47-00-00-NGS-OV-A.md)            | ATA 47 - NGS Overview                       | Overview                     | DRAFT    |
| [GAIA-AIR-47-10-DistributionSys-SDD-A.yaml](docs/air/47/GAIA-AIR-47-10-DistributionSys-SDD-A.yaml) | NGS Distribution System SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-47-20-IndicationCtrlSys-SDD-A.yaml](docs/air/47/GAIA-AIR-47-20-IndicationCtrlSys-SDD-A.yaml) | NGS Indication & Control System SDD   | System Design Description    | DRAFT    |
| [GAIA-AIR-47-30-SmartNitrogenMgmt-SDD-A.yaml](docs/air/47/GAIA-AIR-47-30-SmartNitrogenMgmt-SDD-A.yaml) | Smart Nitrogen Management SDD         | System Design Description    | DRAFT    |
</details>

#### ATA 48: Reserved for Future Use
<details><summary>Expand ATA 48 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-48-00-00-Reserved-REF-A.md](docs/air/48/GAIA-AIR-48-00-00-Reserved-REF-A.md) | ATA 48 - Reserved                           | Reference Document           | DRAFT    |
</details>

#### ATA 49: Airborne Auxiliary Power (AAP/APU)
<details><summary>Expand ATA 49 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-49-00-00-APU-OV-A.md](docs/air/49/GAIA-AIR-49-00-00-APU-OV-A.md)            | ATA 49 - APU Overview                       | Overview                     | DRAFT    |
| [GAIA-AIR-49-10-PowerUnit-SDD-A.yaml](docs/air/49/GAIA-AIR-49-10-PowerUnit-SDD-A.yaml)      | APU Power Unit SDD                    | System Design Description    | DRAFT    |
| [GAIA-AIR-49-20-EngineSystem-SDD-A.yaml](docs/air/49/GAIA-AIR-49-20-EngineSystem-SDD-A.yaml)   | APU Engine System SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-49-30-StartSystem-SDD-A.yaml](docs/air/49/GAIA-AIR-49-30-StartSystem-SDD-A.yaml)    | APU Start System SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-49-40-FuelSystem-SDD-A.yaml](docs/air/49/GAIA-AIR-49-40-FuelSystem-SDD-A.yaml)     | APU Fuel System SDD                   | System Design Description    | DRAFT    |
| [GAIA-AIR-49-50-HydrogenAPU-SDD-A.yaml](docs/air/49/GAIA-AIR-49-50-HydrogenAPU-SDD-A.yaml)    | Hydrogen APU SDD                      | System Design Description    | DRAFT    |
| [GAIA-AIR-49-60-FuelCellAPU-SDD-A.yaml](docs/air/49/GAIA-AIR-49-60-FuelCellAPU-SDD-A.yaml)    | Fuel Cell APU SDD                     | System Design Description    | DRAFT    |
</details>

#### ATA 50: Cargo and Accessory Compartments
<details><summary>Expand ATA 50 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-50-00-00-CargoCompart-OV-A.md](docs/air/50/GAIA-AIR-50-00-00-CargoCompart-OV-A.md)  | ATA 50 - Cargo & Accessory Compartments Overview | Overview                     | DRAFT    |
</details>

#### ATA 51: Structures – General
<details><summary>Expand ATA 51 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-51-00-00-StructuresGen-OV-A.md](docs/air/51/GAIA-AIR-51-00-00-StructuresGen-OV-A.md) | ATA 51 - Structures General Overview        | Overview                     | DRAFT    |
| *(... SHM, BIO, SM, MF subsections and documents ...)* | | | |
</details>

#### ATA 52: Doors
<details><summary>Expand ATA 52 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-52-00-00-Doors-OV-A.md](docs/air/52/GAIA-AIR-52-00-00-Doors-OV-A.md)          | ATA 52 - Doors Overview                     | Overview                     | DRAFT    |
| [GAIA-AIR-52-10-PassengerCrew-SDD-A.yaml](docs/air/52/GAIA-AIR-52-10-PassengerCrew-SDD-A.yaml) | Passenger/Crew Doors SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-52-20-Emergency-SDD-A.yaml](docs/air/52/GAIA-AIR-52-20-Emergency-SDD-A.yaml)      | Emergency Exit Doors SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-52-30-Cargo-SDD-A.yaml](docs/air/52/GAIA-AIR-52-30-Cargo-SDD-A.yaml)          | Cargo Doors SDD                       | System Design Description    | DRAFT    |
| [GAIA-AIR-52-40-Service-SDD-A.yaml](docs/air/52/GAIA-AIR-52-40-Service-SDD-A.yaml)        | Service Doors SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-52-50-FixedInterior-SDD-A.yaml](docs/air/52/GAIA-AIR-52-50-FixedInterior-SDD-A.yaml)  | Fixed Interior Doors SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-52-60-Entrance-SDD-A.yaml](docs/air/52/GAIA-AIR-52-60-Entrance-SDD-A.yaml)       | Entrance Doors SDD                    | System Design Description    | DRAFT    |
| [GAIA-AIR-52-70-Monitoring-SDD-A.yaml](docs/air/52/GAIA-AIR-52-70-Monitoring-SDD-A.yaml)     | Door Monitoring System SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-52-80-SmartDoors-SDD-A.yaml](docs/air/52/GAIA-AIR-52-80-SmartDoors-SDD-A.yaml)     | Smart Door Systems SDD                | System Design Description    | DRAFT    |
</details>

#### ATA 53: Fuselage
<details><summary>Expand ATA 53 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-53-00-00-Fuselage-OV-A.md](docs/air/53/GAIA-AIR-53-00-00-Fuselage-OV-A.md)       | ATA 53 - Fuselage Overview                  | Overview                     | DRAFT    |
| [GAIA-AIR-53-10-Structure-SDD-A.yaml](docs/air/53/GAIA-AIR-53-10-Structure-SDD-A.yaml)      | Fuselage Structure SDD                  | System Design Description    | DRAFT    |
| [GAIA-AIR-53-20-Plates-SDD-A.yaml](docs/air/53/GAIA-AIR-53-20-Plates-SDD-A.yaml)         | Fuselage Plates/Skin SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-53-30-CompositeStructures-SDD-A.yaml](docs/air/53/GAIA-AIR-53-30-CompositeStructures-SDD-A.yaml) | Fuselage Composite Structures SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-53-40-MetamaterialsApp-SDD-A.yaml](docs/air/53/GAIA-AIR-53-40-MetamaterialsApp-SDD-A.yaml) | Fuselage Metamaterials Application SDD | System Design Description    | DRAFT    |
| [GAIA-AIR-53-50-StructuralSensors-SDD-A.yaml](docs/air/53/GAIA-AIR-53-50-StructuralSensors-SDD-A.yaml) | Fuselage Structural Sensors SDD       | System Design Description    | DRAFT    |
| [GAIA-AIR-53-60-SelfHealingStructures-SDD-A.yaml](docs/air/53/GAIA-AIR-53-60-SelfHealingStructures-SDD-A.yaml) | Fuselage Self-Healing Structures SDD  | System Design Description    | DRAFT    |
</details>

#### ATA 54: Nacelles/Pylons
<details><summary>Expand ATA 54 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-54-00-00-NacellesPylons-OV-A.md](docs/air/54/GAIA-AIR-54-00-00-NacellesPylons-OV-A.md) | ATA 54 - Nacelles/Pylons Overview           | Overview                     | DRAFT    |
| [GAIA-AIR-54-10-NacelleStructure-SDD-A.yaml](docs/air/54/GAIA-AIR-54-10-NacelleStructure-SDD-A.yaml) | Nacelle Structure SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-54-20-PylonStructure-SDD-A.yaml](docs/air/54/GAIA-AIR-54-20-PylonStructure-SDD-A.yaml)   | Pylon Structure SDD                   | System Design Description    | DRAFT    |
| [GAIA-AIR-54-30-AttachFittings-SDD-A.yaml](docs/air/54/GAIA-AIR-54-30-AttachFittings-SDD-A.yaml) | Nacelle/Pylon Attach Fittings SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-54-40-AcousticTreatment-SDD-A.yaml](docs/air/54/GAIA-AIR-54-40-AcousticTreatment-SDD-A.yaml) | Nacelle Acoustic Treatment SDD        | System Design Description    | DRAFT    |
| [GAIA-AIR-54-50-ActiveFlowControl-SDD-A.yaml](docs/air/54/GAIA-AIR-54-50-ActiveFlowControl-SDD-A.yaml) | Nacelle Active Flow Control SDD       | System Design Description    | DRAFT    |
</details>

#### ATA 55: Stabilizers
<details><summary>Expand ATA 55 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-55-00-00-Stabilizers-OV-A.md](docs/air/55/GAIA-AIR-55-00-00-Stabilizers-OV-A.md)    | ATA 55 - Stabilizers Overview               | Overview                     | DRAFT    |
| [GAIA-AIR-55-10-HorizStabStructure-SDD-A.yaml](docs/air/55/GAIA-AIR-55-10-HorizStabStructure-SDD-A.yaml) | Horizontal Stabilizer Structure SDD   | System Design Description    | DRAFT    |
| [GAIA-AIR-55-20-VertStabStructure-SDD-A.yaml](docs/air/55/GAIA-AIR-55-20-VertStabStructure-SDD-A.yaml)  | Vertical Stabilizer Structure SDD     | System Design Description    | DRAFT    |
| [GAIA-AIR-55-30-MorphingStructures-SDD-A.yaml](docs/air/55/GAIA-AIR-55-30-MorphingStructures-SDD-A.yaml) | Stabilizer Morphing Structures SDD    | System Design Description    | DRAFT    |
| [GAIA-AIR-55-40-AdaptiveStabilizers-SDD-A.yaml](docs/air/55/GAIA-AIR-55-40-AdaptiveStabilizers-SDD-A.yaml) | Adaptive Stabilizers SDD              | System Design Description    | DRAFT    |
</details>

#### ATA 56: Windows
<details><summary>Expand ATA 56 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-56-00-00-Windows-OV-A.md](docs/air/56/GAIA-AIR-56-00-00-Windows-OV-A.md)        | ATA 56 - Windows Overview                   | Overview                     | DRAFT    |
| [GAIA-AIR-56-10-FlightCompartment-SDD-A.yaml](docs/air/56/GAIA-AIR-56-10-FlightCompartment-SDD-A.yaml) | Flight Compartment Windows SDD        | System Design Description    | DRAFT    |
| [GAIA-AIR-56-20-Cabin-SDD-A.yaml](docs/air/56/GAIA-AIR-56-20-Cabin-SDD-A.yaml)          | Cabin Windows SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-56-30-Door-SDD-A.yaml](docs/air/56/GAIA-AIR-56-30-Door-SDD-A.yaml)           | Door Windows SDD                      | System Design Description    | DRAFT    |
| [GAIA-AIR-56-40-Inspection-SDD-A.yaml](docs/air/56/GAIA-AIR-56-40-Inspection-SDD-A.yaml)     | Inspection Windows SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-56-50-SmartWindows-SDD-A.yaml](docs/air/56/GAIA-AIR-56-50-SmartWindows-SDD-A.yaml)     | Smart Windows SDD                     | System Design Description    | DRAFT    |
| [GAIA-AIR-56-60-AR-HUD-Integration-SDD-A.yaml](docs/air/56/GAIA-AIR-56-60-AR-HUD-Integration-SDD-A.yaml) | AR/HUD Integration SDD              | System Design Description    | DRAFT    |
</details>

#### ATA 57: Wings
<details><summary>Expand ATA 57 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-57-00-00-Wings-OV-A.md](docs/air/57/GAIA-AIR-57-00-00-Wings-OV-A.md)          | ATA 57 - Wings Overview                     | Overview                     | DRAFT    |
| [GAIA-AIR-57-10-CenterWing-SDD-A.yaml](docs/air/57/GAIA-AIR-57-10-CenterWing-SDD-A.yaml)     | Center Wing Structure SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-57-20-OuterWing-SDD-A.yaml](docs/air/57/GAIA-AIR-57-20-OuterWing-SDD-A.yaml)      | Outer Wing Structure SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-57-30-WingTips-SDD-A.yaml](docs/air/57/GAIA-AIR-57-30-WingTips-SDD-A.yaml)       | Wing Tips SDD                         | System Design Description    | DRAFT    |
| [GAIA-AIR-57-40-LeadingEdge-SDD-A.yaml](docs/air/57/GAIA-AIR-57-40-LeadingEdge-SDD-A.yaml)    | Leading Edge Structure SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-57-50-TrailingEdge-SDD-A.yaml](docs/air/57/GAIA-AIR-57-50-TrailingEdge-SDD-A.yaml)   | Trailing Edge Structure SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-57-60-MorphingWingSys-SDD-A.yaml](docs/air/57/GAIA-AIR-57-60-MorphingWingSys-SDD-A.yaml) | Morphing Wing System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-57-70-AdaptiveWingTips-SDD-A.yaml](docs/air/57/GAIA-AIR-57-70-AdaptiveWingTips-SDD-A.yaml) | Adaptive Wing Tips SDD                | System Design Description    | DRAFT    |
</details>

#### ATA 60: Standard Practices – Engine
<details><summary>Expand ATA 60 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-60-00-00-StdPracticesEng-OV-A.md](docs/air/60/GAIA-AIR-60-00-00-StdPracticesEng-OV-A.md) | ATA 60 - Standard Practices Engine Overview | Overview                     | DRAFT    |
</details>

#### ATA 61: Propellers/Propulsors
<details><summary>Expand ATA 61 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-61-00-00-Propulsors-OV-A.md](docs/air/61/GAIA-AIR-61-00-00-Propulsors-OV-A.md)     | ATA 61 - Propellers/Propulsors Overview     | Overview                     | DRAFT    |
</details>

#### ATA 62-67: Rotorcraft Specific
<details><summary>Expand ATA 62-67 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-62-00-00-RotorcraftNA-REF-A.md](docs/air/62/GAIA-AIR-62-00-00-RotorcraftNA-REF-A.md) | ATA 62-67 - Rotorcraft Specific (N/A)       | Reference Document           | DRAFT    |
</details>

#### ATA 71: Power Plant–General
<details><summary>Expand ATA 71 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-71-00-00-PowerPlantGen-OV-A.md](docs/air/71/GAIA-AIR-71-00-00-PowerPlantGen-OV-A.md) | ATA 71 - Power Plant General Overview       | Overview                     | DRAFT    |
| [GAIA-AIR-71-10-Cowling-SDD-A.yaml](docs/air/71/GAIA-AIR-71-10-Cowling-SDD-A.yaml)          | Engine Cowling System SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-71-20-Mounts-SDD-A.yaml](docs/air/71/GAIA-AIR-71-20-Mounts-SDD-A.yaml)           | Engine Mount System SDD               | System Design Description    | DRAFT    |
| [GAIA-AIR-71-30-FireSeals-SDD-A.yaml](docs/air/71/GAIA-AIR-71-30-FireSeals-SDD-A.yaml)        | Engine Fire Seals SDD                 | System Design Description    | DRAFT    |
| [GAIA-AIR-71-40-Attach-SDD-A.yaml](docs/air/71/GAIA-AIR-71-40-Attach-SDD-A.yaml)           | Engine Attach Fittings SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-71-50-Electrical-SDD-A.yaml](docs/air/71/GAIA-AIR-71-50-Electrical-SDD-A.yaml)       | Engine Electrical Interfaces SDD      | System Design Description    | DRAFT    |
| [GAIA-AIR-71-60-AirIntake-SDD-A.yaml](docs/air/71/GAIA-AIR-71-60-AirIntake-SDD-A.yaml)        | Engine Air Intake System SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-71-70-DrainSystems-SDD-A.yaml](docs/air/71/GAIA-AIR-71-70-DrainSystems-SDD-A.yaml)     | Engine Drain Systems SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-71-80-ElectricPowerplant-SDD-A.yaml](docs/air/71/GAIA-AIR-71-80-ElectricPowerplant-SDD-A.yaml) | Electric Powerplant Integration SDD   | System Design Description    | DRAFT    |
| [GAIA-AIR-71-90-HydrogenPropulsion-SDD-A.yaml](docs/air/71/GAIA-AIR-71-90-HydrogenPropulsion-SDD-A.yaml) | Hydrogen Propulsion Integration SDD   | System Design Description    | DRAFT    |
</details>

#### ATA 72: Engine (Turbine/Hybrid/H2)
<details><summary>Expand ATA 72 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-72-00-00-Engine-OV-A.md](docs/air/72/GAIA-AIR-72-00-00-Engine-OV-A.md)         | ATA 72 - Engine Overview                    | Overview                     | DRAFT    |
| *(... Specific engine component documents ...)* | | | |
</details>

#### ATA 73: Engine Fuel & Control
<details><summary>Expand ATA 73 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-73-00-00-EngineFuelCtrl-OV-A.md](docs/air/73/GAIA-AIR-73-00-00-EngineFuelCtrl-OV-A.md) | ATA 73 - Engine Fuel & Control Overview     | Overview                     | DRAFT    |
| [GAIA-AIR-73-10-Distribution-SDD-A.yaml](docs/air/73/GAIA-AIR-73-10-Distribution-SDD-A.yaml)   | Engine Fuel Distribution SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-73-20-Controlling-SDD-A.yaml](docs/air/73/GAIA-AIR-73-20-Controlling-SDD-A.yaml)    | Engine Fuel Controlling SDD           | System Design Description    | DRAFT    |
| [GAIA-AIR-73-30-Indicating-SDD-A.yaml](docs/air/73/GAIA-AIR-73-30-Indicating-SDD-A.yaml)     | Engine Fuel Indicating SDD            | System Design Description    | DRAFT    |
| [GAIA-AIR-73-40-AIEnhancedControl-SDD-A.yaml](docs/air/73/GAIA-AIR-73-40-AIEnhancedControl-SDD-A.yaml) | AI Enhanced Fuel Control SDD          | System Design Description    | DRAFT    |
| [GAIA-AIR-73-50-AlternativeFuelCtrl-SDD-A.yaml](docs/air/73/GAIA-AIR-73-50-AlternativeFuelCtrl-SDD-A.yaml) | Alternative Fuel Control SDD        | System Design Description    | DRAFT    |
</details>

#### ATA 74: Ignition
<details><summary>Expand ATA 74 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-74-00-00-Ignition-OV-A.md](docs/air/74/GAIA-AIR-74-00-00-Ignition-OV-A.md)       | ATA 74 - Ignition Overview                  | Overview                     | DRAFT    |
| [GAIA-AIR-74-10-ElectricalPower-SDD-A.yaml](docs/air/74/GAIA-AIR-74-10-ElectricalPower-SDD-A.yaml) | Ignition Electrical Power SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-74-20-Distribution-SDD-A.yaml](docs/air/74/GAIA-AIR-74-20-Distribution-SDD-A.yaml)   | Ignition Distribution SDD             | System Design Description    | DRAFT    |
| [GAIA-AIR-74-30-SwitchingCtrl-SDD-A.yaml](docs/air/74/GAIA-AIR-74-30-SwitchingCtrl-SDD-A.yaml)  | Ignition Switching/Control SDD        | System Design Description    | DRAFT    |
| [GAIA-AIR-74-40-PlasmaIgnition-SDD-A.yaml](docs/air/74/GAIA-AIR-74-40-PlasmaIgnition-SDD-A.yaml)  | Plasma Ignition System SDD            | System Design Description    | DRAFT    |
</details>

#### ATA 75: Air (Engine Bleed/ECS Input)
<details><summary>Expand ATA 75 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-75-00-00-EngineAir-OV-A.md](docs/air/75/GAIA-AIR-75-00-00-EngineAir-OV-A.md)     | ATA 75 - Engine Air Overview                | Overview                     | DRAFT    |
</details>

#### ATA 76: Engine Controls
<details><summary>Expand ATA 76 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-76-00-00-EngineControls-OV-A.md](docs/air/76/GAIA-AIR-76-00-00-EngineControls-OV-A.md) | ATA 76 - Engine Controls Overview           | Overview                     | DRAFT    |
| [GAIA-AIR-76-10-PowerCtrl-SDD-A.yaml](docs/air/76/GAIA-AIR-76-10-PowerCtrl-SDD-A.yaml)        | Power Control System SDD              | System Design Description    | DRAFT    |
| [GAIA-AIR-76-20-EmergencyShutdown-SDD-A.yaml](docs/air/76/GAIA-AIR-76-20-EmergencyShutdown-SDD-A.yaml) | Emergency Shutdown System SDD         | System Design Description    | DRAFT    |
| [GAIA-AIR-76-30-AIPowerOptimizer-SDD-A.yaml](docs/air/76/GAIA-AIR-76-30-AIPowerOptimizer-SDD-A.yaml)  | AI Power Optimizer SDD                | System Design Description    | DRAFT    |
| [GAIA-AIR-76-40-AdaptiveControl-SDD-A.yaml](docs/air/76/GAIA-AIR-76-40-AdaptiveControl-SDD-A.yaml)  | Adaptive Engine Control SDD           | System Design Description    | DRAFT    |
</details>

#### ATA 77: Engine Indication
<details><summary>Expand ATA 77 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-77-00-00-EngineIndication-OV-A.md](docs/air/77/GAIA-AIR-77-00-00-EngineIndication-OV-A.md) | ATA 77 - Engine Indication Overview         | Overview                     | DRAFT    |
</details>

#### ATA 78: Exhaust
<details><summary>Expand ATA 78 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-78-00-00-Exhaust-OV-A.md](docs/air/78/GAIA-AIR-78-00-00-Exhaust-OV-A.md)        | ATA 78 - Exhaust Overview                   | Overview                     | DRAFT    |
</details>

#### ATA 79: Oil
<details><summary>Expand ATA 79 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-79-00-00-OilSystem-OV-A.md](docs/air/79/GAIA-AIR-79-00-00-OilSystem-OV-A.md)     | ATA 79 - Oil System Overview                | Overview                     | DRAFT    |
</details>

#### ATA 80: Starting
<details><summary>Expand ATA 80 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-80-00-00-Starting-OV-A.md](docs/air/80/GAIA-AIR-80-00-00-Starting-OV-A.md)       | ATA 80 - Starting System Overview           | Overview                     | DRAFT    |
</details>

#### ATA 81: Turbines (Reciprocating Engines)
<details><summary>Expand ATA 81 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-81-00-00-RecipNA-REF-A.md](docs/air/81/GAIA-AIR-81-00-00-RecipNA-REF-A.md)               | ATA 81 - Reciprocating Engines (N/A)        | Reference Document           | DRAFT    |
</details>

#### ATA 82: Water Injection
<details><summary>Expand ATA 82 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-82-00-00-WaterInjectionNA-REF-A.md](docs/air/82/GAIA-AIR-82-00-00-WaterInjectionNA-REF-A.md)     | ATA 82 - Water Injection (N/A)              | Reference Document           | DRAFT    |
</details>

#### ATA 83: Accessory Gear Boxes
<details><summary>Expand ATA 83 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-83-00-00-AccGearbox-OV-A.md](docs/air/83/GAIA-AIR-83-00-00-AccGearbox-OV-A.md)    | ATA 83 - Accessory Gear Boxes Overview      | Overview                     | DRAFT    |
</details>

#### ATA 84: Reserved for Future Use
<details><summary>Expand ATA 84 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-84-00-00-Reserved-REF-A.md](docs/air/84/GAIA-AIR-84-00-00-Reserved-REF-A.md) | ATA 84 - Reserved                           | Reference Document           | DRAFT    |
</details>

#### ATA 85: Fuel Cell System
<details><summary>Expand ATA 85 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-85-00-00-FuelCell-OV-A.md](docs/air/85/GAIA-AIR-85-00-00-FuelCell-OV-A.md)      | ATA 85 - Fuel Cell System Overview          | Overview                     | DRAFT    |
</details>

#### ATA 91: Charts
<details><summary>Expand ATA 91 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-91-00-00-Charts-OV-A.md](docs/air/91/GAIA-AIR-91-00-00-Charts-OV-A.md)         | ATA 91 - Charts Overview                    | Overview                     | DRAFT    |
</details>

#### ATA 92: Electrical System Installation
<details><summary>Expand ATA 92 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-92-00-00-ElecInstall-OV-A.md](docs/air/92/GAIA-AIR-92-00-00-ElecInstall-OV-A.md)   | ATA 92 - Electrical Installation Overview   | Overview                     | DRAFT    |
</details>

#### ATA 95: Special Equipment (GSE)
<details><summary>Expand ATA 95 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-95-00-00-GSE-OV-A.md](docs/air/95/GAIA-AIR-95-00-00-GSE-OV-A.md)            | ATA 95 - Special Equipment (GSE) Overview   | Overview                     | DRAFT    |
</details>

#### ATA 97: Wiring Reporting
<details><summary>Expand ATA 97 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-97-00-00-WiringReport-OV-A.md](docs/air/97/GAIA-AIR-97-00-00-WiringReport-OV-A.md)  | ATA 97 - Wiring Reporting Overview          | Overview                     | DRAFT    |
</details>

#### ATA 99: Special / Emerging Tech
<details><summary>Expand ATA 99 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-AIR-99-00-00-SpecialTech-OV-A.md](docs/air/99/GAIA-AIR-99-00-00-SpecialTech-OV-A.md)   | ATA 99 - Special / Emerging Tech Overview   | Overview                     | DRAFT    |
</details>

</details>

---

## 6. Master Index Part II: GAIA SPACE (SToC Structure)

*This section outlines the structure based on the Space Numbering System (SNS) for Space Systems.*

### Part II: Spacecraft Systems (SS 00-99)

<details>
<summary><strong>Expand Part II: Spacecraft Systems (SS 00-99) Outline</strong></summary>

#### SS 10 - Structural Systems
<details><summary>Expand SS 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-10-00-Overview-OV-A.md](docs/space/ss/10/GAIA-SPACE-SS-10-00-Overview-OV-A.md) | SS 10 - Structural Systems Overview         | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-10-10-PrimaryStructure-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-10-PrimaryStructure-SDD-A.yaml) | Primary Structure SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-20-SecondaryStructure-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-20-SecondaryStructure-SDD-A.yaml) | Secondary Structure SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-30-MechanicalInterfaces-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-30-MechanicalInterfaces-SDD-A.yaml) | Mechanical Interfaces SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-40-DeployableSystems-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-40-DeployableSystems-SDD-A.yaml) | Deployable Systems SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-50-DockingMechanisms-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-50-DockingMechanisms-SDD-A.yaml) | Docking Mechanisms SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-60-SelfHealingStructures-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-60-SelfHealingStructures-SDD-A.yaml) | Self-Healing Structures SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-70-MetamaterialsApp-SDD-A.yaml](docs/space/ss/10/GAIA-SPACE-SS-10-70-MetamaterialsApp-SDD-A.yaml) | Metamaterials Application SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-10-10-PrimaryStructure-DWG-A.svg](docs/space/ss/10/GAIA-SPACE-SS-10-10-PrimaryStructure-DWG-A.svg) | Primary Structure Drawing             | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-10-40-DeployableSystems-DWG-A.svg](docs/space/ss/10/GAIA-SPACE-SS-10-40-DeployableSystems-DWG-A.svg) | Deployable Systems Drawing          | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-10-00-StructuralAnalysis-CAL-A.md](docs/space/ss/10/GAIA-SPACE-SS-10-00-StructuralAnalysis-CAL-A.md) | Structural Analysis Report            | Calculation / Analysis Report| DRAFT    |
</details>

#### SS 20 - Thermal Control Systems
<details><summary>Expand SS 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-20-00-Overview-OV-A.md](docs/space/ss/20/GAIA-SPACE-SS-20-00-Overview-OV-A.md) | SS 20 - Thermal Control Systems Overview    | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-20-10-PassiveThermalControl-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-10-PassiveThermalControl-SDD-A.yaml) | Passive Thermal Control SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-20-ActiveThermalControl-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-20-ActiveThermalControl-SDD-A.yaml) | Active Thermal Control SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-30-CryogenicSystems-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-30-CryogenicSystems-SDD-A.yaml) | Cryogenic Systems SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-40-ThermalProtection-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-40-ThermalProtection-SDD-A.yaml) | Thermal Protection System SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-50-ThermalMonitoring-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-50-ThermalMonitoring-SDD-A.yaml) | Thermal Monitoring System SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-60-AIThermalManagement-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-60-AIThermalManagement-SDD-A.yaml) | AI Thermal Management SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-70-AdaptiveThermalSystems-SDD-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-70-AdaptiveThermalSystems-SDD-A.yaml) | Adaptive Thermal Systems SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-20-10-PassiveThermalControl-DWG-A.svg](docs/space/ss/20/GAIA-SPACE-SS-20-10-PassiveThermalControl-DWG-A.svg) | Passive Thermal Control Drawing       | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-20-20-ActiveThermalControl-DWG-A.svg](docs/space/ss/20/GAIA-SPACE-SS-20-20-ActiveThermalControl-DWG-A.svg) | Active Thermal Control Drawing        | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-20-00-ThermalAnalysis-THERM-A.yaml](docs/space/ss/20/GAIA-SPACE-SS-20-00-ThermalAnalysis-THERM-A.yaml) | Thermal Analysis Data                 | Thermal Analysis             | DRAFT    |
</details>

#### SS 21 - Propulsion Systems
<details><summary>Expand SS 21 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-21-00-Overview-OV-A.md](docs/space/ss/21/GAIA-SPACE-SS-21-00-Overview-OV-A.md) | SS 21 - Propulsion Systems Overview       | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-21-10-ChemicalPropulsion-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-10-ChemicalPropulsion-SDD-A.yaml) | Chemical Propulsion SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-20-ElectricPropulsion-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-20-ElectricPropulsion-SDD-A.yaml) | Electric Propulsion SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-30-ColdGasSystems-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-30-ColdGasSystems-SDD-A.yaml) | Cold Gas Systems SDD                  | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-40-PropellantManagement-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-40-PropellantManagement-SDD-A.yaml) | Propellant Management SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-50-ThrustVectorControl-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-50-ThrustVectorControl-SDD-A.yaml) | Thrust Vector Control SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-60-PropulsionControl-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-60-PropulsionControl-SDD-A.yaml) | Propulsion Control System SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-70-NuclearPropulsion-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-70-NuclearPropulsion-SDD-A.yaml) | Nuclear Propulsion SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-80-AIPropulsionOptimizer-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-80-AIPropulsionOptimizer-SDD-A.yaml) | AI Propulsion Optimizer SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-90-QuantumPropulsion-SDD-A.yaml](docs/space/ss/21/GAIA-SPACE-SS-21-90-QuantumPropulsion-SDD-A.yaml) | Quantum Propulsion SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-21-10-ChemicalPropulsion-DWG-A.svg](docs/space/ss/21/GAIA-SPACE-SS-21-10-ChemicalPropulsion-DWG-A.svg) | Chemical Propulsion Drawing           | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-21-20-ElectricPropulsion-DWG-A.svg](docs/space/ss/21/GAIA-SPACE-SS-21-20-ElectricPropulsion-DWG-A.svg) | Electric Propulsion Drawing           | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-21-00-PropulsionCalibration-PROC-A.md](docs/space/ss/21/GAIA-SPACE-SS-21-00-PropulsionCalibration-PROC-A.md) | Propulsion Calibration Procedure      | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-21-00-ThrusterTesting-PROC-A.md](docs/space/ss/21/GAIA-SPACE-SS-21-00-ThrusterTesting-PROC-A.md) | Thruster Testing Procedure            | Procedure                    | DRAFT    |
</details>

#### SS 22 - Guidance, Navigation, and Control
<details><summary>Expand SS 22 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-22-00-Overview-OV-A.md](docs/space/ss/22/GAIA-SPACE-SS-22-00-Overview-OV-A.md) | SS 22 - GNC Overview                    | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-22-10-AttitudeDetermination-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-10-AttitudeDetermination-SDD-A.yaml) | Attitude Determination System SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-20-AttitudeControl-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-20-AttitudeControl-SDD-A.yaml) | Attitude Control System SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-30-NavigationSensors-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-30-NavigationSensors-SDD-A.yaml) | Navigation Sensors SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-40-OrbitDetermination-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-40-OrbitDetermination-SDD-A.yaml) | Orbit Determination System SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-50-ReactionWheels-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-50-ReactionWheels-SDD-A.yaml) | Reaction Wheels SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-60-MagneticTorquers-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-60-MagneticTorquers-SDD-A.yaml) | Magnetic Torquers SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-70-StarTrackers-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-70-StarTrackers-SDD-A.yaml)   | Star Trackers SDD                     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-80-GyrosAccelerometers-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-80-GyrosAccelerometers-SDD-A.yaml) | Gyros & Accelerometers SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-90-AIGNCSystem-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-90-AIGNCSystem-SDD-A.yaml)    | AI GNC System SDD                     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-95-QuantumNavigation-SDD-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-95-QuantumNavigation-SDD-A.yaml) | Quantum Navigation System SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-22-10-AttitudeDetermination-DWG-A.svg](docs/space/ss/22/GAIA-SPACE-SS-22-10-AttitudeDetermination-DWG-A.svg) | Attitude Determination System Drawing | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-22-50-ReactionWheels-DWG-A.svg](docs/space/ss/22/GAIA-SPACE-SS-22-50-ReactionWheels-DWG-A.svg) | Reaction Wheels Drawing               | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-22-00-GNCSelfTest-PROC-A.md](docs/space/ss/22/GAIA-SPACE-SS-22-00-GNCSelfTest-PROC-A.md)     | GNC Self-Test Procedure               | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-22-00-OrbitAnalysis-ORB-A.yaml](docs/space/ss/22/GAIA-SPACE-SS-22-00-OrbitAnalysis-ORB-A.yaml)  | Orbit Analysis Data                   | Orbital Analysis             | DRAFT    |
</details>

#### SS 23 - Communications Systems
<details><summary>Expand SS 23 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-23-00-Overview-OV-A.md](docs/space/ss/23/GAIA-SPACE-SS-23-00-Overview-OV-A.md) | SS 23 - Communications Systems Overview   | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-23-10-RadioFrequencySystems-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-10-RadioFrequencySystems-SDD-A.yaml) | Radio Frequency Systems SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-20-OpticalCommunications-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-20-OpticalCommunications-SDD-A.yaml) | Optical Communications SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-30-Antennas-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-30-Antennas-SDD-A.yaml)       | Antennas SDD                          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-40-Transponders-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-40-Transponders-SDD-A.yaml)   | Transponders SDD                      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-50-DataEncryption-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-50-DataEncryption-SDD-A.yaml) | Data Encryption SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-60-InterSatelliteLinks-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-60-InterSatelliteLinks-SDD-A.yaml) | Inter-Satellite Links SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-70-DeepSpaceComms-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-70-DeepSpaceComms-SDD-A.yaml) | Deep Space Communications SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-80-QuantumCommunications-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-80-QuantumCommunications-SDD-A.yaml) | Quantum Communications SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-90-AICommOptimizer-SDD-A.yaml](docs/space/ss/23/GAIA-SPACE-SS-23-90-AICommOptimizer-SDD-A.yaml) | AI Communications Optimizer SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-23-10-RadioFrequencySystems-DWG-A.svg](docs/space/ss/23/GAIA-SPACE-SS-23-10-RadioFrequencySystems-DWG-A.svg) | Radio Frequency Systems Drawing     | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-23-20-OpticalCommunications-DWG-A.svg](docs/space/ss/23/GAIA-SPACE-SS-23-20-OpticalCommunications-DWG-A.svg) | Optical Communications Drawing      | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-23-00-CommCheck-PROC-A.md](docs/space/ss/23/GAIA-SPACE-SS-23-00-CommCheck-PROC-A.md)       | Communications Check Procedure        | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-23-00-AntennaDeployment-PROC-A.md](docs/space/ss/23/GAIA-SPACE-SS-23-00-AntennaDeployment-PROC-A.md) | Antenna Deployment Procedure          | Procedure                    | DRAFT    |
</details>

#### SS 24 - Electrical Power Systems
<details><summary>Expand SS 24 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-24-00-Overview-OV-A.md](docs/space/ss/24/GAIA-SPACE-SS-24-00-Overview-OV-A.md) | SS 24 - Electrical Power Systems Overview | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-24-10-SolarArrays-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-10-SolarArrays-SDD-A.yaml)    | Solar Arrays SDD                      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-20-Batteries-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-20-Batteries-SDD-A.yaml)      | Batteries SDD                         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-30-PowerDistribution-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-30-PowerDistribution-SDD-A.yaml) | Power Distribution SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-40-PowerConditioning-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-40-PowerConditioning-SDD-A.yaml) | Power Conditioning SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-50-FuelCells-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-50-FuelCells-SDD-A.yaml)      | Fuel Cells SDD                        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-60-RadioisotopeSystems-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-60-RadioisotopeSystems-SDD-A.yaml) | Radioisotope Systems SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-70-SupercapacitorStorage-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-70-SupercapacitorStorage-SDD-A.yaml) | Supercapacitor Storage SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-80-AIPowerManagement-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-80-AIPowerManagement-SDD-A.yaml) | AI Power Management SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-90-QuantumEnergyHarvesting-SDD-A.yaml](docs/space/ss/24/GAIA-SPACE-SS-24-90-QuantumEnergyHarvesting-SDD-A.yaml) | Quantum Energy Harvesting SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-24-10-SolarArrays-DWG-A.svg](docs/space/ss/24/GAIA-SPACE-SS-24-10-SolarArrays-DWG-A.svg)    | Solar Arrays Drawing                  | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-24-30-PowerDistribution-DWG-A.svg](docs/space/ss/24/GAIA-SPACE-SS-24-30-PowerDistribution-DWG-A.svg) | Power Distribution Drawing          | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-24-00-BatteryMaintenance-PROC-A.md](docs/space/ss/24/GAIA-SPACE-SS-24-00-BatteryMaintenance-PROC-A.md) | Battery Maintenance Procedure         | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-24-00-PowerBudget-CAL-A.md](docs/space/ss/24/GAIA-SPACE-SS-24-00-PowerBudget-CAL-A.md)      | Power Budget Calculation              | Calculation / Analysis Report| DRAFT    |
</details>

#### SS 25 - Environmental Control and Life Support
<details><summary>Expand SS 25 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-25-00-Overview-OV-A.md](docs/space/ss/25/GAIA-SPACE-SS-25-00-Overview-OV-A.md) | SS 25 - ECLSS Overview                  | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-25-10-AtmosphereManagement-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-10-AtmosphereManagement-SDD-A.yaml) | Atmosphere Management System SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-20-WaterManagement-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-20-WaterManagement-SDD-A.yaml) | Water Management System SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-30-WasteManagement-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-30-WasteManagement-SDD-A.yaml) | Waste Management System SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-40-FireDetectionSuppression-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-40-FireDetectionSuppression-SDD-A.yaml) | Fire Detection & Suppression SDD    | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-50-FoodSystems-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-50-FoodSystems-SDD-A.yaml)    | Food Systems SDD                      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-60-CrewHabitation-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-60-CrewHabitation-SDD-A.yaml) | Crew Habitation Systems SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-70-BioregenerativeSystems-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-70-BioregenerativeSystems-SDD-A.yaml) | Bioregenerative Systems SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-80-AILifeSupportOptimizer-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-80-AILifeSupportOptimizer-SDD-A.yaml) | AI Life Support Optimizer SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-90-ClosedLoopECLSS-SDD-A.yaml](docs/space/ss/25/GAIA-SPACE-SS-25-90-ClosedLoopECLSS-SDD-A.yaml) | Closed-Loop ECLSS SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-25-10-AtmosphereManagement-DWG-A.svg](docs/space/ss/25/GAIA-SPACE-SS-25-10-AtmosphereManagement-DWG-A.svg) | Atmosphere Management Drawing       | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-25-60-CrewHabitation-DWG-A.svg](docs/space/ss/25/GAIA-SPACE-SS-25-60-CrewHabitation-DWG-A.svg) | Crew Habitation Drawing               | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-25-00-LifeSupportCheck-PROC-A.md](docs/space/ss/25/GAIA-SPACE-SS-25-00-LifeSupportCheck-PROC-A.md) | Life Support Check Procedure          | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-25-00-EmergencyProcedures-PROC-A.md](docs/space/ss/25/GAIA-SPACE-SS-25-00-EmergencyProcedures-PROC-A.md) | ECLSS Emergency Procedures          | Procedure                    | DRAFT    |
</details>

#### SS 26 - Payload Systems
<details><summary>Expand SS 26 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-26-00-Overview-OV-A.md](docs/space/ss/26/GAIA-SPACE-SS-26-00-Overview-OV-A.md) | SS 26 - Payload Systems Overview          | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-26-10-ScientificInstruments-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-10-ScientificInstruments-SDD-A.yaml) | Scientific Instruments SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-20-EarthObservation-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-20-EarthObservation-SDD-A.yaml) | Earth Observation Payload SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-30-CommunicationsPayload-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-30-CommunicationsPayload-SDD-A.yaml) | Communications Payload SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-40-NavigationPayload-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-40-NavigationPayload-SDD-A.yaml) | Navigation Payload SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-50-TechnologyDemonstration-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-50-TechnologyDemonstration-SDD-A.yaml) | Technology Demonstration Payload SDD  | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-60-PayloadInterfaces-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-60-PayloadInterfaces-SDD-A.yaml) | Payload Interfaces SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-70-PayloadDataProcessing-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-70-PayloadDataProcessing-SDD-A.yaml) | Payload Data Processing SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-80-AIPayloadControl-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-80-AIPayloadControl-SDD-A.yaml) | AI Payload Control SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-90-QuantumSensors-SDD-A.yaml](docs/space/ss/26/GAIA-SPACE-SS-26-90-QuantumSensors-SDD-A.yaml) | Quantum Sensors Payload SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-26-10-ScientificInstruments-DWG-A.svg](docs/space/ss/26/GAIA-SPACE-SS-26-10-ScientificInstruments-DWG-A.svg) | Scientific Instruments Drawing        | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-26-20-EarthObservation-DWG-A.svg](docs/space/ss/26/GAIA-SPACE-SS-26-20-EarthObservation-DWG-A.svg) | Earth Observation Payload Drawing     | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-26-00-PayloadCalibration-PROC-A.md](docs/space/ss/26/GAIA-SPACE-SS-26-00-PayloadCalibration-PROC-A.md) | Payload Calibration Procedure         | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-26-00-InstrumentOperations-PROC-A.md](docs/space/ss/26/GAIA-SPACE-SS-26-00-InstrumentOperations-PROC-A.md) | Instrument Operations Procedure       | Procedure                    | DRAFT    |
</details>

#### SS 27 - Command and Data Handling
<details><summary>Expand SS 27 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-27-00-Overview-OV-A.md](docs/space/ss/27/GAIA-SPACE-SS-27-00-Overview-OV-A.md) | SS 27 - C&DH Overview                   | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-27-10-OnboardComputers-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-10-OnboardComputers-SDD-A.yaml) | Onboard Computers SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-20-DataStorage-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-20-DataStorage-SDD-A.yaml)    | Data Storage System SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-30-CommandProcessing-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-30-CommandProcessing-SDD-A.yaml) | Command Processing SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-40-TelemetryProcessing-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-40-TelemetryProcessing-SDD-A.yaml) | Telemetry Processing SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-50-DataBus-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-50-DataBus-SDD-A.yaml)        | Data Bus System SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-60-FlightSoftware-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-60-FlightSoftware-SDD-A.yaml) | Flight Software SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-70-FaultManagement-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-70-FaultManagement-SDD-A.yaml) | Fault Management System SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-80-AIDataProcessing-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-80-AIDataProcessing-SDD-A.yaml) | AI Data Processing SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-90-QuantumComputing-SDD-A.yaml](docs/space/ss/27/GAIA-SPACE-SS-27-90-QuantumComputing-SDD-A.yaml) | Quantum Computing Integration SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-27-10-OnboardComputers-DWG-A.svg](docs/space/ss/27/GAIA-SPACE-SS-27-10-OnboardComputers-DWG-A.svg) | Onboard Computers Drawing             | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-27-50-DataBus-DWG-A.svg](docs/space/ss/27/GAIA-SPACE-SS-27-50-DataBus-DWG-A.svg)        | Data Bus Drawing                      | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-27-00-SoftwareUpload-PROC-A.md](docs/space/ss/27/GAIA-SPACE-SS-27-00-SoftwareUpload-PROC-A.md)  | Software Upload Procedure             | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-27-00-DataManagement-PROC-A.md](docs/space/ss/27/GAIA-SPACE-SS-27-00-DataManagement-PROC-A.md)  | Data Management Procedure             | Procedure                    | DRAFT    |
</details>

#### SS 28 - Materials and Processes
<details><summary>Expand SS 28 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-28-00-Overview-OV-A.md](docs/space/ss/28/GAIA-SPACE-SS-28-00-Overview-OV-A.md) | SS 28 - Materials & Processes Overview    | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-28-10-StructuralMaterials-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-10-StructuralMaterials-SDD-A.yaml) | Structural Materials SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-20-ThermalMaterials-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-20-ThermalMaterials-SDD-A.yaml) | Thermal Materials SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-30-ElectricalMaterials-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-30-ElectricalMaterials-SDD-A.yaml) | Electrical Materials SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-40-OpticalMaterials-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-40-OpticalMaterials-SDD-A.yaml) | Optical Materials SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-50-LubricantsAdhesives-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-50-LubricantsAdhesives-SDD-A.yaml) | Lubricants & Adhesives SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-60-RadiationHardening-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-60-RadiationHardening-SDD-A.yaml) | Radiation Hardening Materials SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-70-OutgassingControl-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-70-OutgassingControl-SDD-A.yaml) | Outgassing Control Materials SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-80-AdvancedComposites-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-80-AdvancedComposites-SDD-A.yaml) | Advanced Composites SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-90-SelfHealingMaterials-SDD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-90-SelfHealingMaterials-SDD-A.yaml) | Self-Healing Materials SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-28-00-MaterialsSelection-PROC-A.md](docs/space/ss/28/GAIA-SPACE-SS-28-00-MaterialsSelection-PROC-A.md) | Materials Selection Procedure         | Procedure                    | DRAFT    |
| [GAIA-SPACE-SS-28-00-RadiationAnalysis-RAD-A.yaml](docs/space/ss/28/GAIA-SPACE-SS-28-00-RadiationAnalysis-RAD-A.yaml) | Radiation Analysis Data               | Radiation Analysis           | DRAFT    |
</details>

#### SS 29 - Mechanisms
<details><summary>Expand SS 29 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SS-29-00-Overview-OV-A.md](docs/space/ss/29/GAIA-SPACE-SS-29-00-Overview-OV-A.md) | SS 29 - Mechanisms Overview             | Overview                     | DRAFT    |
| [GAIA-SPACE-SS-29-10-DeploymentMechanisms-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-10-DeploymentMechanisms-SDD-A.yaml) | Deployment Mechanisms SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-20-ActuationSystems-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-20-ActuationSystems-SDD-A.yaml) | Actuation Systems SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-30-PointingMechanisms-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-30-PointingMechanisms-SDD-A.yaml) | Pointing Mechanisms SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-40-ReleaseMechanisms-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-40-ReleaseMechanisms-SDD-A.yaml) | Release Mechanisms SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-50-DockingMechanisms-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-50-DockingMechanisms-SDD-A.yaml) | Docking Mechanisms SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-60-RoboticSystems-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-60-RoboticSystems-SDD-A.yaml) | Robotic Systems SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-70-SampleCollection-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-70-SampleCollection-SDD-A.yaml) | Sample Collection Mechanisms SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-80-AIMechanismControl-SDD-A.yaml](docs/space/ss/29/GAIA-SPACE-SS-29-80-AIMechanismControl-SDD-A.yaml) | AI Mechanism Control SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SS-29-10-DeploymentMechanisms-DWG-A.svg](docs/space/ss/29/GAIA-SPACE-SS-29-10-DeploymentMechanisms-DWG-A.svg) | Deployment Mechanisms Drawing       | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-29-60-RoboticSystems-DWG-A.svg](docs/space/ss/29/GAIA-SPACE-SS-29-60-RoboticSystems-DWG-A.svg) | Robotic Systems Drawing               | Drawing                      | DRAFT    |
| [GAIA-SPACE-SS-29-00-MechanismTesting-PROC-A.md](docs/space/ss/29/GAIA-SPACE-SS-29-00-MechanismTesting-PROC-A.md) | Mechanism Testing Procedure           | Procedure                    | DRAFT    |
</details>

</details>

---

### Part III: Mission Operations (MO 00-99)

<details>
<summary><strong>Expand Part III: Mission Operations (MO 00-99) Outline</strong></summary>

#### MO 10 - Mission Planning
<details><summary>Expand MO 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-MO-10-00-Overview-OV-A.md](docs/space/mo/10/GAIA-SPACE-MO-10-00-Overview-OV-A.md) | MO 10 - Mission Planning Overview         | Overview                     | DRAFT    |
| [GAIA-SPACE-MO-10-10-MissionDesign-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-10-MissionDesign-SDD-A.yaml)  | Mission Design SDD                    | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-20-TrajectoryPlanning-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-20-TrajectoryPlanning-SDD-A.yaml) | Trajectory Planning SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-30-LaunchOperations-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-30-LaunchOperations-SDD-A.yaml) | Launch Operations Planning SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-40-OrbitInsertion-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-40-OrbitInsertion-SDD-A.yaml) | Orbit Insertion Planning SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-50-MissionPhases-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-50-MissionPhases-SDD-A.yaml)  | Mission Phases Planning SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-60-EndOfLifeOperations-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-60-EndOfLifeOperations-SDD-A.yaml) | End-Of-Life Operations Planning SDD   | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-70-AIMissionPlanner-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-70-AIMissionPlanner-SDD-A.yaml) | AI Mission Planner SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-80-QuantumTrajectoryOptimizer-SDD-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-80-QuantumTrajectoryOptimizer-SDD-A.yaml) | Quantum Trajectory Optimizer SDD    | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-10-00-MissionPlan-PLAN-A.md](docs/space/mo/10/GAIA-SPACE-MO-10-00-MissionPlan-PLAN-A.md)     | Mission Plan Document                 | Plan                         | DRAFT    |
| [GAIA-SPACE-MO-10-00-TrajectoryAnalysis-ORB-A.yaml](docs/space/mo/10/GAIA-SPACE-MO-10-00-TrajectoryAnalysis-ORB-A.yaml) | Trajectory Analysis Data              | Orbital Analysis             | DRAFT    |
</details>

#### MO 20 - Ground Systems
<details><summary>Expand MO 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-MO-20-00-Overview-OV-A.md](docs/space/mo/20/GAIA-SPACE-MO-20-00-Overview-OV-A.md) | MO 20 - Ground Systems Overview         | Overview                     | DRAFT    |
| [GAIA-SPACE-MO-20-10-GroundStations-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-10-GroundStations-SDD-A.yaml) | Ground Stations SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-20-MissionControlCenter-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-20-MissionControlCenter-SDD-A.yaml) | Mission Control Center SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-30-DataProcessingCenter-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-30-DataProcessingCenter-SDD-A.yaml) | Data Processing Center SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-40-SimulationSystems-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-40-SimulationSystems-SDD-A.yaml) | Simulation Systems SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-50-TestingFacilities-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-50-TestingFacilities-SDD-A.yaml) | Testing Facilities SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-60-GroundNetworks-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-60-GroundNetworks-SDD-A.yaml) | Ground Networks SDD                   | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-70-AIGroundOperations-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-70-AIGroundOperations-SDD-A.yaml) | AI Ground Operations SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-80-QuantumGroundSystems-SDD-A.yaml](docs/space/mo/20/GAIA-SPACE-MO-20-80-QuantumGroundSystems-SDD-A.yaml) | Quantum Ground Systems SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-20-10-GroundStations-DWG-A.svg](docs/space/mo/20/GAIA-SPACE-MO-20-10-GroundStations-DWG-A.svg) | Ground Stations Drawing               | Drawing                      | DRAFT    |
| [GAIA-SPACE-MO-20-20-MissionControlCenter-DWG-A.svg](docs/space/mo/20/GAIA-SPACE-MO-20-20-MissionControlCenter-DWG-A.svg) | Mission Control Center Drawing        | Drawing                      | DRAFT    |
| [GAIA-SPACE-MO-20-00-GroundSystemsOps-PROC-A.md](docs/space/mo/20/GAIA-SPACE-MO-20-00-GroundSystemsOps-PROC-A.md) | Ground Systems Operations Procedure   | Procedure                    | DRAFT    |
</details>

#### MO 30 - Flight Dynamics
<details><summary>Expand MO 30 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-MO-30-00-Overview-OV-A.md](docs/space/mo/30/GAIA-SPACE-MO-30-00-Overview-OV-A.md) | MO 30 - Flight Dynamics Overview        | Overview                     | DRAFT    |
| [GAIA-SPACE-MO-30-10-OrbitDetermination-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-10-OrbitDetermination-SDD-A.yaml) | Orbit Determination System SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-20-ManeuverPlanning-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-20-ManeuverPlanning-SDD-A.yaml) | Maneuver Planning System SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-30-AttitudeDynamics-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-30-AttitudeDynamics-SDD-A.yaml) | Attitude Dynamics System SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-40-ProximityOperations-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-40-ProximityOperations-SDD-A.yaml) | Proximity Operations SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-50-EntryDescentLanding-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-50-EntryDescentLanding-SDD-A.yaml) | Entry, Descent & Landing (EDL) SDD    | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-60-FormationFlying-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-60-FormationFlying-SDD-A.yaml) | Formation Flying System SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-70-AIFlightDynamics-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-70-AIFlightDynamics-SDD-A.yaml) | AI Flight Dynamics SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-80-QuantumOrbitPrediction-SDD-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-80-QuantumOrbitPrediction-SDD-A.yaml) | Quantum Orbit Prediction SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-30-00-OrbitDeterminationProc-PROC-A.md](docs/space/mo/30/GAIA-SPACE-MO-30-00-OrbitDeterminationProc-PROC-A.md) | Orbit Determination Procedure       | Procedure                    | DRAFT    |
| [GAIA-SPACE-MO-30-00-ManeuverPlanning-PROC-A.md](docs/space/mo/30/GAIA-SPACE-MO-30-00-ManeuverPlanning-PROC-A.md) | Maneuver Planning Procedure           | Procedure                    | DRAFT    |
| [GAIA-SPACE-MO-30-00-OrbitAnalysis-ORB-A.yaml](docs/space/mo/30/GAIA-SPACE-MO-30-00-OrbitAnalysis-ORB-A.yaml)  | Orbit Analysis Data                   | Orbital Analysis             | DRAFT    |
</details>

#### MO 40 - Telemetry, Tracking, and Command
<details><summary>Expand MO 40 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-MO-40-00-Overview-OV-A.md](docs/space/mo/40/GAIA-SPACE-MO-40-00-Overview-OV-A.md) | MO 40 - TT&C Overview                   | Overview                     | DRAFT    |
| [GAIA-SPACE-MO-40-10-TelemetryProcessing-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-10-TelemetryProcessing-SDD-A.yaml) | Telemetry Processing System SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-20-CommandGeneration-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-20-CommandGeneration-SDD-A.yaml) | Command Generation System SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-30-TrackingData-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-30-TrackingData-SDD-A.yaml)    | Tracking Data System SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-40-DataArchiving-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-40-DataArchiving-SDD-A.yaml)   | TT&C Data Archiving SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-50-RealTimeOperations-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-50-RealTimeOperations-SDD-A.yaml) | Real-Time Operations SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-60-RemoteTerminals-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-60-RemoteTerminals-SDD-A.yaml) | Remote Terminals SDD                  | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-70-AITelemetryAnalysis-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-70-AITelemetryAnalysis-SDD-A.yaml) | AI Telemetry Analysis SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-80-QuantumDataSecurity-SDD-A.yaml](docs/space/mo/40/GAIA-SPACE-MO-40-80-QuantumDataSecurity-SDD-A.yaml) | Quantum Data Security for TT&C SDD  | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-40-10-TelemetryProcessing-DWG-A.svg](docs/space/mo/40/GAIA-SPACE-MO-40-10-TelemetryProcessing-DWG-A.svg) | Telemetry Processing Flow Drawing     | Drawing                      | DRAFT    |
| [GAIA-SPACE-MO-40-20-CommandGeneration-DWG-A.svg](docs/space/mo/40/GAIA-SPACE-MO-40-20-CommandGeneration-DWG-A.svg) | Command Generation Flow Drawing       | Drawing                      | DRAFT    |
| [GAIA-SPACE-MO-40-00-TelemetryMonitoring-PROC-A.md](docs/space/mo/40/GAIA-SPACE-MO-40-00-TelemetryMonitoring-PROC-A.md) | Telemetry Monitoring Procedure        | Procedure                    | DRAFT    |
| [GAIA-SPACE-MO-40-00-CommandProcedures-PROC-A.md](docs/space/mo/40/GAIA-SPACE-MO-40-00-CommandProcedures-PROC-A.md) | Command Procedures                  | Procedure                    | DRAFT    |
</details>

#### MO 50 - Mission Data Management
<details><summary>Expand MO 50 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-MO-50-00-Overview-OV-A.md](docs/space/mo/50/GAIA-SPACE-MO-50-00-Overview-OV-A.md) | MO 50 - Mission Data Management Overview  | Overview                     | DRAFT    |
| [GAIA-SPACE-MO-50-10-DataProcessing-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-10-DataProcessing-SDD-A.yaml) | Mission Data Processing SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-20-DataDistribution-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-20-DataDistribution-SDD-A.yaml) | Mission Data Distribution SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-30-DataArchiving-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-30-DataArchiving-SDD-A.yaml)   | Mission Data Archiving SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-40-DataQuality-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-40-DataQuality-SDD-A.yaml)    | Mission Data Quality SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-50-DataSecurity-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-50-DataSecurity-SDD-A.yaml)   | Mission Data Security SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-60-DataVisualization-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-60-DataVisualization-SDD-A.yaml) | Mission Data Visualization SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-70-AIDataAnalytics-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-70-AIDataAnalytics-SDD-A.yaml) | AI Mission Data Analytics SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-80-QuantumDataProcessing-SDD-A.yaml](docs/space/mo/50/GAIA-SPACE-MO-50-80-QuantumDataProcessing-SDD-A.yaml) | Quantum Data Processing SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-MO-50-10-DataProcessing-DWG-A.svg](docs/space/mo/50/GAIA-SPACE-MO-50-10-DataProcessing-DWG-A.svg)  | Mission Data Processing Flow Drawing  | Drawing                      | DRAFT    |
| [GAIA-SPACE-MO-50-30-DataArchiving-DWG-A.svg](docs/space/mo/50/GAIA-SPACE-MO-50-30-DataArchiving-DWG-A.svg)   | Mission Data Archiving Architecture   | Drawing                      | DRAFT    |
| [GAIA-SPACE-MO-50-00-DataManagementPlan-PLAN-A.md](docs/space/mo/50/GAIA-SPACE-MO-50-00-DataManagementPlan-PLAN-A.md) | Mission Data Management Plan          | Plan                         | DRAFT    |
| [GAIA-SPACE-MO-50-00-DataSecurityProcedures-PROC-A.md](docs/space/mo/50/GAIA-SPACE-MO-50-00-DataSecurityProcedures-PROC-A.md) | Mission Data Security Procedures      | Procedure                    | DRAFT    |
</details>

</details>

---

### Part IV: Space Environment (SE 00-99)

<details>
<summary><strong>Expand Part IV: Space Environment (SE 00-99) Outline</strong></summary>

#### SE 10 - Space Weather
<details><summary>Expand SE 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SE-10-00-Overview-OV-A.md](docs/space/se/10/GAIA-SPACE-SE-10-00-Overview-OV-A.md) | SE 10 - Space Weather Overview            | Overview                     | DRAFT    |
| [GAIA-SPACE-SE-10-10-SolarActivity-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-10-SolarActivity-SDD-A.yaml)  | Solar Activity Models SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-20-GeomagneticStorms-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-20-GeomagneticStorms-SDD-A.yaml) | Geomagnetic Storm Models SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-30-CosmicRadiation-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-30-CosmicRadiation-SDD-A.yaml) | Cosmic Radiation Environment SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-40-SpaceWeatherForecasting-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-40-SpaceWeatherForecasting-SDD-A.yaml) | Space Weather Forecasting SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-50-RadiationEffects-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-50-RadiationEffects-SDD-A.yaml) | Radiation Effects Analysis SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-60-SpaceWeatherMonitoring-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-60-SpaceWeatherMonitoring-SDD-A.yaml) | Space Weather Monitoring Systems SDD  | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-70-AISpaceWeatherPrediction-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-70-AISpaceWeatherPrediction-SDD-A.yaml) | AI Space Weather Prediction SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-80-QuantumRadiationDetection-SDD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-80-QuantumRadiationDetection-SDD-A.yaml) | Quantum Radiation Detection SDD   | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-10-00-RadiationAnalysis-RAD-A.yaml](docs/space/se/10/GAIA-SPACE-SE-10-00-RadiationAnalysis-RAD-A.yaml) | Radiation Analysis Data               | Radiation Analysis           | DRAFT    |
| [GAIA-SPACE-SE-10-00-SpaceWeatherResponse-PROC-A.md](docs/space/se/10/GAIA-SPACE-SE-10-00-SpaceWeatherResponse-PROC-A.md) | Space Weather Response Procedure      | Procedure                    | DRAFT    |
</details>

#### SE 20 - Orbital Environment
<details><summary>Expand SE 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SE-20-00-Overview-OV-A.md](docs/space/se/20/GAIA-SPACE-SE-20-00-Overview-OV-A.md) | SE 20 - Orbital Environment Overview      | Overview                     | DRAFT    |
| [GAIA-SPACE-SE-20-10-OrbitalDebris-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-10-OrbitalDebris-SDD-A.yaml)  | Orbital Debris Environment SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-20-MicrometeoroidEnvironment-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-20-MicrometeoroidEnvironment-SDD-A.yaml) | Micrometeoroid Environment SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-30-CollisionAvoidance-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-30-CollisionAvoidance-SDD-A.yaml) | Collision Avoidance System SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-40-DebrisTracking-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-40-DebrisTracking-SDD-A.yaml) | Debris Tracking System SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-50-DebrisMitigation-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-50-DebrisMitigation-SDD-A.yaml) | Debris Mitigation Strategies SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-60-SpaceSituationalAwareness-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-60-SpaceSituationalAwareness-SDD-A.yaml) | Space Situational Awareness (SSA) SDD | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-70-AICollisionPrediction-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-70-AICollisionPrediction-SDD-A.yaml) | AI Collision Prediction SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-80-QuantumDebrisDetection-SDD-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-80-QuantumDebrisDetection-SDD-A.yaml) | Quantum Debris Detection SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-20-00-DebrisAnalysis-ORB-A.yaml](docs/space/se/20/GAIA-SPACE-SE-20-00-DebrisAnalysis-ORB-A.yaml) | Debris Environment Analysis Data      | Orbital Analysis             | DRAFT    |
| [GAIA-SPACE-SE-20-00-CollisionAvoidanceProc-PROC-A.md](docs/space/se/20/GAIA-SPACE-SE-20-00-CollisionAvoidanceProc-PROC-A.md) | Collision Avoidance Procedure         | Procedure                    | DRAFT    |
</details>

#### SE 30 - Planetary Environments
<details><summary>Expand SE 30 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SE-30-00-Overview-OV-A.md](docs/space/se/30/GAIA-SPACE-SE-30-00-Overview-OV-A.md) | SE 30 - Planetary Environments Overview   | Overview                     | DRAFT    |
| [GAIA-SPACE-SE-30-10-LunarEnvironment-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-10-LunarEnvironment-SDD-A.yaml) | Lunar Environment Model SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-20-MartianEnvironment-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-20-MartianEnvironment-SDD-A.yaml) | Martian Environment Model SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-30-VenusianEnvironment-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-30-VenusianEnvironment-SDD-A.yaml) | Venusian Environment Model SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-40-GasGiantEnvironments-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-40-GasGiantEnvironments-SDD-A.yaml) | Gas Giant Environments Model SDD    | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-50-AsteroidEnvironments-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-50-AsteroidEnvironments-SDD-A.yaml) | Asteroid Environments Model SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-60-CometaryEnvironments-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-60-CometaryEnvironments-SDD-A.yaml) | Cometary Environments Model SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-70-AIPlanetaryModeling-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-70-AIPlanetaryModeling-SDD-A.yaml) | AI Planetary Environment Modeling SDD | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-80-QuantumEnvironmentSensing-SDD-A.yaml](docs/space/se/30/GAIA-SPACE-SE-30-80-QuantumEnvironmentSensing-SDD-A.yaml) | Quantum Environment Sensing SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SE-30-00-PlanetaryProtection-PROC-A.md](docs/space/se/30/GAIA-SPACE-SE-30-00-PlanetaryProtection-PROC-A.md) | Planetary Protection Procedure        | Procedure                    | DRAFT    |
| [GAIA-SPACE-SE-30-00-SurfaceOperations-PROC-A.md](docs/space/se/30/GAIA-SPACE-SE-30-00-SurfaceOperations-PROC-A.md) | Planetary Surface Operations Proc     | Procedure                    | DRAFT    |
</details>

</details>

---

### Part V: Launch Systems (LS 00-99)

<details>
<summary><strong>Expand Part V: Launch Systems (LS 00-99) Outline</strong></summary>

#### LS 10 - Launch Vehicles
<details><summary>Expand LS 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-LS-10-00-Overview-OV-A.md](docs/space/ls/10/GAIA-SPACE-LS-10-00-Overview-OV-A.md) | LS 10 - Launch Vehicles Overview          | Overview                     | DRAFT    |
| [GAIA-SPACE-LS-10-10-LaunchVehicleArchitecture-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-10-LaunchVehicleArchitecture-SDD-A.yaml) | Launch Vehicle Architecture SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-20-PropulsionSystems-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-20-PropulsionSystems-SDD-A.yaml) | LV Propulsion Systems SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-30-AvionicsSystems-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-30-AvionicsSystems-SDD-A.yaml) | LV Avionics Systems SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-40-StructuralSystems-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-40-StructuralSystems-SDD-A.yaml) | LV Structural Systems SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-50-StagingSystems-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-50-StagingSystems-SDD-A.yaml) | LV Staging Systems SDD                | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-60-FairingDesign-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-60-FairingDesign-SDD-A.yaml)  | LV Fairing Design SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-70-AILaunchOptimization-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-70-AILaunchOptimization-SDD-A.yaml) | AI Launch Optimization SDD          | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-80-ReusableLaunchSystems-SDD-A.yaml](docs/space/ls/10/GAIA-SPACE-LS-10-80-ReusableLaunchSystems-SDD-A.yaml) | Reusable Launch Systems SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-10-10-LaunchVehicleArchitecture-DWG-A.svg](docs/space/ls/10/GAIA-SPACE-LS-10-10-LaunchVehicleArchitecture-DWG-A.svg) | Launch Vehicle Architecture Drawing | Drawing                      | DRAFT    |
| [GAIA-SPACE-LS-10-20-PropulsionSystems-DWG-A.svg](docs/space/ls/10/GAIA-SPACE-LS-10-20-PropulsionSystems-DWG-A.svg) | LV Propulsion Systems Drawing         | Drawing                      | DRAFT    |
| [GAIA-SPACE-LS-10-00-LaunchVehiclePrep-PROC-A.md](docs/space/ls/10/GAIA-SPACE-LS-10-00-LaunchVehiclePrep-PROC-A.md) | Launch Vehicle Preparation Proc       | Procedure                    | DRAFT    |
| [GAIA-SPACE-LS-10-00-LaunchSequence-PROC-A.md](docs/space/ls/10/GAIA-SPACE-LS-10-00-LaunchSequence-PROC-A.md)  | Launch Sequence Procedure             | Procedure                    | DRAFT    |
</details>

#### LS 20 - Launch Operations
<details><summary>Expand LS 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-LS-20-00-Overview-OV-A.md](docs/space/ls/20/GAIA-SPACE-LS-20-00-Overview-OV-A.md) | LS 20 - Launch Operations Overview        | Overview                     | DRAFT    |
| [GAIA-SPACE-LS-20-10-LaunchSites-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-10-LaunchSites-SDD-A.yaml)      | Launch Sites SDD                      | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-20-LaunchProcessing-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-20-LaunchProcessing-SDD-A.yaml) | Launch Processing SDD                 | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-30-LaunchControl-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-30-LaunchControl-SDD-A.yaml)    | Launch Control System SDD             | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-40-RangeOperations-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-40-RangeOperations-SDD-A.yaml)  | Range Operations SDD                  | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-50-WeatherMonitoring-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-50-WeatherMonitoring-SDD-A.yaml) | Launch Weather Monitoring SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-60-LaunchSafety-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-60-LaunchSafety-SDD-A.yaml)     | Launch Safety System SDD              | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-70-AILaunchDecisionSupport-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-70-AILaunchDecisionSupport-SDD-A.yaml) | AI Launch Decision Support SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-80-QuantumLaunchSecurity-SDD-A.yaml](docs/space/ls/20/GAIA-SPACE-LS-20-80-QuantumLaunchSecurity-SDD-A.yaml) | Quantum Launch Security SDD         | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-20-10-LaunchSites-DWG-A.svg](docs/space/ls/20/GAIA-SPACE-LS-20-10-LaunchSites-DWG-A.svg)      | Launch Sites Drawing                  | Drawing                      | DRAFT    |
| [GAIA-SPACE-LS-20-30-LaunchControl-DWG-A.svg](docs/space/ls/20/GAIA-SPACE-LS-20-30-LaunchControl-DWG-A.svg)    | Launch Control Drawing                | Drawing                      | DRAFT    |
| [GAIA-SPACE-LS-20-00-LaunchCountdown-PROC-A.md](docs/space/ls/20/GAIA-SPACE-LS-20-00-LaunchCountdown-PROC-A.md) | Launch Countdown Procedure            | Procedure                    | DRAFT    |
| [GAIA-SPACE-LS-20-00-LaunchAbort-PROC-A.md](docs/space/ls/20/GAIA-SPACE-LS-20-00-LaunchAbort-PROC-A.md)     | Launch Abort Procedure                | Procedure                    | DRAFT    |
</details>

#### LS 30 - Spacecraft Integration
<details><summary>Expand LS 30 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-LS-30-00-Overview-OV-A.md](docs/space/ls/30/GAIA-SPACE-LS-30-00-Overview-OV-A.md) | LS 30 - Spacecraft Integration Overview   | Overview                     | DRAFT    |
| [GAIA-SPACE-LS-30-10-PayloadIntegration-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-10-PayloadIntegration-SDD-A.yaml) | Payload Integration SDD               | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-20-LaunchVehicleIntegration-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-20-LaunchVehicleIntegration-SDD-A.yaml) | Launch Vehicle Integration SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-30-InterfaceVerification-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-30-InterfaceVerification-SDD-A.yaml) | Interface Verification SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-40-SystemsTesting-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-40-SystemsTesting-SDD-A.yaml)   | Integration Systems Testing SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-50-FinalCheckout-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-50-FinalCheckout-SDD-A.yaml)    | Final Checkout SDD                    | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-60-TransportToLaunchSite-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-60-TransportToLaunchSite-SDD-A.yaml) | Transport to Launch Site SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-70-AIIntegrationAssistant-SDD-A.yaml](docs/space/ls/30/GAIA-SPACE-LS-30-70-AIIntegrationAssistant-SDD-A.yaml) | AI Integration Assistant SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-LS-30-10-PayloadIntegration-DWG-A.svg](docs/space/ls/30/GAIA-SPACE-LS-30-10-PayloadIntegration-DWG-A.svg) | Payload Integration Drawing           | Drawing                      | DRAFT    |
| [GAIA-SPACE-LS-30-20-LaunchVehicleIntegration-DWG-A.svg](docs/space/ls/30/GAIA-SPACE-LS-30-20-LaunchVehicleIntegration-DWG-A.svg) | Launch Vehicle Integration Drawing  | Drawing                      | DRAFT    |
| [GAIA-SPACE-LS-30-00-IntegrationProcedures-PROC-A.md](docs/space/ls/30/GAIA-SPACE-LS-30-00-IntegrationProcedures-PROC-A.md) | Integration Procedures                | Procedure                    | DRAFT    |
| [GAIA-SPACE-LS-30-00-TestingProcedures-PROC-A.md](docs/space/ls/30/GAIA-SPACE-LS-30-00-TestingProcedures-PROC-A.md) | Integration Testing Procedures        | Procedure                    | DRAFT    |
</details>

</details>

---

### Part VI: Space Project Management (PM 00-99)
*(Note: This should ideally be unified with the Common PM Part)*

<details>
<summary><strong>Expand Part VI: Space Project Management (PM 00-99) Outline</strong></summary>

#### PM 10 - Project Planning
<details><summary>Expand PM 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-PM-10-00-Overview-OV-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-00-Overview-OV-A.md) | Space PM 10 - Project Planning Overview   | Overview                     | DRAFT    |
| [GAIA-SPACE-PM-10-10-ProjectCharter-PLAN-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-10-ProjectCharter-PLAN-A.md) | Space Project Charter                   | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-10-20-WBS-WBS-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-20-WBS-WBS-A.md)       | Space Project WBS                     | Work Breakdown Structure     | DRAFT    |
| [GAIA-SPACE-PM-10-30-Schedules-PLAN-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-30-Schedules-PLAN-A.md)    | Space Project Schedules               | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-10-40-Resources-PLAN-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-40-Resources-PLAN-A.md)    | Space Project Resource Plan           | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-10-50-AIProjectPlanning-SDD-A.yaml](docs/space/pm/10/GAIA-SPACE-PM-10-50-AIProjectPlanning-SDD-A.yaml) | AI Project Planning (Space) SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-PM-10-60-RiskManagement-PLAN-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-60-RiskManagement-PLAN-A.md) | Space Risk Management Plan            | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-10-70-StakeholderManagement-PLAN-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-70-StakeholderManagement-PLAN-A.md) | Space Stakeholder Management Plan   | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-10-00-ProjectPlan-PLAN-A.md](docs/space/pm/10/GAIA-SPACE-PM-10-00-ProjectPlan-PLAN-A.md)     | Space Project Management Plan         | Plan                         | DRAFT    |
</details>

#### PM 20 - Configuration Management
<details><summary>Expand PM 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-PM-20-00-Overview-OV-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-00-Overview-OV-A.md) | Space PM 20 - Config Management Overview  | Overview                     | DRAFT    |
| [GAIA-SPACE-PM-20-10-CMPlan-PLAN-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-10-CMPlan-PLAN-A.md)       | Space Configuration Management Plan     | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-20-20-ChangeControl-PROC-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-20-ChangeControl-PROC-A.md) | Space Change Control Procedure          | Procedure                    | DRAFT    |
| [GAIA-SPACE-PM-20-30-Baselines-BASE-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-30-Baselines-BASE-A.md)    | Space Configuration Baselines         | Baseline Document            | DRAFT    |
| [GAIA-SPACE-PM-20-40-VersionControl-PROC-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-40-VersionControl-PROC-A.md) | Space Version Control Procedure         | Procedure                    | DRAFT    |
| [GAIA-SPACE-PM-20-50-AIConfigOptimizer-SDD-A.yaml](docs/space/pm/20/GAIA-SPACE-PM-20-50-AIConfigOptimizer-SDD-A.yaml) | AI Configuration Optimizer (Space) SDD | System Design Description    | DRAFT    |
| [GAIA-SPACE-PM-20-60-DocumentationControl-PROC-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-60-DocumentationControl-PROC-A.md) | Space Documentation Control Procedure | Procedure                    | DRAFT    |
| [GAIA-SPACE-PM-20-00-CMProcedures-PROC-A.md](docs/space/pm/20/GAIA-SPACE-PM-20-00-CMProcedures-PROC-A.md)    | Space CM Procedures                   | Procedure                    | DRAFT    |
</details>

#### PM 30 - Quality Assurance
<details><summary>Expand PM 30 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-PM-30-00-Overview-OV-A.md](docs/space/pm/30/GAIA-SPACE-PM-30-00-Overview-OV-A.md) | Space PM 30 - Quality Assurance Overview  | Overview                     | DRAFT    |
| [GAIA-SPACE-PM-30-10-QAPlan-PLAN-A.md](docs/space/pm/30/GAIA-SPACE-PM-30-10-QAPlan-PLAN-A.md)       | Space Quality Assurance Plan            | Plan                         | DRAFT    |
| [GAIA-SPACE-PM-30-20-QAProcesses-PROC-A.md](docs/space/pm/30/GAIA-SPACE-PM-30-20-QAProcesses-PROC-A.md) | Space QA Processes                    | Procedure                    | DRAFT    |
| [GAIA-SPACE-PM-30-30-QAStandards-SPEC-A.yaml](docs/space/pm/30/GAIA-SPACE-PM-30-30-QAStandards-SPEC-A.yaml) | Space QA Standards (ECSS)             | Specification                | DRAFT    |
| [GAIA-SPACE-PM-30-40-QAMetrics-LIST-A.csv](docs/space/pm/30/GAIA-SPACE-PM-30-40-QAMetrics-LIST-A.csv)   | Space QA Metrics                      | List                         | DRAFT    |
| [GAIA-SPACE-PM-30-50-AIQualityMonitor-SDD-A.yaml](docs/space/pm/30/GAIA-SPACE-PM-30-50-AIQualityMonitor-SDD-A.yaml) | AI Quality Monitor (Space) SDD        | System Design Description    | DRAFT    |
| [GAIA-SPACE-PM-30-60-TestingVerification-PROC-A.md](docs/space/pm/30/GAIA-SPACE-PM-30-60-TestingVerification-PROC-A.md) | Space Testing & Verification Proc     | Procedure                    | DRAFT    |
| [GAIA-SPACE-PM-30-70-QualityReporting-PROC-A.md](docs/space/pm/30/GAIA-SPACE-PM-30-70-QualityReporting-PROC-A.md) | Space Quality Reporting Procedure     | Procedure                    | DRAFT    |
| [GAIA-SPACE-PM-30-00-QAProcedures-PROC-A.md](docs/space/pm/30/GAIA-SPACE-PM-30-00-QAProcedures-PROC-A.md)    | Space QA Procedures                   | Procedure                    | DRAFT    |
</details>

#### PM 40 - Risk Management
<details><summary>Expand PM 40 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-PM-40-00-Overview-OV-A.md](docs/space/pm/40/GAIA-SPACE-PM-40-00-Overview-OV-A.md) | Space PM 40 - Risk Management Overview    | Overview                     | DRAFT    |
| *(... Documents similar to AToC PM 40 ...)* | | | |
</details>

#### PM 50 - Governance & Compliance
<details><summary>Expand PM 50 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-PM-50-00-Overview-OV-A.md](docs/space/pm/50/GAIA-SPACE-PM-50-00-Overview-OV-A.md) | Space PM 50 - Governance & Compliance Ov. | Overview                     | DRAFT    |
| *(... Documents similar to AToC PM 50, referencing space regulations ...)* | | | |
</details>

</details>

---

### Part VII: Space Research Systems (SR 00-99)

<details>
<summary><strong>Expand Part VII: Space Research Systems (SR 00-99) Outline</strong></summary>

#### SR 10 - Experimental Systems
<details><summary>Expand SR 10 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SR-10-00-Overview-OV-A.md](docs/space/sr/10/GAIA-SPACE-SR-10-00-Overview-OV-A.md) | SR 10 - Experimental Systems Overview     | Overview                     | DRAFT    |
| [GAIA-SPACE-SR-10-10-TestBed-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-10-TestBed-SDD-A.yaml)       | Space Test Bed SDD                    | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-20-PrototypeSystems-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-20-PrototypeSystems-SDD-A.yaml) | Space Prototype Systems SDD           | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-30-SimulationEnv-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-30-SimulationEnv-SDD-A.yaml)  | Space Simulation Environment SDD      | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-40-AIExperiments-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-40-AIExperiments-SDD-A.yaml)  | AI Experiments (Space) SDD            | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-50-QuantumExperiments-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-50-QuantumExperiments-SDD-A.yaml) | Quantum Experiments (Space) SDD       | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-60-BioExperiments-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-60-BioExperiments-SDD-A.yaml)   | Biological Experiments (Space) SDD    | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-70-MaterialsExperiments-SDD-A.yaml](docs/space/sr/10/GAIA-SPACE-SR-10-70-MaterialsExperiments-SDD-A.yaml) | Materials Experiments (Space) SDD     | System Design Description    | DRAFT    |
| [GAIA-SPACE-SR-10-10-TestBed-DWG-A.svg](docs/space/sr/10/GAIA-SPACE-SR-10-10-TestBed-DWG-A.svg)       | Space Test Bed Drawing                | Drawing                      | DRAFT    |
| [GAIA-SPACE-SR-10-30-SimulationEnv-DWG-A.svg](docs/space/sr/10/GAIA-SPACE-SR-10-30-SimulationEnv-DWG-A.svg)  | Space Simulation Environment Drawing  | Drawing                      | DRAFT    |
| [GAIA-SPACE-SR-10-00-ExperimentProcedures-PROC-A.md](docs/space/sr/10/GAIA-SPACE-SR-10-00-ExperimentProcedures-PROC-A.md) | Experiment Procedures (Space)         | Procedure                    | DRAFT    |
| [GAIA-SPACE-SR-10-00-SimulationSetup-PROC-A.md](docs/space/sr/10/GAIA-SPACE-SR-10-00-SimulationSetup-PROC-A.md) | Simulation Setup Procedure (Space)    | Procedure                    | DRAFT    |
</details>

#### SR 20 - Advanced Concepts
<details><summary>Expand SR 20 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SR-20-00-Overview-OV-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-00-Overview-OV-A.md) | SR 20 - Advanced Concepts Overview        | Overview                     | DRAFT    |
| [GAIA-SPACE-SR-20-10-FuturePropulsion-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-10-FuturePropulsion-CONOPS-A.md) | Future Propulsion Concepts CONOPS     | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-20-AutonomousSpacecraft-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-20-AutonomousSpacecraft-CONOPS-A.md) | Autonomous Spacecraft CONOPS        | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-30-SpaceHabitats-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-30-SpaceHabitats-CONOPS-A.md) | Space Habitats Concepts CONOPS        | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-40-AGI-Space-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-40-AGI-Space-CONOPS-A.md)     | AGI in Space CONOPS                 | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-50-QuantumSpaceTech-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-50-QuantumSpaceTech-CONOPS-A.md) | Quantum Space Technology CONOPS       | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-60-SpaceMining-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-60-SpaceMining-CONOPS-A.md)    | Space Mining Concepts CONOPS          | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-70-InterstellarConcepts-CONOPS-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-70-InterstellarConcepts-CONOPS-A.md) | Interstellar Concepts CONOPS        | Concept of Operations        | DRAFT    |
| [GAIA-SPACE-SR-20-00-ConceptDevelopment-PROC-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-00-ConceptDevelopment-PROC-A.md) | Concept Development Procedure         | Procedure                    | DRAFT    |
| [GAIA-SPACE-SR-20-00-FeasibilityStudies-RES-A.md](docs/space/sr/20/GAIA-SPACE-SR-20-00-FeasibilityStudies-RES-A.md) | Advanced Concepts Feasibility Studies | Research Document            | DRAFT    |
</details>

#### SR 30 - Research Partnerships
<details><summary>Expand SR 30 Details</summary>

| Document ID                         | Title                                       | Type                         | Status   |
| :---------------------------------- | :------------------------------------------ | :--------------------------- | :------- |
| [GAIA-SPACE-SR-30-00-Overview-OV-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-00-Overview-OV-A.md) | SR 30 - Research Partnerships Overview    | Overview                     | DRAFT    |
| [GAIA-SPACE-SR-30-10-AcademicPartners-ADMIN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-10-AcademicPartners-ADMIN-A.md) | Academic Partnerships List            | Administrative Document    | DRAFT    |
| [GAIA-SPACE-SR-30-20-IndustryPartners-ADMIN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-20-IndustryPartners-ADMIN-A.md) | Industry Partnerships List            | Administrative Document    | DRAFT    |
| [GAIA-SPACE-SR-30-30-GovernmentPartners-ADMIN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-30-GovernmentPartners-ADMIN-A.md) | Government Partnerships List          | Administrative Document    | DRAFT    |
| [GAIA-SPACE-SR-30-40-ResearchCollaborations-PLAN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-40-ResearchCollaborations-PLAN-A.md) | Research Collaborations Plan        | Plan                         | DRAFT    |
| [GAIA-SPACE-SR-30-50-OpenInnovation-PLAN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-50-OpenInnovation-PLAN-A.md) | Open Innovation Plan                  | Plan                         | DRAFT    |
| [GAIA-SPACE-SR-30-60-TechnologyTransfer-PROC-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-60-TechnologyTransfer-PROC-A.md) | Technology Transfer Procedure         | Procedure                    | DRAFT    |
| [GAIA-SPACE-SR-30-70-JointResearchPrograms-PLAN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-70-JointResearchPrograms-PLAN-A.md) | Joint Research Programs Plan          | Plan                         | DRAFT    |
| [GAIA-SPACE-SR-30-00-PartnershipAgreements-ADMIN-A.md](docs/space/sr/30/GAIA-SPACE-SR-30-00-PartnershipAgreements-ADMIN-A.md) | Partnership Agreements                | Administrative Document    | DRAFT    |
</details>

</details>

---

## 8. Common Parts (Referenced by both AToC & SToC)

<details>
<summary><strong>Expand Common Parts Outline</strong></summary>

*   **Part 0: Program Foundations (GP-FD)**
    *   *Master Index:* [`ToC-GP-FD.md`](docs/common/fd/ToC-GP-FD.md) *(Placeholder Link)*
    <details><summary>Expand GP-FD Outline</summary>

        *   **FD.00: Program Management Office (PMO) Foundation**
            *   [GAIA-COMMON-FD-00-01-ProgramCharter-PLAN-A.md](docs/common/fd/00/GAIA-COMMON-FD-00-01-ProgramCharter-PLAN-A.md): Program Charter - *(PLAN)*
            *   [GAIA-COMMON-FD-00-02-OrgStructure-ADMIN-A.md](docs/common/fd/00/GAIA-COMMON-FD-00-02-OrgStructure-ADMIN-A.md): Organizational Structure - *(ADMIN, FIG)*
            *   [GAIA-COMMON-FD-00-03-GovernanceFramework-PLAN-A.md](docs/common/fd/00/GAIA-COMMON-FD-00-03-GovernanceFramework-PLAN-A.md): Governance Framework - *(PLAN, PROC)*
        *   **FD.01: Foundational Research & Theory**
            *   [GAIA-COMMON-FD-01-01-CoreConcepts-OV-A.md](docs/common/fd/01/GAIA-COMMON-FD-01-01-CoreConcepts-OV-A.md): Core Concepts (GAIA Philosophy) - *(OV, RES)*
            *   [GAIA-COMMON-FD-01-02-KeyStandardsRef-REF-A.md](docs/common/fd/01/GAIA-COMMON-FD-01-02-KeyStandardsRef-REF-A.md): Key Referenced Standards (AGIS, TPSL, etc.) - *(REF, SPEC)*
            *   [GAIA-COMMON-FD-01-03-FoundationalPapers-LIST-A.csv](docs/common/fd/01/GAIA-COMMON-FD-01-03-FoundationalPapers-LIST-A.csv): Foundational Scientific Papers - *(RES, LIST)*
        *   **FD.02: Requirements & Specifications Framework**
            *   [GAIA-COMMON-FD-02-01-ReqHierarchyMgmt-PLAN-A.md](docs/common/fd/02/GAIA-COMMON-FD-02-01-ReqHierarchyMgmt-PLAN-A.md): Requirements Hierarchy & Management Process - *(PLAN, PROC)* (Ref URIF)
            *   [GAIA-COMMON-FD-02-02-SpecTemplateStd-SPEC-A.yaml](docs/common/fd/02/GAIA-COMMON-FD-02-02-SpecTemplateStd-SPEC-A.yaml): Specification Template Standard - *(SPEC)*
            *   [GAIA-COMMON-FD-02-03-VnVStrategy-PLAN-A.md](docs/common/fd/02/GAIA-COMMON-FD-02-03-VnVStrategy-PLAN-A.md): Verification & Validation Strategy (Top Level) - *(PLAN)*
        *   **FD.03: Design & Development Framework**
            *   [GAIA-COMMON-FD-03-01-DesignPhilosophy-OV-A.md](docs/common/fd/03/GAIA-COMMON-FD-03-01-DesignPhilosophy-OV-A.md): GAIA Design Philosophy - *(OV)*
            *   [GAIA-COMMON-FD-03-02-MBSEApproach-PLAN-A.md](docs/common/fd/03/GAIA-COMMON-FD-03-02-MBSEApproach-PLAN-A.md): Model-Based Systems Engineering (MBSE) Approach - *(PLAN, PROC)*
            *   [GAIA-COMMON-FD-03-03-IDEStandards-SPEC-A.yaml](docs/common/fd/03/GAIA-COMMON-FD-03-03-IDEStandards-SPEC-A.yaml): Integrated Development Environment (IDE) Standards - *(SPEC)*
        *   **FD.04: Ethical Framework & Governance (incl. AI Ethics)**
            *   [GAIA-COMMON-FD-04-01-EthicalPrinciples-SPEC-A.yaml](docs/common/fd/04/GAIA-COMMON-FD-04-01-EthicalPrinciples-SPEC-A.yaml): GAIA Ethical Principles - *(SPEC)* (Ref CEU)
            *   [GAIA-COMMON-FD-04-02-EthicsBoardCharter-ADMIN-A.md](docs/common/fd/04/GAIA-COMMON-FD-04-02-EthicsBoardCharter-ADMIN-A.md): Ethics Governance Board Charter & Procedures - *(ADMIN, PROC)*
            *   [GAIA-COMMON-FD-04-03-AIEthicsGuidelines-SPEC-A.yaml](docs/common/fd/04/GAIA-COMMON-FD-04-03-AIEthicsGuidelines-SPEC-A.yaml): AI Ethics Guidelines & Compliance Checklist - *(SPEC, LIST)*
            *   [GAIA-COMMON-FD-04-04-ComplianceMonitoring-PROC-A.md](docs/common/fd/04/GAIA-COMMON-FD-04-04-ComplianceMonitoring-PROC-A.md): Compliance Monitoring & Reporting - *(PROC, RPT)*
        *   **FD.05: AI Documentation Standards (Preferred InfoCodes)**
            *   [GAIA-COMMON-FD-05-01-AIDocStandards-OV-A.md](docs/common/fd/05/GAIA-COMMON-FD-05-01-AIDocStandards-OV-A.md): AI Documentation Standards Overview - *(OV)*
            *   [GAIA-COMMON-FD-05-02-AIInfoCodes-SPEC-A.yaml](docs/common/fd/05/GAIA-COMMON-FD-05-02-AIInfoCodes-SPEC-A.yaml): Preferred InfoCodes per AI Chapter Specification - *(SPEC)*
            *   [GAIA-COMMON-FD-05-03-AIDocPlan-PLAN-A.md](docs/common/fd/05/GAIA-COMMON-FD-05-03-AIDocPlan-PLAN-A.md): AI Documentation Development Plan - *(PLAN)*
        *   **FD.10: AI Foundation** *(OV, SPEC, REQ, SDD, PLAN, CONOPS)*
        *   **FD.20: Machine Learning Systems** *(OV, SDD, DD, REQ, CAL, TEST, PROC, SWD, CERT)*
        *   **FD.30: Natural Language Processing** *(OV, DD, SDD, CAL, TEST, RES, PLAN, SWD, GLO)*
        *   **FD.40: Computer Vision** *(OV, SDD, CAL, TEST, DD, SWD, CAT, FIG)*
        *   **FD.50: Autonomous Systems** *(OV, CONOPS, SDD, ICD, SPEC, PROC, TEST, CERT, LIST)*
        *   **FD.60: Decision Systems** *(OV, SDD, REQ, CAL, DD, TEST, PLAN, RPT)*
        *   **FD.70: AI Ethics & Governance** *(OV, REQ, SPEC, PLAN, CERT, RPT, PROC, GLO, RES)*
        *   **FD.80: AI Lifecycle Management** *(OV, PLAN, MPD, TEST, CERT, PROC, ADMIN, RPT, WBS)*
        *   **FD.90: AI Integration & Interfaces** *(OV, ICD, SPEC, LIST, DWG, CAT, CAL, TEST)*

    </details>
*   **Part: Computing Networks (CN 00-99)** *(Formerly GP-COM / Part III in AToC)*
    *   *Master Index:* [`ToC-GP-CN.md`](docs/common/cn/ToC-GP-CN.md) *(Placeholder Link)*
    <details><summary>Expand GP-CN Outline</summary>

        #### CN 10 - Data Networks
        *   [GAIA-COMMON-CN-10-00-Overview-OV-A.md](docs/common/cn/10/GAIA-COMMON-CN-10-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-10-10-IMANetworks-SDD-A.yaml](docs/common/cn/10/GAIA-COMMON-CN-10-10-IMANetworks-SDD-A.yaml)
        *   [GAIA-COMMON-CN-10-20-SecureDataLinks-SDD-A.yaml](docs/common/cn/10/GAIA-COMMON-CN-10-20-SecureDataLinks-SDD-A.yaml)
        *   [GAIA-COMMON-CN-10-30-WirelessNetworks-SDD-A.yaml](docs/common/cn/10/GAIA-COMMON-CN-10-30-WirelessNetworks-SDD-A.yaml)
        *   [GAIA-COMMON-CN-10-40-QuantumNetworks-SDD-A.yaml](docs/common/cn/10/GAIA-COMMON-CN-10-40-QuantumNetworks-SDD-A.yaml)
        #### CN 20 - Information Security
        *   [GAIA-COMMON-CN-20-00-Overview-OV-A.md](docs/common/cn/20/GAIA-COMMON-CN-20-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-20-10-AuthenticationSys-SDD-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-10-AuthenticationSys-SDD-A.yaml)
        *   [GAIA-COMMON-CN-20-20-EncryptionSys-SDD-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-20-EncryptionSys-SDD-A.yaml)
        *   [GAIA-COMMON-CN-20-30-IntrusionDetection-SDD-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-30-IntrusionDetection-SDD-A.yaml)
        *   [GAIA-COMMON-CN-20-40-ThreatIntelligence-SDD-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-40-ThreatIntelligence-SDD-A.yaml)
        *   [GAIA-COMMON-CN-20-50-QuantumCrypto-SDD-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-50-QuantumCrypto-SDD-A.yaml)
        *   [GAIA-COMMON-CN-20-60-AISecurityMonitor-SDD-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-60-AISecurityMonitor-SDD-A.yaml)
        *   [GAIA-COMMON-CN-20-70-SecurityArchitecture-ARCH-A.yaml](docs/common/cn/20/GAIA-COMMON-CN-20-70-SecurityArchitecture-ARCH-A.yaml)
        #### CN 30 - Data Management
        *   [GAIA-COMMON-CN-30-00-Overview-OV-A.md](docs/common/cn/30/GAIA-COMMON-CN-30-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-30-10-Databases-SDD-A.yaml](docs/common/cn/30/GAIA-COMMON-CN-30-10-Databases-SDD-A.yaml)
        *   [GAIA-COMMON-CN-30-20-DataStorage-SDD-A.yaml](docs/common/cn/30/GAIA-COMMON-CN-30-20-DataStorage-SDD-A.yaml)
        *   [GAIA-COMMON-CN-30-30-DataAnalytics-SDD-A.yaml](docs/common/cn/30/GAIA-COMMON-CN-30-30-DataAnalytics-SDD-A.yaml)
        *   [GAIA-COMMON-CN-30-40-BigDataSystems-SDD-A.yaml](docs/common/cn/30/GAIA-COMMON-CN-30-40-BigDataSystems-SDD-A.yaml)
        *   [GAIA-COMMON-CN-30-50-QuantumDataProcessing-SDD-A.yaml](docs/common/cn/30/GAIA-COMMON-CN-30-50-QuantumDataProcessing-SDD-A.yaml)
        *   [GAIA-COMMON-CN-30-60-AIKnowledgeGraphs-SDD-A.yaml](docs/common/cn/30/GAIA-COMMON-CN-30-60-AIKnowledgeGraphs-SDD-A.yaml)
        *   [GAIA-COMMON-CN-30-70-DataGovernance-PLAN-A.md](docs/common/cn/30/GAIA-COMMON-CN-30-70-DataGovernance-PLAN-A.md)
        #### CN 40 - Computing Infrastructure
        *   [GAIA-COMMON-CN-40-00-Overview-OV-A.md](docs/common/cn/40/GAIA-COMMON-CN-40-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-40-10-EdgeComputing-SDD-A.yaml](docs/common/cn/40/GAIA-COMMON-CN-40-10-EdgeComputing-SDD-A.yaml)
        *   [GAIA-COMMON-CN-40-20-CloudServices-SDD-A.yaml](docs/common/cn/40/GAIA-COMMON-CN-40-20-CloudServices-SDD-A.yaml)
        *   [GAIA-COMMON-CN-40-30-ServerArchitecture-ARCH-A.yaml](docs/common/cn/40/GAIA-COMMON-CN-40-30-ServerArchitecture-ARCH-A.yaml)
        *   [GAIA-COMMON-CN-40-40-QuantumCompute-SDD-A.yaml](docs/common/cn/40/GAIA-COMMON-CN-40-40-QuantumCompute-SDD-A.yaml)
        *   [GAIA-COMMON-CN-40-50-AIAccelerators-SDD-A.yaml](docs/common/cn/40/GAIA-COMMON-CN-40-50-AIAccelerators-SDD-A.yaml)
        #### CN 50 - Software Modules Core
        *   [GAIA-COMMON-CN-50-00-Overview-OV-A.md](docs/common/cn/50/GAIA-COMMON-CN-50-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-50-10-PolicyEngine-SDD-A.yaml](docs/common/cn/50/GAIA-COMMON-CN-50-10-PolicyEngine-SDD-A.yaml)
        *   [GAIA-COMMON-CN-50-20-BITT-SDD-A.yaml](docs/common/cn/50/GAIA-COMMON-CN-50-20-BITT-SDD-A.yaml)
        *   [GAIA-COMMON-CN-50-30-COAFI-SDD-A.yaml](docs/common/cn/50/GAIA-COMMON-CN-50-30-COAFI-SDD-A.yaml)
        *   *(... Other Core Software Modules SDDs ...)*
        #### CN 51 - Security Modules Core
        *   [GAIA-COMMON-CN-51-00-Overview-OV-A.md](docs/common/cn/51/GAIA-COMMON-CN-51-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-51-10-SecGateway-SDD-A.yaml](docs/common/cn/51/GAIA-COMMON-CN-51-10-SecGateway-SDD-A.yaml)
        *   [GAIA-COMMON-CN-51-20-QuantumCrypto-SDD-A.yaml](docs/common/cn/51/GAIA-COMMON-CN-51-20-QuantumCrypto-SDD-A.yaml)
        *   *(... Other Core Security Modules SDDs ...)*
        #### CN 52 - AI Modules Core
        *   [GAIA-COMMON-CN-52-00-Overview-OV-A.md](docs/common/cn/52/GAIA-COMMON-CN-52-00-Overview-OV-A.md)
        *   [GAIA-COMMON-CN-52-10-LLMCore-SDD-A.yaml](docs/common/cn/52/GAIA-COMMON-CN-52-10-LLMCore-SDD-A.yaml)
        *   [GAIA-COMMON-CN-52-20-Vision-SDD-A.yaml](docs/common/cn/52/GAIA-COMMON-CN-52-20-Vision-SDD-A.yaml)
        *   [GAIA-COMMON-CN-52-30-Prediction-SDD-A.yaml](docs/common/cn/52/GAIA-COMMON-CN-52-30-Prediction-SDD-A.yaml)
        *   *(... Other Core AI Modules SDDs ...)*

    </details>
*   **Part: Ground-Based Systems (GB 00-99)** *(Formerly GP-GRO / Part IV in AToC)*
    *   *Master Index:* [`ToC-GP-GB.md`](docs/common/gb/ToC-GP-GB.md) *(Placeholder Link)*
    <details><summary>Expand GP-GB Outline</summary>

        #### GB 10 - Ground Control
        *   [GAIA-COMMON-GB-10-00-Overview-OV-A.md](docs/common/gb/10/GAIA-COMMON-GB-10-00-Overview-OV-A.md)
        *   [GAIA-COMMON-GB-10-10-ControlCenters-SDD-A.yaml](docs/common/gb/10/GAIA-COMMON-GB-10-10-ControlCenters-SDD-A.yaml)
        *   [GAIA-COMMON-GB-10-20-RemoteOperations-SDD-A.yaml](docs/common/gb/10/GAIA-COMMON-GB-10-20-RemoteOperations-SDD-A.yaml)
        *   [GAIA-COMMON-GB-10-30-GCSArchitecture-ARCH-A.yaml](docs/common/gb/10/GAIA-COMMON-GB-10-30-GCSArchitecture-ARCH-A.yaml)
        *   [GAIA-COMMON-GB-10-40-AIGroundControl-SDD-A.yaml](docs/common/gb/10/GAIA-COMMON-GB-10-40-AIGroundControl-SDD-A.yaml)
        #### GB 20 - Ground Support Equipment (GSE)
        *   [GAIA-COMMON-GB-20-00-Overview-OV-A.md](docs/common/gb/20/GAIA-COMMON-GB-20-00-Overview-OV-A.md)
        *   [GAIA-COMMON-GB-20-10-PowerSupport-SDD-A.yaml](docs/common/gb/20/GAIA-COMMON-GB-20-10-PowerSupport-SDD-A.yaml)
        *   [GAIA-COMMON-GB-20-20-ServicingEquip-SDD-A.yaml](docs/common/gb/20/GAIA-COMMON-GB-20-20-ServicingEquip-SDD-A.yaml)
        *   [GAIA-COMMON-GB-20-30-AirconditgEqpt-SDD-A.yaml](docs/common/gb/20/GAIA-COMMON-GB-20-30-AirconditgEqpt-SDD-A.yaml)
        *   [GAIA-COMMON-GB-20-40-TestEquipment-SDD-A.yaml](docs/common/gb/20/GAIA-COMMON-GB-20-40-TestEquipment-SDD-A.yaml)
        *   [GAIA-COMMON-GB-20-50-AIDiagnosticsGSE-SDD-A.yaml](docs/common/gb/20/GAIA-COMMON-GB-20-50-AIDiagnosticsGSE-SDD-A.yaml)
        *   [GAIA-COMMON-GB-20-60-RoboticGSE-SDD-A.yaml](docs/common/gb/20/GAIA-COMMON-GB-20-60-RoboticGSE-SDD-A.yaml)
        #### GB 30 - Ground Transportation & Logistics
        *   [GAIA-COMMON-GB-30-00-Overview-OV-A.md](docs/common/gb/30/GAIA-COMMON-GB-30-00-Overview-OV-A.md)
        *   [GAIA-COMMON-GB-30-10-VehicleSystems-SDD-A.yaml](docs/common/gb/30/GAIA-COMMON-GB-30-10-VehicleSystems-SDD-A.yaml)
        *   [GAIA-COMMON-GB-30-20-AutonomousVehicles-SDD-A.yaml](docs/common/gb/30/GAIA-COMMON-GB-30-20-AutonomousVehicles-SDD-A.yaml)
        *   [GAIA-COMMON-GB-30-30-ChargingFuelingInfra-SDD-A.yaml](docs/common/gb/30/GAIA-COMMON-GB-30-30-ChargingFuelingInfra-SDD-A.yaml)
        *   [GAIA-COMMON-GB-30-40-AIFleetOptimizer-SDD-A.yaml](docs/common/gb/30/GAIA-COMMON-GB-30-40-AIFleetOptimizer-SDD-A.yaml)
        *   [GAIA-COMMON-GB-30-50-GroundLogisticsPlan-PLAN-A.md](docs/common/gb/30/GAIA-COMMON-GB-30-50-GroundLogisticsPlan-PLAN-A.md)
        #### GB 40 - Launch/Landing Facilities
        *   [GAIA-COMMON-GB-40-00-Overview-OV-A.md](docs/common/gb/40/GAIA-COMMON-GB-40-00-Overview-OV-A.md)
        *   [GAIA-COMMON-GB-40-10-AirfieldSpaceportDesign-DD-A.yaml](docs/common/gb/40/GAIA-COMMON-GB-40-10-AirfieldSpaceportDesign-DD-A.yaml)
        *   [GAIA-COMMON-GB-40-20-LaunchSystemsInterface-ICD-A.yaml](docs/common/gb/40/GAIA-COMMON-GB-40-20-LaunchSystemsInterface-ICD-A.yaml)
        *   [GAIA-COMMON-GB-40-30-LandingRecoverySys-SDD-A.yaml](docs/common/gb/40/GAIA-COMMON-GB-40-30-LandingRecoverySys-SDD-A.yaml)
        *   [GAIA-COMMON-GB-40-40-InfrastructureMgmt-PROC-A.md](docs/common/gb/40/GAIA-COMMON-GB-40-40-InfrastructureMgmt-PROC-A.md)

    </details>
*   **Part: Supply Chain & Logistics (GP-SUPL)** *(Formerly Part V in AToC)*
    *   *Master Index:* [`ToC-GP-SUPL.md`](docs/common/supl/ToC-GP-SUPL.md) *(Placeholder Link)*
    <details><summary>Expand GP-SUPL Outline</summary>

        *   **SUPL.00: Supply Chain Management Overview**
            *   [GAIA-COMMON-SUPL-00-01-SCM-Philosophy-OV-A.md](docs/common/supl/00/GAIA-COMMON-SUPL-00-01-SCM-Philosophy-OV-A.md)
            *   [GAIA-COMMON-SUPL-00-02-Standards-SPEC-A.yaml](docs/common/supl/00/GAIA-COMMON-SUPL-00-02-Standards-SPEC-A.yaml)
            *   [GAIA-COMMON-SUPL-00-03-RiskMgmt-PLAN-A.md](docs/common/supl/00/GAIA-COMMON-SUPL-00-03-RiskMgmt-PLAN-A.md)
        *   **SUPL.10: Supplier Management & Vetting**
            *   [GAIA-COMMON-SUPL-10-01-SupplierQual-PROC-A.md](docs/common/supl/10/GAIA-COMMON-SUPL-10-01-SupplierQual-PROC-A.md)
            *   [GAIA-COMMON-SUPL-10-02-SupplierCodeConduct-SPEC-A.yaml](docs/common/supl/10/GAIA-COMMON-SUPL-10-02-SupplierCodeConduct-SPEC-A.yaml)
            *   [GAIA-COMMON-SUPL-10-03-SupplierMonitor-PROC-A.md](docs/common/supl/10/GAIA-COMMON-SUPL-10-03-SupplierMonitor-PROC-A.md)
            *   [GAIA-COMMON-SUPL-10-04-SupplierMgmtSys-SDD-A.yaml](docs/common/supl/10/GAIA-COMMON-SUPL-10-04-SupplierMgmtSys-SDD-A.yaml)
        *   **SUPL.20: Ethical & Sustainable Sourcing**
            *   [GAIA-COMMON-SUPL-20-01-SustainableSource-SPEC-A.yaml](docs/common/supl/20/GAIA-COMMON-SUPL-20-01-SustainableSource-SPEC-A.yaml)
            *   [GAIA-COMMON-SUPL-20-02-ConflictMinerals-SPEC-A.yaml](docs/common/supl/20/GAIA-COMMON-SUPL-20-02-ConflictMinerals-SPEC-A.yaml)
            *   [GAIA-COMMON-SUPL-20-03-FairLaborVerify-PROC-A.md](docs/common/supl/20/GAIA-COMMON-SUPL-20-03-FairLaborVerify-PROC-A.md)
            *   [GAIA-COMMON-SUPL-20-04-CarbonTrackSource-PROC-A.md](docs/common/supl/20/GAIA-COMMON-SUPL-20-04-CarbonTrackSource-PROC-A.md)
        *   **SUPL.30: Material & Component Traceability**
            *   [GAIA-COMMON-SUPL-30-01-TraceabilityReqs-REQ-A.yaml](docs/common/supl/30/GAIA-COMMON-SUPL-30-01-TraceabilityReqs-REQ-A.yaml)
            *   [GAIA-COMMON-SUPL-30-02-BITTIntegration-ICD-A.yaml](docs/common/supl/30/GAIA-COMMON-SUPL-30-02-BITTIntegration-ICD-A.yaml)
            *   [GAIA-COMMON-SUPL-30-03-TLS-UTidS-App-PROC-A.md](docs/common/supl/30/GAIA-COMMON-SUPL-30-03-TLS-UTidS-App-PROC-A.md)
            *   [GAIA-COMMON-SUPL-30-04-CounterfeitPrevent-PLAN-A.md](docs/common/supl/30/GAIA-COMMON-SUPL-30-04-CounterfeitPrevent-PLAN-A.md)
        *   **SUPL.40: Logistics & Transportation Optimization**
            *   [GAIA-COMMON-SUPL-40-01-GreenLogistics-PLAN-A.md](docs/common/supl/40/GAIA-COMMON-SUPL-40-01-GreenLogistics-PLAN-A.md)
            *   [GAIA-COMMON-SUPL-40-02-RouteOptimization-ALGO-A.yaml](docs/common/supl/40/GAIA-COMMON-SUPL-40-02-RouteOptimization-ALGO-A.yaml)
            *   [GAIA-COMMON-SUPL-40-03-SustainablePkg-SPEC-A.yaml](docs/common/supl/40/GAIA-COMMON-SUPL-40-03-SustainablePkg-SPEC-A.yaml)
            *   [GAIA-COMMON-SUPL-40-04-LogisticsPartnerReqs-SPEC-A.yaml](docs/common/supl/40/GAIA-COMMON-SUPL-40-04-LogisticsPartnerReqs-SPEC-A.yaml)
        *   **SUPL.50: End-of-Life Management & Circular Economy**
            *   [GAIA-COMMON-SUPL-50-01-EOL-Disposal-PROC-A.md](docs/common/supl/50/GAIA-COMMON-SUPL-50-01-EOL-Disposal-PROC-A.md)
            *   [GAIA-COMMON-SUPL-50-02-RecyclingRecovery-PROC-A.md](docs/common/supl/50/GAIA-COMMON-SUPL-50-02-RecyclingRecovery-PROC-A.md)
            *   [GAIA-COMMON-SUPL-50-03-DesignDisassembly-SPEC-A.yaml](docs/common/supl/50/GAIA-COMMON-SUPL-50-03-DesignDisassembly-SPEC-A.yaml)
            *   [GAIA-COMMON-SUPL-50-04-CircularEconomyMetrics-RPT-A.md](docs/common/supl/50/GAIA-COMMON-SUPL-50-04-CircularEconomyMetrics-RPT-A.md)

       </details>
*   **Part: Robotic Systems (GP-RAME)** *(Formerly Part VI in AToC)*
    *   *Master Index:* [`ToC-GP-RAME.md`](docs/common/rame/ToC-GP-RAME.md) *(Placeholder Link)*
    <details><summary>Expand GP-RAME Outline</summary>

        *   **RAME.00: Robotic Systems Overview**
            *   [GAIA-COMMON-RAME-00-01-RoboticsStrategy-OV-A.md](docs/common/rame/00/GAIA-COMMON-RAME-00-01-RoboticsStrategy-OV-A.md): Robotics & Automation Strategy for GAIA - *(OV, PLAN)*
            *   [GAIA-COMMON-RAME-00-02-SafetyStandards-SPEC-A.yaml](docs/common/rame/00/GAIA-COMMON-RAME-00-02-SafetyStandards-SPEC-A.yaml): Safety Standards for Robotic Operations (ISO 10218) - *(SPEC, SEC)*
            *   [GAIA-COMMON-RAME-00-03-HRCFramework-CONOPS-A.md](docs/common/rame/00/GAIA-COMMON-RAME-00-03-HRCFramework-CONOPS-A.md): Human-Robot Collaboration Framework - *(CONOPS, SPEC)*
        *   **RAME.10: Robotic Assembly Systems**
            *   [GAIA-COMMON-RAME-10-01-AssemblyLineDesign-DD-A.yaml](docs/common/rame/10/GAIA-COMMON-RAME-10-01-AssemblyLineDesign-DD-A.yaml): Automated Assembly Line Design - *(DD, ARCH)*
            *   [GAIA-COMMON-RAME-10-02-LargeStructureRobots-SDD-A.yaml](docs/common/rame/10/GAIA-COMMON-RAME-10-02-LargeStructureRobots-SDD-A.yaml): Large Structure Assembly Robots (Fuselage, Wings) - *(SDD, SPEC)*
            *   [GAIA-COMMON-RAME-10-03-PrecisionRobots-SDD-A.yaml](docs/common/rame/10/GAIA-COMMON-RAME-10-03-PrecisionRobots-SDD-A.yaml): Precision Assembly Robots (Avionics, Small Components) - *(SDD, SPEC)*
            *   [GAIA-COMMON-RAME-10-04-AFP-Systems-SDD-A.yaml](docs/common/rame/10/GAIA-COMMON-RAME-10-04-AFP-Systems-SDD-A.yaml): Automated Fiber Placement (AFP) Systems - *(SDD, PROC)* (Ref ATA 20-AM)
            *   [GAIA-COMMON-RAME-10-05-AMIntegration-SDD-A.yaml](docs/common/rame/10/GAIA-COMMON-RAME-10-05-AMIntegration-SDD-A.yaml): Additive Manufacturing Integration Robots - *(SDD, ICD)* (Ref ATA 20-AM)
        *   **RAME.20: Automated Inspection & Quality Control**
            *   [GAIA-COMMON-RAME-20-01-RoboticNDI-SDD-A.yaml](docs/common/rame/20/GAIA-COMMON-RAME-20-01-RoboticNDI-SDD-A.yaml): Robotic Non-Destructive Inspection (NDI) Systems - *(SDD, PROC)* (Ref ATA 05)
            *   [GAIA-COMMON-RAME-20-02-VisualInspection-SDD-A.yaml](docs/common/rame/20/GAIA-COMMON-RAME-20-02-VisualInspection-SDD-A.yaml): Automated Visual Inspection Systems (AI Vision) - *(SDD, ALGO)* (Ref GP-COM-AI)
            *   [GAIA-COMMON-RAME-20-03-CMMAutomation-SDD-A.yaml](docs/common/rame/20/GAIA-COMMON-RAME-20-03-CMMAutomation-SDD-A.yaml): Coordinate Measuring Machine (CMM) Automation - *(SDD, PROC)*
            *   [GAIA-COMMON-RAME-20-04-QualityDataBITT-ICD-A.yaml](docs/common/rame/20/GAIA-COMMON-RAME-20-04-QualityDataBITT-ICD-A.yaml): Quality Data Integration with BITT - *(ICD)*
        *   **RAME.30: Robotic Maintenance Systems**
            *   [GAIA-COMMON-RAME-30-01-MaintRobotCaps-OV-A.md](docs/common/rame/30/GAIA-COMMON-RAME-30-01-MaintRobotCaps-OV-A.md): Maintenance Robot Capabilities Overview - *(OV, SPEC)*
            *   [GAIA-COMMON-RAME-30-02-ExteriorRobots-SDD-A.yaml](docs/common/rame/30/GAIA-COMMON-RAME-30-02-ExteriorRobots-SDD-A.yaml): Aircraft Exterior Inspection & Cleaning Robots - *(SDD, PROC)*
            *   [GAIA-COMMON-RAME-30-03-ComponentRobots-SDD-A.yaml](docs/common/rame/30/GAIA-COMMON-RAME-30-03-ComponentRobots-SDD-A.yaml): Component Removal & Replacement Robots (LRU) - *(SDD, PROC)*
            *   [GAIA-COMMON-RAME-30-04-ConfinedSpaceRobots-SDD-A.yaml](docs/common/rame/30/GAIA-COMMON-RAME-30-04-ConfinedSpaceRobots-SDD-A.yaml): Confined Space Maintenance Robots - *(SDD, SPEC)*
            *   [GAIA-COMMON-RAME-30-05-Teleoperation-ICD-A.yaml](docs/common/rame/30/GAIA-COMMON-RAME-30-05-Teleoperation-ICD-A.yaml): Remote Teleoperation Interfaces - *(ICD, UG)*
        *   **RAME.40: Human-Robot Collaboration (HRC)**
            *   [GAIA-COMMON-RAME-40-01-HRCSafety-SEC-A.yaml](docs/common/rame/40/GAIA-COMMON-RAME-40-01-HRCSafety-SEC-A.yaml): HRC Safety Protocols & Zones - *(SEC, PROC)*
            *   [GAIA-COMMON-RAME-40-02-CollaborativeTasks-CONOPS-A.md](docs/common/rame/40/GAIA-COMMON-RAME-40-02-CollaborativeTasks-CONOPS-A.md): Collaborative Task Design - *(CONOPS, PROC)*
            *   [GAIA-COMMON-RAME-40-03-ARGuidanceHRC-SDD-A.yaml](docs/common/rame/40/GAIA-COMMON-RAME-40-03-ARGuidanceHRC-SDD-A.yaml): Augmented Reality (AR) Guidance for HRC - *(SDD, UG)*
        *   **RAME.50: Integration with Predictive Maintenance (PdM)**
            *   [GAIA-COMMON-RAME-50-01-PdMInterface-ICD-A.yaml](docs/common/rame/50/GAIA-COMMON-RAME-50-01-PdMInterface-ICD-A.yaml): PdM System Interface for Robotic Tasking - *(ICD)* (Ref ATA 45)
            *   [GAIA-COMMON-RAME-50-02-AutomatedTaskGen-ALGO-A.yaml](docs/common/rame/50/GAIA-COMMON-RAME-50-02-AutomatedTaskGen-ALGO-A.yaml): Automated Maintenance Task Generation from PdM Alerts - *(ALGO, SDD)*
            *   [GAIA-COMMON-RAME-50-03-RoboticExecutionPdM-PROC-A.md](docs/common/rame/50/GAIA-COMMON-RAME-50-03-RoboticExecutionPdM-PROC-A.md): Robotic Execution of PdM-Recommended Actions - *(PROC, CONOPS)*

    </details>
*   **Part: Project Management (GP-PM / PM 00-99)** *(Shared between AToC Part VII & SToC Part VI)*
    *   *Master Index:* [`ToC-GP-PM.md`](docs/common/pm/ToC-GP-PM.md) *(Placeholder Link)*
    <details><summary>Expand GP-PM / PM Outline</summary>

        #### PM 10 - Project Planning & Execution
        *   [GAIA-COMMON-PM-10-00-Overview-OV-A.md](docs/common/pm/10/GAIA-COMMON-PM-10-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-10-10-ProjectCharter-PLAN-A.md](docs/common/pm/10/GAIA-COMMON-PM-10-10-ProjectCharter-PLAN-A.md)
        *   [GAIA-COMMON-PM-10-20-WBS-WBS-A.md](docs/common/pm/10/GAIA-COMMON-PM-10-20-WBS-WBS-A.md)
        *   [GAIA-COMMON-PM-10-30-Schedules-PLAN-A.md](docs/common/pm/10/GAIA-COMMON-PM-10-30-Schedules-PLAN-A.md)
        *   [GAIA-COMMON-PM-10-40-Resources-PLAN-A.md](docs/common/pm/10/GAIA-COMMON-PM-10-40-Resources-PLAN-A.md)
        *   [GAIA-COMMON-PM-10-50-AIProjectPlanning-SDD-A.yaml](docs/common/pm/10/GAIA-COMMON-PM-10-50-AIProjectPlanning-SDD-A.yaml)
        *   [GAIA-COMMON-PM-10-60-CommunicationPlan-PLAN-A.md](docs/common/pm/10/GAIA-COMMON-PM-10-60-CommunicationPlan-PLAN-A.md)
        #### PM 20 - Configuration Management
        *   [GAIA-COMMON-PM-20-00-Overview-OV-A.md](docs/common/pm/20/GAIA-COMMON-PM-20-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-20-10-CMPlan-PLAN-A.md](docs/common/pm/20/GAIA-COMMON-PM-20-10-CMPlan-PLAN-A.md)
        *   [GAIA-COMMON-PM-20-20-ChangeControl-PROC-A.md](docs/common/pm/20/GAIA-COMMON-PM-20-20-ChangeControl-PROC-A.md)
        *   [GAIA-COMMON-PM-20-30-Baselines-BASE-A.md](docs/common/pm/20/GAIA-COMMON-PM-20-30-Baselines-BASE-A.md)
        *   [GAIA-COMMON-PM-20-40-VersionControl-PROC-A.md](docs/common/pm/20/GAIA-COMMON-PM-20-40-VersionControl-PROC-A.md)
        *   [GAIA-COMMON-PM-20-50-AIConfigOptimizer-SDD-A.yaml](docs/common/pm/20/GAIA-COMMON-PM-20-50-AIConfigOptimizer-SDD-A.yaml)
        *   [GAIA-COMMON-PM-20-60-DocumentationControl-PROC-A.md](docs/common/pm/20/GAIA-COMMON-PM-20-60-DocumentationControl-PROC-A.md)
        #### PM 30 - Quality Assurance
        *   [GAIA-COMMON-PM-30-00-Overview-OV-A.md](docs/common/pm/30/GAIA-COMMON-PM-30-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-30-10-QAPlan-PLAN-A.md](docs/common/pm/30/GAIA-COMMON-PM-30-10-QAPlan-PLAN-A.md)
        *   [GAIA-COMMON-PM-30-20-QAProcesses-PROC-A.md](docs/common/pm/30/GAIA-COMMON-PM-30-20-QAProcesses-PROC-A.md)
        *   [GAIA-COMMON-PM-30-30-QAStandards-SPEC-A.yaml](docs/common/pm/30/GAIA-COMMON-PM-30-30-QAStandards-SPEC-A.yaml) (Ref AS9100/ECSS)
        *   [GAIA-COMMON-PM-30-40-QAMetrics-LIST-A.csv](docs/common/pm/30/GAIA-COMMON-PM-30-40-QAMetrics-LIST-A.csv)
        *   [GAIA-COMMON-PM-30-50-AIQualityMonitor-SDD-A.yaml](docs/common/pm/30/GAIA-COMMON-PM-30-50-AIQualityMonitor-SDD-A.yaml)
        *   [GAIA-COMMON-PM-30-60-TestingVerificationPlan-PLAN-A.md](docs/common/pm/30/GAIA-COMMON-PM-30-60-TestingVerificationPlan-PLAN-A.md)
        *   [GAIA-COMMON-PM-30-70-QualityReporting-PROC-A.md](docs/common/pm/30/GAIA-COMMON-PM-30-70-QualityReporting-PROC-A.md)
        *   [GAIA-COMMON-PM-30-80-AuditProcedure-PROC-A.md](docs/common/pm/30/GAIA-COMMON-PM-30-80-AuditProcedure-PROC-A.md)
        #### PM 40 - Risk Management
        *   [GAIA-COMMON-PM-40-00-Overview-OV-A.md](docs/common/pm/40/GAIA-COMMON-PM-40-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-40-10-RiskManagementPlan-PLAN-A.md](docs/common/pm/40/GAIA-COMMON-PM-40-10-RiskManagementPlan-PLAN-A.md)
        *   [GAIA-COMMON-PM-40-20-RiskRegister-LIST-A.csv](docs/common/pm/40/GAIA-COMMON-PM-40-20-RiskRegister-LIST-A.csv)
        *   [GAIA-COMMON-PM-40-30-RiskMitigation-PROC-A.md](docs/common/pm/40/GAIA-COMMON-PM-40-30-RiskMitigation-PROC-A.md)
        *   [GAIA-COMMON-PM-40-40-OpportunityManagement-PROC-A.md](docs/common/pm/40/GAIA-COMMON-PM-40-40-OpportunityManagement-PROC-A.md)
        #### PM 50 - Governance & Compliance
        *   [GAIA-COMMON-PM-50-00-Overview-OV-A.md](docs/common/pm/50/GAIA-COMMON-PM-50-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-50-10-RegulatoryComplianceFramework-SPEC-A.yaml](docs/common/pm/50/GAIA-COMMON-PM-50-10-RegulatoryComplianceFramework-SPEC-A.yaml) (Ref EASA/FAA/Space Law)
        *   [GAIA-COMMON-PM-50-20-EthicalGuidelines-SPEC-A.yaml](docs/common/pm/50/GAIA-COMMON-PM-50-20-EthicalGuidelines-SPEC-A.yaml) (Ref GP-FD)
        *   [GAIA-COMMON-PM-50-30-CertificationPlan-PLAN-A.md](docs/common/pm/50/GAIA-COMMON-PM-50-30-CertificationPlan-PLAN-A.md)
        *   [GAIA-COMMON-PM-50-40-GovernanceModel-ADMIN-A.md](docs/common/pm/50/GAIA-COMMON-PM-50-40-GovernanceModel-ADMIN-A.md)
        #### PM 60 - Digital Twin ROI (DT-ROI)
        *   [GAIA-COMMON-PM-60-00-Overview-OV-A.md](docs/common/pm/60/GAIA-COMMON-PM-60-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-60-10-DT-ROI-Framework-REF-A.md](docs/common/pm/60/GAIA-COMMON-PM-60-10-DT-ROI-Framework-REF-A.md) (Ref GP-FD)
        *   [GAIA-COMMON-PM-60-20-DT-ROI-Templates-SPEC-A.yaml](docs/common/pm/60/GAIA-COMMON-PM-60-20-DT-ROI-Templates-SPEC-A.yaml)
        *   [GAIA-COMMON-PM-60-30-Program-DT-ROI-Report-RPT-A.md](docs/common/pm/60/GAIA-COMMON-PM-60-30-Program-DT-ROI-Report-RPT-A.md)
        *   [GAIA-COMMON-PM-60-40-ROI-Monitoring-PROC-A.md](docs/common/pm/60/GAIA-COMMON-PM-60-40-ROI-Monitoring-PROC-A.md)
        #### PM 70 - Go-To-Market (GTM) & Field Support (FRSE)
        *   [GAIA-COMMON-PM-70-00-Overview-OV-A.md](docs/common/pm/70/GAIA-COMMON-PM-70-00-Overview-OV-A.md)
        *   [GAIA-COMMON-PM-70-10-GTM-Strategy-PLAN-A.md](docs/common/pm/70/GAIA-COMMON-PM-70-10-GTM-Strategy-PLAN-A.md)
        *   [GAIA-COMMON-PM-70-20-LaunchReadiness-LIST-A.csv](docs/common/pm/70/GAIA-COMMON-PM-70-20-LaunchReadiness-LIST-A.csv)
        *   [GAIA-COMMON-PM-70-30-FRSE-Strategy-PLAN-A.md](docs/common/pm/70/GAIA-COMMON-PM-70-30-FRSE-Strategy-PLAN-A.md)
        *   [GAIA-COMMON-PM-70-40-FieldSupport-PROC-A.md](docs/common/pm/70/GAIA-COMMON-PM-70-40-FieldSupport-PROC-A.md)

    </details>
*   **Part: Digital Design & AI (GP-DS)** *(Formerly Part XI in AToC)*
    *   *Master Index:* [`ToC-GP-DS.md`](docs/common/ds/ToC-GP-DS.md) *(Placeholder Link)*
    <details><summary>Expand GP-DS Outline</summary>

        *   **DS.00: Digital Design Intelligence Overview**
            *   [GAIA-COMMON-DS-00-01-VisionStrategy-OV-A.md](docs/common/ds/00/GAIA-COMMON-DS-00-01-VisionStrategy-OV-A.md): Vision & Strategy for AI/AGI in Design - *(OV, PLAN)*
            *   [GAIA-COMMON-DS-00-02-Architecture-ARCH-A.yaml](docs/common/ds/00/GAIA-COMMON-DS-00-02-Architecture-ARCH-A.yaml): Architecture of Integrated Design Systems - *(ARCH)*
            *   [GAIA-COMMON-DS-00-03-EthicalConsiderations-SPEC-A.yaml](docs/common/ds/00/GAIA-COMMON-DS-00-03-EthicalConsiderations-SPEC-A.yaml): Ethical Considerations for AI/AGI in Design - *(SPEC, RES)* (Ref GP-FD)
        *   **DS.10: Advanced Digital Design Tools**
            *   [GAIA-COMMON-DS-10-01-AIAIDED-Ext-ICD-A.yaml](docs/common/ds/10/GAIA-COMMON-DS-10-01-AIAIDED-Ext-ICD-A.yaml): AI-AIDED Platform Extensions & APIs - *(ICD, SPEC)* (Ref GP-AERO-AIDED)
            *   [GAIA-COMMON-DS-10-02-GenerativeDesign-ALGO-A.yaml](docs/common/ds/10/GAIA-COMMON-DS-10-02-GenerativeDesign-ALGO-A.yaml): Generative Design Algorithms & Systems - *(ALGO, SDD)*
            *   [GAIA-COMMON-DS-10-03-MDOFramework-SDD-A.yaml](docs/common/ds/10/GAIA-COMMON-DS-10-03-MDOFramework-SDD-A.yaml): Multidisciplinary Design Optimization (MDO) Framework - *(SDD, CAL)*
            *   [GAIA-COMMON-DS-10-04-VirtualPrototyping-SDD-A.yaml](docs/common/ds/10/GAIA-COMMON-DS-10-04-VirtualPrototyping-SDD-A.yaml): Virtual Prototyping & Simulation Environment - *(SDD, UG)*
        *   **DS.20: Cognitive Interface Design (UI/UX)**
            *   [GAIA-COMMON-DS-20-01-CognitiveUIUXPrinciples-SPEC-A.yaml](docs/common/ds/20/GAIA-COMMON-DS-20-01-CognitiveUIUXPrinciples-SPEC-A.yaml): Principles of Cognitive UI/UX for Complex Systems - *(SPEC, RES)*
            *   [GAIA-COMMON-DS-20-02-AdaptiveUI-SDD-A.yaml](docs/common/ds/20/GAIA-COMMON-DS-20-02-AdaptiveUI-SDD-A.yaml): Adaptive User Interfaces - *(SDD, ALGO)*
            *   [GAIA-COMMON-DS-20-03-NLPInterface-SDD-A.yaml](docs/common/ds/20/GAIA-COMMON-DS-20-03-NLPInterface-SDD-A.yaml): Natural Language Interfaces for Design & Analysis - *(SDD, ICD)* (Ref GP-COM-AI)
            *   [GAIA-COMMON-DS-20-04-ARVRInterface-SDD-A.yaml](docs/common/ds/20/GAIA-COMMON-DS-20-04-ARVRInterface-SDD-A.yaml): AR/VR Interfaces for Design Review & Collaboration - *(SDD, UG)* (Ref Robbotix)
        *   **DS.30: AGI Component Integration**
            *   *Note: Highly speculative, focuses on defining potential future interfaces.*
            *   [GAIA-COMMON-DS-30-01-AGIReqs-REQ-A.yaml](docs/common/ds/30/GAIA-COMMON-DS-30-01-AGIReqs-REQ-A.yaml): AGI Interface Requirements for Design Tasks - *(REQ, RES)*
            *   [GAIA-COMMON-DS-30-02-AGIArchConcept-ARCH-A.yaml](docs/common/ds/30/GAIA-COMMON-DS-30-02-AGIArchConcept-ARCH-A.yaml): Conceptual AGI Integration Architecture - *(ARCH, RES)*
            *   [GAIA-COMMON-DS-30-03-AGISafetyProtocols-SEC-A.yaml](docs/common/ds/30/GAIA-COMMON-DS-30-03-AGISafetyProtocols-SEC-A.yaml): Safety & Control Protocols for AGI Interaction - *(SEC, PROC, RES)*
            *   [GAIA-COMMON-DS-30-04-AGIDataFormats-SPEC-A.yaml](docs/common/ds/30/GAIA-COMMON-DS-30-04-AGIDataFormats-SPEC-A.yaml): Data Exchange Formats with AGI - *(SPEC, ICD)*
        *   **DS.40: Human-AI Collaboration in Design**
            *   [GAIA-COMMON-DS-40-01-CollaborationModels-CONOPS-A.md](docs/common/ds/40/GAIA-COMMON-DS-40-01-CollaborationModels-CONOPS-A.md): Models for Collaborative Design Processes - *(CONOPS, PROC)*
            *   [GAIA-COMMON-DS-40-02-XAI-Design-ALGO-A.yaml](docs/common/ds/40/GAIA-COMMON-DS-40-02-XAI-Design-ALGO-A.yaml): Explainable AI (XAI) for Design Recommendations - *(ALGO, SDD)* (Ref SMAIE/AMEDEO)
            *   [GAIA-COMMON-DS-40-03-TrustCalibration-RES-A.md](docs/common/ds/40/GAIA-COMMON-DS-40-03-TrustCalibration-RES-A.md): Trust & Calibration in Human-AI Design Teams - *(RES, RPT)*
        *   **DS.50: Knowledge Management & Design Rationale Capture**
            *   [GAIA-COMMON-DS-50-01-RationaleCaptureSys-SDD-A.yaml](docs/common/ds/50/GAIA-COMMON-DS-50-01-RationaleCaptureSys-SDD-A.yaml): Automated Design Rationale Capture System - *(SDD)*
            *   [GAIA-COMMON-DS-50-02-KnowledgeGraph-ARCH-A.yaml](docs/common/ds/50/GAIA-COMMON-DS-50-02-KnowledgeGraph-ARCH-A.yaml): Design Knowledge Graph Implementation - *(ARCH, SDD)*
            *   [GAIA-COMMON-DS-50-03-MemoryIntegration-ICD-A.yaml](docs/common/ds/50/GAIA-COMMON-DS-50-03-MemoryIntegration-ICD-A.yaml): Integration with GAIA_MEMORIES - *(ICD)*

    </details>
*   **Part: Research & Speculation (GP-DIMENSIONS)** *(Formerly Part XII in AToC)*
    *   *Master Index:* [`ToC-GP-DIMENSIONS.md`](docs/common/dimensions/ToC-GP-DIMENSIONS.md) *(Placeholder Link)*
    <details><summary>Expand GP-DIMENSIONS Outline</summary>

        *   **DIM.00: Introduction to GAIA Futures**
            *   [GAIA-COMMON-DIM-00-01-Vision-OV-A.md](docs/common/dimensions/00/GAIA-COMMON-DIM-00-01-Vision-OV-A.md): Vision for Long-Term Evolution - *(OV, RES)*
            *   [GAIA-COMMON-DIM-00-02-Methodology-PROC-A.md](docs/common/dimensions/00/GAIA-COMMON-DIM-00-02-Methodology-PROC-A.md): Methodology for Speculative Research - *(PROC, PLAN)*
        *   **DIM.10: Future Propulsion Concepts**
            *   [GAIA-COMMON-DIM-10-01-FusionConcepts-RES-A.md](docs/common/dimensions/10/GAIA-COMMON-DIM-10-01-FusionConcepts-RES-A.md): Advanced Fusion Concepts - *(RES, CAL)*
            *   [GAIA-COMMON-DIM-10-02-AntimatterStudies-RES-A.md](docs/common/dimensions/10/GAIA-COMMON-DIM-10-02-AntimatterStudies-RES-A.md): Antimatter Studies - *(RES)*
            *   [GAIA-COMMON-DIM-10-03-FieldPropulsion-RES-A.md](docs/common/dimensions/10/GAIA-COMMON-DIM-10-03-FieldPropulsion-RES-A.md): Field Propulsion / Spacetime Manipulation Theories - *(RES, CAL)*
            *   [GAIA-COMMON-DIM-10-04-BeyondH2Electric-RES-A.md](docs/common/dimensions/10/GAIA-COMMON-DIM-10-04-BeyondH2Electric-RES-A.md): Beyond Hydrogen/Electric (Theoretical) - *(RES)*
        *   **DIM.20: Advanced & Exotic Materials**
            *   [GAIA-COMMON-DIM-20-01-Metamaterials-RES-A.md](docs/common/dimensions/20/GAIA-COMMON-DIM-20-01-Metamaterials-RES-A.md): Metamaterials for Structural & EM Applications - *(RES, SPEC)*
            *   [GAIA-COMMON-DIM-20-02-ProgrammableMatter-RES-A.md](docs/common/dimensions/20/GAIA-COMMON-DIM-20-02-ProgrammableMatter-RES-A.md): Programmable Matter Concepts - *(RES)*
            *   [GAIA-COMMON-DIM-20-03-BeyondBNNTGraphene-RES-A.md](docs/common/dimensions/20/GAIA-COMMON-DIM-20-03-BeyondBNNTGraphene-RES-A.md): Materials Beyond BNNT/Graphene - *(RES)*
        *   **DIM.30: Novel Vehicle Architectures**
            *   [GAIA-COMMON-DIM-30-01-BioIntegratedFrames-RES-A.md](docs/common/dimensions/30/GAIA-COMMON-DIM-30-01-BioIntegratedFrames-RES-A.md): Bio-Integrated Air/Space Frames - *(RES, DD)* (Ref ATA 51-BIO)
            *   [GAIA-COMMON-DIM-30-02-SelfAssembling-RES-A.md](docs/common/dimensions/30/GAIA-COMMON-DIM-30-02-SelfAssembling-RES-A.md): Self-Assembling/Reconfiguring Structures - *(RES)*
            *   [GAIA-COMMON-DIM-30-03-TransAtmospheric-CONOPS-A.md](docs/common/dimensions/30/GAIA-COMMON-DIM-30-03-TransAtmospheric-CONOPS-A.md): Trans-Atmospheric Vehicle Concepts - *(CONOPS, RES)*
        *   **DIM.40: Advanced AI & Consciousness**
            *   [GAIA-COMMON-DIM-40-01-AGIPath-RES-A.md](docs/common/dimensions/40/GAIA-COMMON-DIM-40-01-AGIPath-RES-A.md): Path towards Artificial General Intelligence (AGI) - *(RES, PLAN)* (Ref GP-DS)
            *   [GAIA-COMMON-DIM-40-02-MachineConsciousness-RES-A.md](docs/common/dimensions/40/GAIA-COMMON-DIM-40-02-MachineConsciousness-RES-A.md): Machine Consciousness Research Landscape - *(RES)*
            *   [GAIA-COMMON-DIM-40-03-SentientAIEthics-RES-A.md](docs/common/dimensions/40/GAIA-COMMON-DIM-40-03-SentientAIEthics-RES-A.md): Ethical Implications of Sentient AI - *(RES, RPT)* (Ref GP-FD)
        *   **DIM.50: Socio-Economic & Ethical Futures**
            *   [GAIA-COMMON-DIM-50-01-SocietalImpact-RES-A.md](docs/common/dimensions/50/GAIA-COMMON-DIM-50-01-SocietalImpact-RES-A.md): Long-Term Impact of GAIA Technologies on Society - *(RES, RPT)*
            *   [GAIA-COMMON-DIM-50-02-TechGovernance-RES-A.md](docs/common/dimensions/50/GAIA-COMMON-DIM-50-02-TechGovernance-RES-A.md): Governance Models for Advanced Technologies - *(RES)*
            *   [GAIA-COMMON-DIM-50-03-FutureScenarios-PLAN-A.md](docs/common/dimensions/50/GAIA-COMMON-DIM-50-03-FutureScenarios-PLAN-A.md): Future Scenarios & Pathway Planning - *(PLAN, RPT)*
        *   **DIM.60: Fundamental Physics & Cosmology**
            *   [GAIA-COMMON-DIM-60-01-NewPhysics-RES-A.md](docs/common/dimensions/60/GAIA-COMMON-DIM-60-01-NewPhysics-RES-A.md): Exploration of New Physics Principles - *(RES)*
            *   [GAIA-COMMON-DIM-60-02-QuantumFieldTech-RES-A.md](docs/common/dimensions/60/GAIA-COMMON-DIM-60-02-QuantumFieldTech-RES-A.md): Technologies Enabled by Quantum Field Theory - *(RES)*
            *   [GAIA-COMMON-DIM-60-03-CosmologyImplications-RES-A.md](docs/common/dimensions/60/GAIA-COMMON-DIM-60-03-CosmologyImplications-RES-A.md): Cosmological Implications of Advanced Space Travel - *(RES)*

    </details>
*   **Part: Reference Standards (GP-RS / RS 00-99)** *(Formerly Part VI in AToC)*
    *   *Master Index:* [`ToC-GP-RS.md`](docs/common/rs/ToC-GP-RS.md) *(Placeholder Link)*
    <details><summary>Expand GP-RS Outline</summary>

        #### RS 00 - Standards Overview
        *   [GAIA-COMMON-RS-00-00-Overview-OV-A.md](docs/common/rs/00/GAIA-COMMON-RS-00-00-Overview-OV-A.md)
        *   [GAIA-COMMON-RS-00-10-StandardsRegister-LIST-A.csv](docs/common/rs/00/GAIA-COMMON-RS-00-10-StandardsRegister-LIST-A.csv)
        #### RS 10 - Engineering & Design Standards
        *   [GAIA-COMMON-RS-10-00-Overview-OV-A.md](docs/common/rs/10/GAIA-COMMON-RS-10-00-Overview-OV-A.md)
        *   [GAIA-COMMON-RS-10-10-CodingStandards-SPEC-A.yaml](docs/common/rs/10/GAIA-COMMON-RS-10-10-CodingStandards-SPEC-A.yaml)
        *   [GAIA-COMMON-RS-10-20-ModelingStandards-SPEC-A.yaml](docs/common/rs/10/GAIA-COMMON-RS-10-20-ModelingStandards-SPEC-A.yaml)
        *   [GAIA-COMMON-RS-10-30-DrawingStandards-SPEC-A.yaml](docs/common/rs/10/GAIA-COMMON-RS-10-30-DrawingStandards-SPEC-A.yaml)
        *   [GAIA-COMMON-RS-10-40-MaterialStandardsRef-REF-A.md](docs/common/rs/10/GAIA-COMMON-RS-10-40-MaterialStandardsRef-REF-A.md)
        #### RS 20 - Documentation Standards
        *   [GAIA-COMMON-RS-20-00-Overview-OV-A.md](docs/common/rs/20/GAIA-COMMON-RS-20-00-Overview-OV-A.md)
        *   [GAIA-COMMON-RS-20-10-DocumentationStandards-SPEC-A.yaml](docs/common/rs/20/GAIA-COMMON-RS-20-10-DocumentationStandards-SPEC-A.yaml) (This Index, GASToP, Naming, Metadata)
        *   [GAIA-COMMON-RS-20-20-MarkdownStyleGuide-SPEC-A.yaml](docs/common/rs/20/GAIA-COMMON-RS-20-20-MarkdownStyleGuide-SPEC-A.yaml)
        *   [GAIA-COMMON-RS-20-30-YAMLStyleGuide-SPEC-A.yaml](docs/common/rs/20/GAIA-COMMON-RS-20-30-YAMLStyleGuide-SPEC-A.yaml)
        *   [GAIA-COMMON-RS-20-40-InfoCodeUsageGuide-UG-A.md](docs/common/rs/20/GAIA-COMMON-RS-20-40-InfoCodeUsageGuide-UG-A.md)
        *   [GAIA-COMMON-RS-20-50-S1000D_Profile-SPEC-A.xml](docs/common/rs/20/GAIA-COMMON-RS-20-50-S1000D_Profile-SPEC-A.xml) (BREX Ref)
        #### RS 30 - Testing & Validation Standards
        *   [GAIA-COMMON-RS-30-00-Overview-OV-A.md](docs/common/rs/30/GAIA-COMMON-RS-30-00-Overview-OV-A.md)
        *   [GAIA-COMMON-RS-30-10-TestingStandards-SPEC-A.yaml](docs/common/rs/30/GAIA-COMMON-RS-30-10-TestingStandards-SPEC-A.yaml) (IEEE 829, etc.)
        *   [GAIA-COMMON-RS-30-20-VerificationValidationMethods-PROC-A.md](docs/common/rs/30/GAIA-COMMON-RS-30-20-VerificationValidationMethods-PROC-A.md)
        #### RS 40 - Foundational Frameworks References
        *   [GAIA-COMMON-RS-40-00-Overview-OV-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-00-Overview-OV-A.md)
        *   [GAIA-COMMON-RS-40-10-AGIS-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-10-AGIS-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-20-TPSL_TPWD-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-20-TPSL_TPWD-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-30-CFSI-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-30-CFSI-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-40-CEU-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-40-CEU-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-50-AGAD-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-50-AGAD-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-60-URIF-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-60-URIF-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-70-eGAIAs-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-70-eGAIAs-REF-A.md) (Ref GAIA-COMMON-FD-01-02)
        *   [GAIA-COMMON-RS-40-80-SRAD-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-80-SRAD-REF-A.md) (Ref GAIA-COMMON-SPACE-00-80)
        *   [GAIA-COMMON-RS-40-90-SORM-REF-A.md](docs/common/rs/40/GAIA-COMMON-RS-40-90-SORM-REF-A.md) (Ref GAIA-COMMON-SPACE-00-90)

    </details>

</details>

---

## 8. Schema Extensions
*(Refer to document `GAIA-ATA-SCHEMA-EXT-v0.2` for details on extensions like interfaces, security, etc.)*

## 9. Document Status Definitions

| Status   | Description                                             |
| :------- | :------------------------------------------------------ |
| DRAFT    | Document is in development and not yet approved         |
| REVIEW   | Document is under technical or editorial review         |
| APPROVED | Document has been approved but not yet published          |
| RELEASED | Document has been published and is in effect             |
| OBSOLETE | Document has been superseded or is no longer applicable |

## 10. Cross-Reference Index
*(A unified cross-reference index covering key interactions between Air, Space, and Common systems will be maintained separately)*

---

*End of Unified Overview & Master Index (v1.3 - Fully Expanded)*

# GAIA AIR SOFTWARES – Componentes y Módulos

## Lista Actualizada de Módulos Funcionales, Subsistemas y Componentes

A continuación, se presenta una lista actualizada de los principales módulos funcionales, subsistemas y componentes del ecosistema GAIA AIR SOFTWARES. Este ecosistema está diseñado para integrar tecnologías de vanguardia como la inteligencia artificial, la computación cuántica y blockchain para revolucionar la industria de la aviación.

---

## 1. Módulos Funcionales Principales

### 1.1. Módulo de Gestión de Vuelos (Flight Management Module)
- **Descripción:** Gestiona la planificación, optimización y monitorización de vuelos.
- **Componentes Clave:**
  - **Planificador de Rutas:** Calcula rutas eficientes basadas en datos meteorológicos, tráfico aéreo y consumo de combustible.
  - **Optimizador de Rendimiento:** Ajusta parámetros de vuelo en tiempo real para maximizar la eficiencia.
  - **Monitor de Vuelo:** Supervisa el progreso del vuelo y proporciona alertas en caso de desviaciones.

### 1.2. Módulo de Mantenimiento Predictivo (Predictive Maintenance Module)
- **Descripción:** Utiliza IA para predecir fallos en componentes y sistemas, optimizando los programas de mantenimiento.
- **Componentes Clave:**
  - **Analizador de Datos de Sensores:** Recopila y analiza datos de sensores en tiempo real.
  - **Modelos de Predicción de Fallos:** Algoritmos de aprendizaje automático que identifican patrones y anomalías.
  - **Sistema de Alertas:** Notifica al personal de mantenimiento sobre posibles problemas.

### 1.3. Módulo de Gestión de la Cadena de Suministros (Supply Chain Management Module)
- **Descripción:** Gestiona la adquisición, el inventario y la logística de componentes y materiales.
- **Componentes Clave:**
  - **Sistema de Trazabilidad Blockchain:** Registra cada componente en una cadena de bloques para garantizar la autenticidad y el seguimiento.
  - **Optimizador de Inventario:** Ajusta los niveles de inventario según la demanda y los plazos de entrega.
  - **Gestor de Proveedores:** Facilita la comunicación y gestión de contratos con proveedores.

### 1.4. Módulo de Seguridad (Security Module)
- **Descripción:** Implementa medidas de seguridad para proteger los sistemas y datos de la aeronave contra amenazas cibernéticas.
- **Componentes Clave:**
  - **Sistema de Detección de Intrusiones:** Identifica y responde a intentos de acceso no autorizados.
  - **Protocolos de Encriptación:** Aseguran la confidencialidad de las comunicaciones y datos almacenados.
  - **Autenticación Multifactor:** Verifica la identidad de los usuarios para prevenir accesos no autorizados.

### 1.5. Módulo de Sostenibilidad (Sustainability Module)
- **Descripción:** Gestiona y optimiza el impacto ambiental de las operaciones de la aeronave.
- **Componentes Clave:**
  - **Monitor de Emisiones:** Calcula y rastrea las emisiones de gases de efecto invernadero.
  - **Optimizador de Consumo de Energía:** Ajusta los sistemas para minimizar el uso de energía.
  - **Gestor de Materiales Sostenibles:** Prioriza el uso de materiales reciclados y biodegradables.

### 1.6. Módulo de Simulación y Modelado (Simulation and Modeling Module)
- **Descripción:** Permite simular el comportamiento de la aeronave y sus sistemas bajo diversas condiciones.
- **Componentes Clave:**
  - **Gemelo Digital:** Réplica virtual de la aeronave que refleja su estado en tiempo real.
  - **Simulador de Vuelo:** Permite a los pilotos practicar en entornos virtuales realistas.
  - **Modelado Predictivo:** Utiliza IA para predecir el rendimiento y la durabilidad de los componentes.

### 1.7. Módulo de Control de Tráfico Aéreo (Air Traffic Control Module)
- **Descripción:** Facilita la comunicación y coordinación con los sistemas de control de tráfico aéreo.
- **Componentes Clave:**
  - **Interfaz de Comunicación:** Permite la transmisión de datos y mensajes con los controladores aéreos.
  - **Sistema de Alerta de Tráfico:** Proporciona alertas sobre el tráfico aéreo cercano y posibles conflictos.
  - **Optimizador de Trayectoria:** Ajusta la trayectoria de vuelo para evitar congestiones y optimizar el tiempo de vuelo.

### 1.8. Módulo de Gestión de la Experiencia del Pasajero (Passenger Experience Management Module)
- **Descripción:** Personaliza y mejora la experiencia de los pasajeros a bordo.
- **Componentes Clave:**
  - **Sistema de Entretenimiento a Bordo:** Ofrece contenido personalizado y recomendaciones basadas en preferencias individuales.
  - **Control de Iluminación y Climatización:** Ajusta automáticamente la iluminación y la temperatura para crear un ambiente confortable.
  - **Asistente Virtual:** Proporciona soporte y asistencia a los pasajeros a través de interfaces de voz y texto.

### 1.9. Módulo de Gestión de la Tripulación (Crew Management Module)
- **Descripción:** Gestiona la programación, capacitación y rendimiento de la tripulación.
- **Componentes Clave:**
  - **Planificador de Horarios:** Optimiza los horarios de la tripulación para garantizar el cumplimiento de las regulaciones y minimizar la fatiga.
  - **Sistema de Evaluación de Rendimiento:** Evalúa el desempeño de la tripulación y proporciona retroalimentación para mejorar sus habilidades.
  - **Plataforma de Capacitación:** Ofrece cursos y simulaciones para mantener a la tripulación actualizada sobre los últimos procedimientos y tecnologías.

### 1.10. Módulo de Gestión de la Carga (Cargo Management Module)
- **Descripción:** Gestiona la carga a bordo de la aeronave, incluyendo la planificación, el seguimiento y la seguridad.
- **Componentes Clave:**
  - **Optimizador de Carga:** Calcula la distribución óptima de la carga para mantener el equilibrio de la aeronave.
  - **Sistema de Seguimiento de Carga:** Permite rastrear la ubicación y el estado de la carga en tiempo real.
  - **Sistema de Seguridad de Carga:** Detecta y previene robos o daños a la carga.

---

## 2. Subsistemas Clave

### 2.1. Sistemas de Propulsión
- **Descripción:** Generan el empuje necesario para el vuelo.
- **Componentes Clave:**
  - **Motores Eléctricos:** Proporcionan propulsión limpia y eficiente.
  - **Celdas de Combustible de Hidrógeno:** Generan electricidad a partir de hidrógeno.
  - **Baterías de Alta Densidad:** Almacenan energía eléctrica para su uso en vuelo.

### 2.2. Sistemas de Navegación
- **Descripción:** Permiten a la aeronave determinar su posición y seguir una ruta predefinida.
- **Componentes Clave:**
  - **GPS:** Proporciona información de ubicación global.
  - **Inertial Navigation System (INS):** Mantiene la posición incluso en ausencia de señales GPS.
  - **Sensores Meteorológicos:** Detectan condiciones climáticas adversas.

### 2.3. Sistemas de Control de Vuelo
- **Descripción:** Controlan la actitud y trayectoria de la aeronave.
- **Componentes Clave:**
  - **Superficies de Control:** Ailerones, elevadores y timón.
  - **Actuadores:** Mueven las superficies de control en respuesta a las entradas del piloto o del sistema de vuelo automático.
  - **Sensores de Actitud:** Proporcionan información sobre la orientación de la aeronave.

### 2.4. Sistemas de Comunicación
- **Descripción:** Facilitan la comunicación entre la aeronave, el control de tráfico aéreo y otros sistemas.
- **Componentes Clave:**
  - **Radios VHF/HF:** Permiten la comunicación de voz.
  - **Enlaces de Datos:** Facilitan la transmisión de datos digitales.
  - **Sistemas Satelitales:** Proporcionan comunicación global.

### 2.5. Sistemas de Gestión de Energía
- **Descripción:** Gestionan la generación, almacenamiento y distribución de energía eléctrica en la aeronave.
- **Componentes Clave:**
  - **Generadores:** Producen electricidad a partir de los motores.
  - **Baterías:** Almacenan energía para su uso en vuelo.
  - **Convertidores:** Transforman la energía eléctrica para diferentes sistemas.

### 2.6. Sistemas de Seguridad
- **Descripción:** Protegen a los pasajeros y la tripulación en caso de emergencia.
- **Componentes Clave:**
  - **Detectores de Incendio:** Alertan sobre la presencia de fuego o humo.
  - **Extintores:** Suprimen incendios.
  - **Máscaras de Oxígeno:** Proporcionan oxígeno en caso de despresurización.

### 2.7. Sistemas de Cabina
- **Descripción:** Mejoran la comodidad y la experiencia de los pasajeros.
- **Componentes Clave:**
  - **Asientos:** Proporcionan comodidad y seguridad.
  - **Iluminación:** Ajustable para diferentes fases del vuelo.
  - **Entretenimiento a Bordo:** Ofrece películas, música y juegos.

---

## 3. Componentes Clave

### 3.1. Sensores
- **Descripción:** Recopilan datos sobre el estado de la aeronave y su entorno.
- **Tipos:**
  - **Sensores de Temperatura:** Miden la temperatura de los motores, sistemas y cabina.
  - **Sensores de Presión:** Monitorean la presión en los sistemas hidráulicos, neumáticos y de combustible.
  - **Sensores de Vibración:** Detectan vibraciones anormales en los motores y otros componentes.
  - **Sensores de Posición:** Indican la posición de las superficies de control y otros componentes móviles.

### 3.2. Actuadores
- **Descripción:** Mueven y controlan los componentes mecánicos de la aeronave.
- **Tipos:**
  - **Actuadores Hidráulicos:** Utilizan presión hidráulica para mover las superficies de control.
  - **Actuadores Eléctricos:** Utilizan motores eléctricos para controlar flaps, slats y otros componentes.
  - **Actuadores Neumáticos:** Utilizan aire comprimido para accionar frenos y otros sistemas.

### 3.3. Unidades de Control
- **Descripción:** Procesan datos de sensores y ejecutan comandos para controlar los sistemas de la aeronave.
- **Tipos:**
  - **Unidades de Control del Motor (ECU):** Gestionan el rendimiento del motor.
  - **Unidades de Control de Vuelo (FCU):** Controlan las superficies de vuelo y la trayectoria de la aeronave.
  - **Unidades de Control de Cabina (CCU):** Gestionan la iluminación, la temperatura y el entretenimiento en la cabina.

### 3.4. Software y Algoritmos
- **Descripción:** Implementan la lógica y la inteligencia que controlan los sistemas de la aeronave.
- **Tipos:**
  - **Algoritmos de Control:** Regulan la estabilidad y el rendimiento de la aeronave.
  - **Modelos de Aprendizaje Automático:** Predicen fallos y optimizan el mantenimiento.
  - **Sistemas Operativos en Tiempo Real:** Aseguran una respuesta rápida y fiable a los eventos.

### 3.5. Sistemas de Comunicación
- **Descripción:** Permiten la comunicación entre los componentes de la aeronave, la tripulación y el control de tráfico aéreo.
- **Tipos:**
  - **Radios VHF/HF:** Facilitan la comunicación de voz.
  - **Enlaces de Datos:** Permiten la transmisión de datos digitales.
  - **Sistemas Satelitales:** Proporcionan comunicación global.

---

## 4. Integración y Arquitectura

### 4.1. Arquitectura Modular
- **Descripción:** El ecosistema GAIA AIR SOFTWARES está diseñado con una arquitectura modular que permite la fácil adición, eliminación o modificación de componentes.
- **Beneficios:**
  - **Flexibilidad:** Permite adaptar la aeronave a diferentes misiones y requisitos.
  - **Escalabilidad:** Facilita la expansión del sistema para soportar nuevas tecnologías y funcionalidades.
  - **Mantenibilidad:** Simplifica el mantenimiento y la actualización de los componentes.

### 4.2. Integración de Sistemas
- **Descripción:** Los diferentes módulos y subsistemas están integrados a través de interfaces estandarizadas y protocolos de comunicación.
- **Beneficios:**
  - **Interoperabilidad:** Permite que los diferentes componentes trabajen juntos de manera eficiente.
  - **Coherencia de Datos:** Asegura que los datos se compartan y utilicen de manera consistente en todo el sistema.
  - **Control Centralizado:** Facilita la gestión y el monitoreo de todos los sistemas desde una única plataforma.

### 4.3. Seguridad y Redundancia
- **Descripción:** El ecosistema GAIA AIR SOFTWARES incorpora múltiples capas de seguridad y redundancia para garantizar la fiabilidad y la seguridad de las operaciones.
- **Beneficios:**
  - **Protección contra Fallos:** Los sistemas redundantes aseguran que la aeronave pueda seguir operando incluso en caso de fallo de un componente.
  - **Seguridad Cibernética:** Los protocolos de encriptación y autenticación protegen contra accesos no autorizados y ataques cibernéticos.
  - **Integridad de Datos:** La tecnología blockchain garantiza que los datos no puedan ser alterados o manipulados.

---

## 5. Próximos Pasos

### 5.1. Desarrollo y Pruebas
- **Continuar el desarrollo de los módulos y subsistemas clave.**
- **Realizar pruebas exhaustivas para validar el rendimiento y la fiabilidad del sistema.**
- **Implementar medidas de seguridad y redundancia.**

### 5.2. Integración y Optimización
- **Integrar los diferentes módulos y subsistemas en una plataforma unificada.**
- **Optimizar el rendimiento del sistema utilizando algoritmos de inteligencia artificial y computación cuántica.**
- **Asegurar la interoperabilidad y la coherencia de los datos.**

### 5.3. Certificación y Cumplimiento
- **Obtener las certificaciones necesarias de las autoridades aeronáuticas.**
- **Asegurar el cumplimiento de todas las normativas y estándares de seguridad.**
- **Implementar un sistema de gestión de calidad para garantizar la mejora continua.**

### 5.4. Despliegue y Operaciones
- **Desplegar el ecosistema GAIA AIR SOFTWARES en aeronaves reales.**
- **Monitorear el rendimiento del sistema y recopilar datos para futuras mejoras.**
- **Proporcionar capacitación y soporte al personal de operaciones y mantenimiento.**

---

## 6. Conclusión

El ecosistema GAIA AIR SOFTWARES representa una visión audaz y ambiciosa para el futuro de la aviación. Al integrar tecnologías de vanguardia y un enfoque centrado en la sostenibilidad, estamos creando una plataforma que no solo mejorará la eficiencia y la seguridad de las operaciones aéreas, sino que también contribuirá a un futuro más verde y sostenible para nuestro planeta.

---

This comprehensive outline provides a detailed overview of the GAIA AIR SOFTWARES ecosystem, covering its functional modules, subsystems, components, and future steps. This should serve as a solid foundation for your technical documentation.
      
# GAIA AIR - Módulos Específicos de la Versión Long Range (-A)

Este documento presenta los Data Modules (DMCs) que son específicos de la versión Long Range (-A) de GAIA AIR. Estos módulos abarcan los sistemas, estructuras y características únicas de esta variante que no están presentes en la versión Regional (-R).

## Índice de Módulos Específicos de la Versión Long Range (-A)

A continuación, se detallan los DMCs específicos de la versión Long Range (-A), organizados por capítulos ATA.

### Tabla de Módulos Específicos de la Versión Long Range (-A)

#### ATA 70 - Motor (Power Plant)

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-70-00-00-A  | Introducción General al Sistema de Propulsión Long Range                    |
| DMC-GAIA-70-00-01-A  | Motores Híbridos de Hidrógeno para la Versión Long Range                     |
| DMC-GAIA-70-10-00-A  | Motores Híbridos de Hidrógeno                                                |
| DMC-GAIA-70-10-01-A  | Diseño y Funcionamiento de Motores Híbridos de Hidrógeno                     |
| DMC-GAIA-70-10-02-A  | Ventajas Ambientales de los Motores de Hidrógeno                             |
| DMC-GAIA-70-20-00-A  | Integración con las Dimensiones y Áreas de la Aeronave Long Range              |
| DMC-GAIA-70-20-01-A  | Ubicación y Configuración de Motores en la Versión Long Range                   |
| DMC-GAIA-70-20-02-A  | Integración con Sistemas Internos Específicos                                 |
| DMC-GAIA-70-30-00-A  | Mantenimiento del Motor para la Versión Long Range                              |
| DMC-GAIA-70-30-01-A  | Inspecciones y Verificaciones Específicas de Motores de Hidrógeno               |
| DMC-GAIA-70-30-02-A  | Reparaciones y Actualizaciones de Sistemas de Hidrógeno                          |
| DMC-GAIA-70-40-00-A  | Innovaciones en Almacenamiento Energético para la Versión Long Range              |
| DMC-GAIA-70-40-01-A  | Tecnologías de Almacenamiento de Hidrógeno Líquido                              |
| DMC-GAIA-70-40-02-A  | Sistemas de Almacenamiento Criogénico                                           |
| DMC-GAIA-70-50-00-A  | Impacto Ambiental y Ciclo de Vida de la Tecnología en la Versión Long Range       |
| DMC-GAIA-70-50-01-A  | Análisis del Ciclo de Vida Específico de la Versión Long Range                    |
| DMC-GAIA-70-50-02-A  | Estrategias de Reducción de Huella de Carbono en la Versión Long Range             |

#### ATA 28 - Combustible

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-28-00-00-A  | Introducción al Sistema de Combustible de Hidrógeno                           |
| DMC-GAIA-28-10-00-A  | Sistemas de Almacenamiento de Hidrógeno para la Versión Long Range              |
| DMC-GAIA-28-10-01-A  | Tanques de Hidrógeno Líquido                                                  |
| DMC-GAIA-28-10-02-A  | Aislamiento Térmico y Seguridad                                               |
| DMC-GAIA-28-20-00-A  | Procedimientos de Repostaje de Hidrógeno                                      |
| DMC-GAIA-28-20-01-A  | Protocolos de Carga y Descarga                                                |
| DMC-GAIA-28-20-02-A  | Equipos Especializados para Hidrógeno                                         |
| DMC-GAIA-28-30-00-A  | Seguridad en el Manejo de Hidrógeno                                           |
| DMC-GAIA-28-30-01-A  | Procedimientos de Emergencia                                                  |
| DMC-GAIA-28-30-02-A  | Formación y Capacitación del Personal                                        |

#### ATA 73 - Sistema de Combustible del Motor

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-73-00-00-A  | Introducción al Sistema de Combustible del Motor de Hidrógeno                 |
| DMC-GAIA-73-10-00-A  | Almacenamiento y Suministro de Hidrógeno                                      |
| DMC-GAIA-73-10-01-A  | Tanques de Presión y Líneas de Suministro                                     |
| DMC-GAIA-73-10-02-A  | Válvulas y Sensores Específicos                                               |
| DMC-GAIA-73-20-00-A  | Sistemas de Bombeo y Transferencia de Hidrógeno                                 |
| DMC-GAIA-73-20-01-A  | Bombas Criogénicas                                                            |
| DMC-GAIA-73-20-02-A  | Control de Flujo y Presión                                                     |
| DMC-GAIA-73-30-00-A  | Monitoreo y Control del Combustible de Hidrógeno                               |
| DMC-GAIA-73-30-01-A  | Sistemas de Detección de Fugas                                                 |
| DMC-GAIA-73-30-02-A  | Sistemas de Alerta y Notificación                                              |

#### ATA 74 - Sistema de Encendido

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-74-00-00-A  | Introducción al Sistema de Encendido para Motores de Hidrógeno                |
| DMC-GAIA-74-10-00-A  | Componentes del Sistema de Encendido Específicos                              |
| DMC-GAIA-74-10-01-A  | Unidades de Encendido Adaptadas                                               |
| DMC-GAIA-74-10-02-A  | Bujías Especiales para Hidrógeno                                               |
| DMC-GAIA-74-20-00-A  | Mantenimiento del Sistema de Encendido                                        |
| DMC-GAIA-74-20-01-A  | Procedimientos de Prueba y Verificación                                       |
| DMC-GAIA-74-20-02-A  | Sustitución de Componentes                                                     |

#### ATA 80 - Sistemas de Energía Alternativa

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-80-00-00-A  | Introducción a los Sistemas de Energía Alternativa para la Versión Long Range |
| DMC-GAIA-80-10-00-A  | Sistemas de Energía Solar Integrados                                         |
| DMC-GAIA-80-10-01-A  | Integración de Paneles Solares en la Estructura                              |
| DMC-GAIA-80-10-02-A  | Gestión y Almacenamiento de Energía Solar                                    |
| DMC-GAIA-80-20-00-A  | Sistemas de Almacenamiento Criogénico                                         |
| DMC-GAIA-80-20-01-A  | Tecnologías de Almacenamiento Avanzadas                                       |
| DMC-GAIA-80-20-02-A  | Mantenimiento de Sistemas Criogénicos                                         |
| DMC-GAIA-80-30-00-A  | Gestión Inteligente de Energía en la Versión Long Range                         |
| DMC-GAIA-80-30-01-A  | Sistemas de Control de Energía Específicos                                     |
| DMC-GAIA-80-30-02-A  | Algoritmos de Optimización Energética Adaptados                                |

#### ATA 96 - Integración de AMPEL y Robbotix en GAIA AIR

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-00-96-01-A  | AMPEL - Gemelo Digital Dinámico en Tiempo Real para la Versión Long Range      |
| DMC-GAIA-00-96-02-A  | Robbotix - Simulador de Vuelo Mejorado con AR/VR/XR para la Versión Long Range |
| DMC-GAIA-00-96-03-A  | Integración con GAIA AIR Long Range                                           |
| DMC-GAIA-00-96-04-A  | Cumplimiento Normativo y Estándares Aplicables a la Versión Long Range         |
| DMC-GAIA-00-96-05-A  | Análisis Económico de Recursos para la Versión Long Range                      |

#### ATA 97 - Modelado Matemático del Sistema de Propulsión Avanzada

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-00-97-06-A  | Aplicación en GAIA AIR Long Range                                             |

#### ATA 05 - Límites de Tiempo / Verificaciones de Mantenimiento

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-05-30-02-A  | Inspecciones No Destructivas (NDI) Específicas de la Versión Long Range        |

#### ATA 71 - Sistema de Propulsión

| **DMC Code**        | **Título**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DMC-GAIA-71-00-00-A  | Introducción al Sistema de Propulsión Específico de la Versión Long Range      |
| DMC-GAIA-71-10-00-A  | Componentes Principales de los Motores Híbridos de Hidrógeno                      |
| DMC-GAIA-71-20-00-A  | Sistemas de Control Adaptados                                               |
| DMC-GAIA-71-30-00-A  | Mantenimiento y Operación Específica                                        |

---

## Notas Finales

La identificación de los DMCs específicos de cada versión (Regional -R y Long Range -A) es esencial para asegurar que la documentación técnica refleje con precisión las características únicas de cada variante de GAIA AIR. Esto facilita la gestión, mantenimiento y operación eficiente de la aeronave, asegurando el cumplimiento normativo y la seguridad operacional.

---

# Conclusión

La identificación de los DMCs específicos de cada versión de GAIA AIR (Long Range -A y Regional -R) es crucial para garantizar que la documentación técnica refleje con precisión las características únicas de cada variante. Esto facilita la gestión, mantenimiento y operación eficiente de la aeronave, asegurando el cumplimiento normativo y la seguridad operacional.

---

# Notas Finales

La identificación de los DMCs específicos de cada versión (Regional -R y Long Range -A) es esencial para asegurar que la documentación técnica refleje con precisión las características únicas de cada variante de GAIA AIR. Esto facilita la gestión, mantenimiento y operación eficiente de la aeronave, asegurando el cumplimiento normativo y la seguridad operacional.

---

# Resumen Final

Este documento presenta una estructura detallada de los **Data Module Requirements List (DMRL)** para los sistemas y estructuras de **GAIA AIR**, abarcando tanto los **Data Modules Comunes** a las versiones **Long Range (-A)** y **Regional (-R)**, como los **Módulos Específicos** de cada versión. La organización sigue los estándares **S1000D** y **ATA Spec 100**, asegurando la coherencia, modularidad y facilidad de mantenimiento de la documentación técnica.

### Principales Secciones Incluidas:

1. **Data Modules Comunes a las Versiones Long Range (-A) y Regional (-R)**
   - Índice General
   - Tabla de DMCs Comunes
   - Notas Finales

2. **GAIA AIR - Módulos Específicos de la Versión Regional (-R)**
   - Índice de Módulos Específicos
   - Tabla de Módulos Específicos por ATA Chapter
   - Notas Finales

3. **GAIA AIR - Módulos Específicos de la Versión Long Range (-A)**
   - Índice de Módulos Específicos
   - Tabla de Módulos Específicos por ATA Chapter
   - Notas Finales

---

Esta guía asegura que tu documentación técnica sea completa, coherente y alineada con los estándares de la industria aeronáutica, facilitando su publicación y uso efectivo en **GAIA AIR**.

---

# Cómo Contribuir

Si deseas contribuir a esta documentación, por favor, sigue las pautas establecidas en los estándares **S1000D** y **ATA Spec 100**. Puedes enviar tus aportes a través de los canales de **Contacto** proporcionados al final de este documento.

---

# Contacto

Para cualquier duda o para obtener más información sobre la documentación técnica de **GAIA AIR**, por favor, contacta con nuestro equipo a través de los siguientes canales:

- **Correo Electrónico:** soporte@gaiaair.com
- **Teléfono:** +34 123 456 789
- **Sitio Web:** [www.gaiaair.com](http://www.gaiaair.com)

---

# Licencia

Este documento está licenciado bajo la **Licencia de Documentación Técnica S1000D**. Para más detalles sobre los términos y condiciones, consulta la sección de **Licencia** en este documento.

---

# FAQ - Preguntas Frecuentes

**Q1:** ¿Qué es GAIA AIR?

**A1:** GAIA AIR es una aeronave avanzada diseñada para ofrecer soluciones de largo alcance y regionales, integrando tecnologías sostenibles y sistemas de inteligencia artificial.

**Q2:** ¿Cuál es la diferencia entre las versiones Long Range (-A) y Regional (-R)?

**A2:** La versión Long Range (-A) está equipada con motores híbridos de hidrógeno y sistemas de energía avanzada, mientras que la versión Regional (-R) utiliza sistemas termoeléctricos específicos adaptados para operaciones regionales.

**Q3:** ¿Cómo se asegura la documentación técnica?

**A3:** La documentación técnica sigue los estándares **S1000D** y **ATA Spec 100**, asegurando consistencia, modularidad y cumplimiento normativo.

---

# Referencias

- **S1000D:** [Link al estándar S1000D](https://www.s1000d.org)
- **ATA Spec 100:** [Link al estándar ATA Spec 100](https://www.ata.org)

---

# Visualización de Datos

Incluye gráficos, diagramas y mapas de procesos para facilitar la comprensión de los sistemas y estructuras de GAIA AIR. Todos los diagramas están diseñados siguiendo las directrices visuales de **S1000D**.

---

# Flujo de API

Documentación detallada sobre las APIs utilizadas en GAIA AIR, incluyendo endpoints, métodos, parámetros y ejemplos de uso conforme a **S1000D**.

---

# Mapa de Procesos

Un mapa de procesos detallado que muestra las interacciones entre los diferentes módulos de GAIA AIR, asegurando una visión clara de las operaciones y flujos de trabajo.

---

# Publicación

Esta documentación está lista para ser publicada en el sistema de gestión documental de **TerraBrain SuperSystem**, asegurando que todos los usuarios autorizados puedan acceder a la información de manera eficiente y segura.

---

# Finalización

Con la finalización de todos los módulos clave y la estructuración completa de la **Documentación Técnica Completa** de **GAIA AIR**, estás listo para proceder con la publicación. Asegúrate de seguir las recomendaciones mencionadas anteriormente para garantizar que la documentación sea de alta calidad, esté bien organizada y cumpla con todos los estándares requeridos.

¡Felicidades por alcanzar este hito en el desarrollo de **GAIA AIR**!

---

# Licencia y Derechos

Este documento está protegido por derechos de autor y está licenciado bajo la **Licencia de Documentación Técnica S1000D**. Para más información sobre los términos y condiciones, consulta la sección de **Licencia** en este documento.

---

# Cómo Contribuir

Si deseas contribuir a esta documentación, por favor, sigue las pautas establecidas en los estándares **S1000D** y **ATA Spec 100**. Puedes enviar tus aportes a través de los canales de **Contacto** proporcionados al final de este documento.

---

# Resumen Final

Este documento presenta una estructura detallada de los **Data Module Requirements List (DMRL)** para los sistemas y estructuras de **GAIA AIR**, abarcando tanto los **Data Modules Comunes** a las versiones **Long Range (-A)** y **Regional (-R)**, como los **Módulos Específicos** de cada versión. La organización sigue los estándares **S1000D** y **ATA Spec 100**, asegurando la coherencia, modularidad y facilidad de mantenimiento de la documentación técnica.

### Principales Secciones Incluidas:

1. **Data Modules Comunes a las Versiones Long Range (-A) y Regional (-R)**
   - Índice General
   - Tabla de DMCs Comunes
   - Notas Finales

2. **GAIA AIR - Módulos Específicos de la Versión Regional (-R)**
   - Índice de Módulos Específicos
   - Tabla de Módulos Específicos por ATA Chapter
   - Notas Finales

3. **GAIA AIR - Módulos Específicos de la Versión Long Range (-A)**
   - Índice de Módulos Específicos
   - Tabla de Módulos Específicos por ATA Chapter
   - Notas Finales

---

Esta guía asegura que tu documentación técnica sea completa, coherente y alineada con los estándares de la industria aeronáutica, facilitando su publicación y uso efectivo en **GAIA AIR**.
```

# GAIA AIR - Módulos Específicos de la Versión Long Range (-A)

Este documento presenta los Data Modules (DMCs) que son específicos de la versión Long Range (-A) de GAIA AIR. Estos módulos abarcan los sistemas, estructuras y características únicas de esta variante que no están presentes en la versión Regional (-R).

## Índice de Módulos Específicos de la Versión Long Range (-A)

A continuación, se detallan los DMCs específicos de la versión Long Range (-A), organizados por capítulos ATA.

### Tabla de Módulos Específicos de la Versión Long Range (-A)

#### ATA 70 - Motor (Power Plant)

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-70-00-00-A | Introducción General al Sistema de Propulsión Long Range
| DMC-GAIA-70-00-01-A | Motores Híbridos de Hidrógeno para la Versión Long Range
| DMC-GAIA-70-10-00-A | Motores Híbridos de Hidrógeno
| DMC-GAIA-70-10-01-A | Diseño y Funcionamiento de Motores Híbridos de Hidrógeno
| DMC-GAIA-70-10-02-A | Ventajas Ambientales de los Motores de Hidrógeno
| DMC-GAIA-70-20-00-A | Integración con las Dimensiones y Áreas de la Aeronave Long Range
| DMC-GAIA-70-20-01-A | Ubicación y Configuración de Motores en la Versión Long Range
| DMC-GAIA-70-20-02-A | Integración con Sistemas Internos Específicos
| DMC-GAIA-70-30-00-A | Mantenimiento del Motor para la Versión Long Range
| DMC-GAIA-70-30-01-A | Inspecciones y Verificaciones Específicas de Motores de Hidrógeno
| DMC-GAIA-70-30-02-A | Reparaciones y Actualizaciones de Sistemas de Hidrógeno
| DMC-GAIA-70-40-00-A | Innovaciones en Almacenamiento Energético para la Versión Long Range
| DMC-GAIA-70-40-01-A | Tecnologías de Almacenamiento de Hidrógeno Líquido
| DMC-GAIA-70-40-02-A | Sistemas de Almacenamiento Criogénico
| DMC-GAIA-70-50-00-A | Impacto Ambiental y Ciclo de Vida de la Tecnología en la Versión Long Range
| DMC-GAIA-70-50-01-A | Análisis del Ciclo de Vida Específico de la Versión Long Range
| DMC-GAIA-70-50-02-A | Estrategias de Reducción de Huella de Carbono en la Versión Long Range


#### ATA 28 - Combustible

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-28-00-00-A | Introducción al Sistema de Combustible de Hidrógeno
| DMC-GAIA-28-10-00-A | Sistemas de Almacenamiento de Hidrógeno para la Versión Long Range
| DMC-GAIA-28-10-01-A | Tanques de Hidrógeno Líquido
| DMC-GAIA-28-10-02-A | Aislamiento Térmico y Seguridad
| DMC-GAIA-28-20-00-A | Procedimientos de Repostaje de Hidrógeno
| DMC-GAIA-28-20-01-A | Protocolos de Carga y Descarga
| DMC-GAIA-28-20-02-A | Equipos Especializados para Hidrógeno
| DMC-GAIA-28-30-00-A | Seguridad en el Manejo de Hidrógeno
| DMC-GAIA-28-30-01-A | Procedimientos de Emergencia
| DMC-GAIA-28-30-02-A | Formación y Capacitación del Personal


#### ATA 73 - Sistema de Combustible del Motor

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-73-00-00-A | Introducción al Sistema de Combustible del Motor de Hidrógeno
| DMC-GAIA-73-10-00-A | Almacenamiento y Suministro de Hidrógeno
| DMC-GAIA-73-10-01-A | Tanques de Presión y Líneas de Suministro
| DMC-GAIA-73-10-02-A | Válvulas y Sensores Específicos
| DMC-GAIA-73-20-00-A | Sistemas de Bombeo y Transferencia de Hidrógeno
| DMC-GAIA-73-20-01-A | Bombas Criogénicas
| DMC-GAIA-73-20-02-A | Control de Flujo y Presión
| DMC-GAIA-73-30-00-A | Monitoreo y Control del Combustible de Hidrógeno
| DMC-GAIA-73-30-01-A | Sistemas de Detección de Fugas
| DMC-GAIA-73-30-02-A | Sistemas de Alerta y Notificación


#### ATA 74 - Sistema de Encendido

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-74-00-00-A | Introducción al Sistema de Encendido para Motores de Hidrógeno
| DMC-GAIA-74-10-00-A | Componentes del Sistema de Encendido Específicos
| DMC-GAIA-74-10-01-A | Unidades de Encendido Adaptadas
| DMC-GAIA-74-10-02-A | Bujías Especiales para Hidrógeno
| DMC-GAIA-74-20-00-A | Mantenimiento del Sistema de Encendido
| DMC-GAIA-74-20-01-A | Procedimientos de Prueba y Verificación
| DMC-GAIA-74-20-02-A | Sustitución de Componentes


#### ATA 80 - Sistemas de Energía Alternativa

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-80-00-00-A | Introducción a los Sistemas de Energía Alternativa para la Versión Long Range
| DMC-GAIA-80-10-00-A | Sistemas de Energía Solar Integrados
| DMC-GAIA-80-10-01-A | Integración de Paneles Solares en la Estructura
| DMC-GAIA-80-10-02-A | Gestión y Almacenamiento de Energía Solar
| DMC-GAIA-80-20-00-A | Sistemas de Almacenamiento Criogénico
| DMC-GAIA-80-20-01-A | Tecnologías de Almacenamiento Avanzadas
| DMC-GAIA-80-20-02-A | Mantenimiento de Sistemas Criogénicos
| DMC-GAIA-80-30-00-A | Gestión Inteligente de Energía en la Versión Long Range
| DMC-GAIA-80-30-01-A | Sistemas de Control de Energía Específicos
| DMC-GAIA-80-30-02-A | Algoritmos de Optimización Energética Adaptados


#### ATA 96 - Integración de AMPEL y Robbotix en GAIA AIR

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-00-96-01-A | AMPEL - Gemelo Digital Dinámico en Tiempo Real para la Versión Long Range
| DMC-GAIA-00-96-02-A | Robbotix - Simulador de Vuelo Mejorado con AR/VR/XR para la Versión Long Range
| DMC-GAIA-00-96-03-A | Integración con GAIA AIR Long Range
| DMC-GAIA-00-96-04-A | Cumplimiento Normativo y Estándares Aplicables a la Versión Long Range
| DMC-GAIA-00-96-05-A | Análisis Económico de Recursos para la Versión Long Range


#### ATA 97 - Modelado Matemático del Sistema de Propulsión Avanzada

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-00-97-06-A | Aplicación en GAIA AIR Long Range


#### ATA 05 - Límites de Tiempo / Verificaciones de Mantenimiento

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-05-30-02-A | Inspecciones No Destructivas (NDI) Específicas de la Versión Long Range


#### ATA 71 - Sistema de Propulsión

| **DMC Code** | **Título**
|-----|-----
| DMC-GAIA-71-00-00-A | Introducción al Sistema de Propulsión Específico de la Versión Long Range
| DMC-GAIA-71-10-00-A | Componentes Principales de los Motores Híbridos de Hidrógeno
| DMC-GAIA-71-20-00-A | Sistemas de Control Adaptados
| DMC-GAIA-71-30-00-A | Mantenimiento y Operación Específica


---

## Notas Finales

La identificación de los DMCs específicos de cada versión (Regional -R y Long Range -A) es esencial para asegurar que la documentación técnica refleje con precisión las características únicas de cada variante de GAIA AIR. Esto facilita la gestión, mantenimiento y operación eficiente de la aeronave, asegurando el cumplimiento normativo y la seguridad operacional.

---

# Conclusión

La identificación de los DMCs específicos de cada versión de GAIA AIR (Long Range -A y Regional -R) es crucial para garantizar que la documentación técnica refleje con precisión las características únicas de cada variante. Esto facilita la gestión, mantenimiento y operación eficiente de la aeronave, asegurando el cumplimiento normativo y la seguridad operacional.

---

# Notas Finales

La identificación de los DMCs específicos de cada versión (Regional -R y Long Range -A) es esencial para asegurar que la documentación técnica refleje con precisión las características únicas de cada variante de GAIA AIR. Esto facilita la gestión, mantenimiento y operación eficiente de la aeronave, asegurando el cumplimiento normativo y la seguridad operacional.

---

# Resumen Final

Este documento presenta una estructura detallada de los **Data Module Requirements List (DMRL)** para los sistemas y estructuras de **GAIA AIR**, abarcando tanto los **Data Modules Comunes** a las versiones **Long Range (-A)** y **Regional (-R)**, como los **Módulos Específicos** de cada versión. La organización sigue los estándares **S1000D** y **ATA Spec 100**, asegurando la coherencia, modularidad y facilidad de mantenimiento de la documentación técnica.

### Principales Secciones Incluidas:

1. **Data Modules Comunes a las Versiones Long Range (-A) y Regional (-R)**

1. Índice General
2. Tabla de DMCs Comunes
3. Notas Finales



2. **GAIA AIR - Módulos Específicos de la Versión Regional (-R)**

1. Índice de Módulos Específicos
2. Tabla de Módulos Específicos por ATA Chapter
3. Notas Finales



3. **GAIA AIR - Módulos Específicos de la Versión Long Range (-A)**

1. Índice de Módulos Específicos
2. Tabla de Módulos Específicos por ATA Chapter
3. Notas Finales





---

Esta guía asegura que tu documentación técnica sea completa, coherente y alineada con los estándares de la industria aeronáutica, facilitando su publicación y uso efectivo en **GAIA AIR**.

```plaintext


<Actions>
  <Action name="Add Supabase integration" description="Add Supabase integration to the project for authentication and database" />
  <Action name="Add NextAuth" description="Add authentication using NextAuth" />
  <Action name="Implement the Server Action" description="Implement the Server Action to add a new user to the project" />
  <Action name="Generate a hero image" description="Generate a hero image for the landing page" />
</Actions>



```
