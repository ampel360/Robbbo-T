# AMPEL360XWLRGA
# Measurement Point Definitions Table

**Document ID:** GP-AM-EDR-06-006
**Revision:** A
**Date:** 2025-03-21
**Classification:** Internal / Restricted
**Status:** Draft

## Table of Contents
1. [Introduction](#1-introduction)
2. [Measurement Point Classification](#2-measurement-point-classification)
3. [Primary Structure Measurement Points](#3-primary-structure-measurement-points)
4. [Secondary Structure Measurement Points](#4-secondary-structure-measurement-points)
5. [Systems Installation Measurement Points](#5-systems-installation-measurement-points)
6. [Interior Installation Measurement Points](#6-interior-installation-measurement-points)
7. [Measurement Point Usage Guidelines](#7-measurement-point-usage-guidelines)
8. [References](#8-references)

## 1. Introduction
### 1.1 Purpose
This document defines the standard measurement points for the AMPEL360XWLRGA aircraft. It establishes a comprehensive set of reference points used for manufacturing, assembly, inspection, and maintenance activities. These measurement points provide a common reference system for dimensional control throughout the aircraft's lifecycle.

### 1.2 Scope
This document covers all defined measurement points on the AMPEL360XWLRGA aircraft. It includes points on primary and secondary structure, systems installations, and interior components. The document specifies the location, purpose, and tolerance requirements for each measurement point, as well as guidelines for their use in various activities.

### 1.3 Applicable Documents
- Dimensional Data Report (GP-AM-EDR-06-001)
- Calibration & Measurement Procedures Document (GP-AM-EDR-06-002)
- Structural Integration Analysis Report (GP-AM-EDR-06-003)
- Internal Compartment Layout Document (GP-AM-EDR-06-004)
- Detailed Dimensions and Volume Calculation Report (GP-AM-EDR-06-005)
- Cross-Reference Diagram for Measurement Points (GP-AM-DRW-06-007)

## 2. Measurement Point Classification
### 2.1 Classification System
Measurement points are classified according to the following system:

| Classification | Prefix | Description | Typical Tolerance | Usage |
|----------------|--------|-------------|-------------------|-------|
| Primary Structure | PS | Critical structural reference points | ±0.2 mm | Manufacturing, assembly, major repairs |
| Secondary Structure | SS | Secondary structural reference points | ±0.5 mm | Assembly, component installation |
| Systems | SY | Systems installation reference points | ±1.0 mm | Systems installation, maintenance |
| Interior | IN | Interior installation reference points | ±2.0 mm | Interior installation, configuration changes |
| Tooling | TL | Tooling and jig reference points | ±0.1 mm | Manufacturing, assembly |
| Maintenance | MX | Maintenance reference points | ±1.0 mm | Maintenance, repair, inspection |

### 2.2 Identification System
Each measurement point is identified by a unique code with the following format:
Where:
- **AAA**: Classification prefix (PS, SS, SY, IN, TL, MX)
- **BBBB**: Sequential number within classification
- **CCC**: Location code (L=Left, R=Right, C=Center)

Example: PS-0012-R indicates Primary Structure point #0012 on the right side of the aircraft.

### 2.3 Measurement Point Types
#### 2.3.1 Physical Markers
- **Tooling Holes:** Precision holes used for tool alignment
- **Bushings:** Installed precision bushings with known coordinates
- **Targets:** Permanently installed measurement targets
- **Engraved Marks:** Precision engraved reference marks
- **Surface Features:** Defined features on component surfaces

#### 2.3.2 Virtual Points
- **Derived Points:** Points calculated from physical measurements
- **Constructed Points:** Points defined by geometric construction
- **Theoretical Points:** Points defined by design but not physically marked

## 3. Primary Structure Measurement Points
### 3.1 Fuselage Primary Structure Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| PS-0001-C | Forward Pressure Bulkhead Center | (350, 0, 250) | ±0.2 mm | Tooling Hole | 10 mm diameter hole |
| PS-0002-C | Aft Pressure Bulkhead Center | (2100, 0, 250) | ±0.2 mm | Tooling Hole | 10 mm diameter hole |
| PS-0003-L | Forward Door Frame Reference | (650, -290, 250) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| PS-0004-R | Forward Door Frame Reference | (650, 290, 250) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| PS-0005-L | Aft Door Frame Reference | (1800, -290, 250) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| PS-0006-R | Aft Door Frame Reference | (1800, 290, 250) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| PS-0007-C | Forward Floor Beam Reference | (500, 0, 100) | ±0.3 mm | Tooling Hole | 10 mm diameter hole |
| PS-0008-C | Mid Floor Beam Reference | (1200, 0, 100) | ±0.3 mm | Tooling Hole | 10 mm diameter hole |
| PS-0009-C | Aft Floor Beam Reference | (1900, 0, 100) | ±0.3 mm | Tooling Hole | 10 mm diameter hole |
| PS-0010-L | Frame 20 Reference | (800, -290, 250) | ±0.3 mm | Target | 15 mm diameter target |
| PS-0011-R | Frame 20 Reference | (800, 290, 250) | ±0.3 mm | Target | 15 mm diameter target |
| PS-0012-L | Frame 35 Reference | (1400, -290, 250) | ±0.3 mm | Target | 15 mm diameter target |
| PS-0013-R | Frame 35 Reference | (1400, 290, 250) | ±0.3 mm | Target | 15 mm diameter target |
| PS-0014-L | Frame 50 Reference | (2000, -290, 250) | ±0.3 mm | Target | 15 mm diameter target |
| PS-0015-R | Frame 50 Reference | (2000, 290, 250) | ±0.3 mm | Target | 15 mm diameter target |

### 3.2 Wing Primary Structure Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| PS-0101-L | Wing Front Spar/Fuselage Intersection | (1150, -250, 200) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0102-R | Wing Front Spar/Fuselage Intersection | (1150, 250, 200) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0103-L | Wing Rear Spar/Fuselage Intersection | (1350, -250, 200) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0104-R | Wing Rear Spar/Fuselage Intersection | (1350, 250, 200) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0105-L | Wing Front Spar at BL 500 | (1200, -500, 220) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0106-R | Wing Front Spar at BL 500 | (1200, 500, 220) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0107-L | Wing Rear Spar at BL 500 | (1400, -500, 220) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0108-R | Wing Rear Spar at BL 500 | (1400, 500, 220) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0109-L | Wing Front Spar at BL 1000 | (1250, -1000, 250) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0110-R | Wing Front Spar at BL 1000 | (1250, 1000, 250) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0111-L | Wing Rear Spar at BL 1000 | (1450, -1000, 250) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0112-R | Wing Rear Spar at BL 1000 | (1450, 1000, 250) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0113-L | Wing Tip Reference | (1350, -2600, 300) | ±0.5 mm | Target | 15 mm diameter target |
| PS-0114-R | Wing Tip Reference | (1350, 2600, 300) | ±0.5 mm | Target | 15 mm diameter target |
| PS-0115-L | Wing Leading Edge at BL 1500 | (1200, -1500, 250) | ±0.5 mm | Target | 15 mm diameter target |
| PS-0116-R | Wing Leading Edge at BL 1500 | (1200, 1500, 250) | ±0.5 mm | Target | 15 mm diameter target |

### 3.3 Empennage Primary Structure Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| PS-0201-C | Horizontal Stabilizer Front Spar Attachment | (2350, 0, 500) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0202-C | Horizontal Stabilizer Rear Spar Attachment | (2450, 0, 500) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0203-L | Horizontal Stabilizer Front Spar at BL 300 | (2380, -300, 520) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0204-R | Horizontal Stabilizer Front Spar at BL 300 | (2380, 300, 520) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0205-L | Horizontal Stabilizer Rear Spar at BL 300 | (2480, -300, 520) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0206-R | Horizontal Stabilizer Rear Spar at BL 300 | (2480, 300, 520) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0207-L | Horizontal Stabilizer Tip Reference | (2430, -925, 550) | ±0.5 mm | Target | 15 mm diameter target |
| PS-0208-R | Horizontal Stabilizer Tip Reference | (2430, 925, 550) | ±0.5 mm | Target | 15 mm diameter target |
| PS-0209-C | Vertical Stabilizer Front Spar Attachment | (2300, 0, 650) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0210-C | Vertical Stabilizer Rear Spar Attachment | (2500, 0, 650) | ±0.2 mm | Tooling Hole | 12 mm diameter hole |
| PS-0211-C | Vertical Stabilizer Front Spar at WL 800 | (2350, 0, 800) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0212-C | Vertical Stabilizer Rear Spar at WL 800 | (2550, 0, 800) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| PS-0213-C | Vertical Stabilizer Tip Reference | (2450, 0, 1300) | ±0.5 mm | Target | 15 mm diameter target |

### 3.4 Landing Gear Primary Structure Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| PS-0301-C | Nose Landing Gear Attachment | (450, 0, 100) | ±0.2 mm | Tooling Hole | 15 mm diameter hole |
| PS-0302-C | Nose Landing Gear Trunnion Axis Forward | (440, 0, 100) | ±0.2 mm | Bushing | 15 mm diameter bushing |
| PS-0303-C | Nose Landing Gear Trunnion Axis Aft | (460, 0, 100) | ±0.2 mm | Bushing | 15 mm diameter bushing |
| PS-0304-L | Main Landing Gear Attachment | (1400, -460, 100) | ±0.2 mm | Tooling Hole | 20 mm diameter hole |
| PS-0305-R | Main Landing Gear Attachment | (1400, 460, 100) | ±0.2 mm | Tooling Hole | 20 mm diameter hole |
| PS-0306-L | Main Landing Gear Trunnion Axis Forward | (1380, -460, 100) | ±0.2 mm | Bushing | 20 mm diameter bushing |
| PS-0307-R | Main Landing Gear Trunnion Axis Forward | (1380, 460, 100) | ±0.2 mm | Bushing | 20 mm diameter bushing |
| PS-0308-L | Main Landing Gear Trunnion Axis Aft | (1420, -460, 100) | ±0.2 mm | Bushing | 20 mm diameter bushing |
| PS-0309-R | Main Landing Gear Trunnion Axis Aft | (1420, 460, 100) | ±0.2 mm | Bushing | 20 mm diameter bushing |
| PS-0310-L | Main Landing Gear Drag Strut Attachment | (1450, -460, 150) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| PS-0311-R | Main Landing Gear Drag Strut Attachment | (1450, 460, 150) | ±0.3 mm | Bushing | 15 mm diameter bushing |

## 4. Secondary Structure Measurement Points
### 4.1 Control Surface Attachment Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SS-0001-L | Inboard Aileron Hinge Line Origin | (1300, -500, 250) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0002-R | Inboard Aileron Hinge Line Origin | (1300, 500, 250) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0003-L | Outboard Aileron Hinge Line Origin | (1300, -900, 300) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0004-R | Outboard Aileron Hinge Line Origin | (1300, 900, 300) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0005-L | Inboard Flap Track #1 | (1350, -300, 200) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| SS-0006-R | Inboard Flap Track #1 | (1350, 300, 200) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| SS-0007-L | Inboard Flap Track #2 | (1350, -400, 200) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| SS-0008-R | Inboard Flap Track #2 | (1350, 400, 200) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| SS-0009-L | Outboard Flap Track #1 | (1350, -600, 220) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| SS-0010-R | Outboard Flap Track #1 | (1350, 600, 220) | ±0.3 mm | Bushing | 10 mm diameter bushing |
| SS-0011-L | Elevator Hinge Line Origin | (2400, -300, 500) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0012-R | Elevator Hinge Line Origin | (2400, 300, 500) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0013-C | Rudder Hinge Line Origin | (2450, 0, 700) | ±0.3 mm | Bushing | 8 mm diameter bushing |
| SS-0014-C | Horizontal Stabilizer Pivot Point | (2350, 0, 500) | ±0.2 mm | Bushing | 12 mm diameter bushing |

### 4.2 Door and Access Panel Attachment Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SS-0101-L | Forward Passenger Door Upper Hinge | (650, -290, 350) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0102-L | Forward Passenger Door Lower Hinge | (650, -290, 150) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0103-R | Forward Emergency Exit Upper Hinge | (950, 290, 300) | ±0.5 mm | Bushing | 6 mm diameter bushing |
| SS-0104-R | Forward Emergency Exit Lower Hinge | (950, 290, 200) | ±0.5 mm | Bushing | 6 mm diameter bushing |
| SS-0105-L | Aft Passenger Door Upper Hinge | (1800, -290, 350) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0106-L | Aft Passenger Door Lower Hinge | (1800, -290, 150) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0107-R | Aft Emergency Exit Upper Hinge | (1500, 290, 300) | ±0.5 mm | Bushing | 6 mm diameter bushing |
| SS-0108-R | Aft Emergency Exit Lower Hinge | (1500, 290, 200) | ±0.5 mm | Bushing | 6 mm diameter bushing |
| SS-0109-R | Forward Cargo Door Forward Hinge | (500, 290, 100) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0110-R | Forward Cargo Door Aft Hinge | (650, 290, 100) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0111-R | Aft Cargo Door Forward Hinge | (1900, 290, 100) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0112-R | Aft Cargo Door Aft Hinge | (2050, 290, 100) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SS-0113-L | Service Access Door Hinge | (400, -290, 200) | ±0.5 mm | Bushing | 6 mm diameter bushing |
| SS-0114-C | APU Access Door Upper Hinge | (2700, 0, 250) | ±0.5 mm | Bushing | 6 mm diameter bushing |
| SS-0115-C | APU Access Door Lower Hinge | (2700, 0, 150) | ±0.5 mm | Bushing | 6 mm diameter bushing |

### 4.3 Fairings and Secondary Structure
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SS-0201-L | Wing-to-Fuselage Fairing Forward | (1100, -250, 250) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0202-R | Wing-to-Fuselage Fairing Forward | (1100, 250, 250) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0203-L | Wing-to-Fuselage Fairing Aft | (1400, -250, 250) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0204-R | Wing-to-Fuselage Fairing Aft | (1400, 250, 250) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0205-L | Inboard Engine Pylon Fairing Forward | (1100, -250, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0206-R | Inboard Engine Pylon Fairing Forward | (1100, 250, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0207-L | Inboard Engine Pylon Fairing Aft | (1300, -250, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0208-R | Inboard Engine Pylon Fairing Aft | (1300, 250, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0209-L | Outboard Engine Pylon Fairing Forward | (1100, -650, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0210-R | Outboard Engine Pylon Fairing Forward | (1100, 650, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0211-L | Outboard Engine Pylon Fairing Aft | (1300, -650, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0212-R | Outboard Engine Pylon Fairing Aft | (1300, 650, 300) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0213-C | Vertical Stabilizer-to-Fuselage Fairing Forward | (2300, 0, 650) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0214-C | Vertical Stabilizer-to-Fuselage Fairing Aft | (2500, 0, 650) | ±1.0 mm | Target | 15 mm diameter target |
| SS-0215-C | APU Exhaust Fairing | (2750, 0, 250) | ±1.0 mm | Target | 15 mm diameter target |

## 5. Systems Installation Measurement Points
### 5.1 Propulsion System Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SY-0001-L | Inboard Engine Pylon Forward Attachment | (1100, -250, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0002-R | Inboard Engine Pylon Forward Attachment | (1100, 250, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0003-L | Inboard Engine Pylon Aft Attachment | (1300, -250, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0004-R | Inboard Engine Pylon Aft Attachment | (1300, 250, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0005-L | Outboard Engine Pylon Forward Attachment | (1100, -650, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0006-R | Outboard Engine Pylon Forward Attachment | (1100, 650, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0007-L | Outboard Engine Pylon Aft Attachment | (1300, -650, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0008-R | Outboard Engine Pylon Aft Attachment | (1300, 650, 300) | ±0.3 mm | Bushing | 15 mm diameter bushing |
| SY-0009-C | Quantum Propulsion System Forward Mount | (1200, 0, 250) | ±0.2 mm | Bushing | 20 mm diameter bushing |
| SY-0010-C | Quantum Propulsion System Aft Mount | (1350, 0, 250) | ±0.2 mm | Bushing | 20 mm diameter bushing |
| SY-0011-C | APU Forward Mount | (2350, 0, 200) | ±0.5 mm | Bushing | 12 mm diameter bushing |
| SY-0012-C | APU Aft Mount | (2400, 0, 200) | ±0.5 mm | Bushing | 12 mm diameter bushing |

### 5.2 Flight Control System Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SY-0101-L | Aileron Actuator Attachment | (1300, -500, 240) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0102-R | Aileron Actuator Attachment | (1300, 500, 240) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0103-L | Inboard Flap Actuator Attachment | (1350, -350, 190) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0104-R | Inboard Flap Actuator Attachment | (1350, 350, 190) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0105-L | Outboard Flap Actuator Attachment | (1350, -650, 210) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0106-R | Outboard Flap Actuator Attachment | (1350, 650, 210) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0107-L | Spoiler Actuator Attachment | (1250, -400, 240) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SY-0108-R | Spoiler Actuator Attachment | (1250, 400, 240) | ±0.5 mm | Bushing | 8 mm diameter bushing |
| SY-0109-L | Elevator Actuator Attachment | (2400, -200, 490) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0110-R | Elevator Actuator Attachment | (2400, 200, 490) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0111-C | Rudder Actuator Lower Attachment | (2450, 0, 700) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0112-C | Rudder Actuator Upper Attachment | (2450, 0, 900) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0113-C | Horizontal Stabilizer Actuator Forward | (2350, 0, 480) | ±0.3 mm | Bushing | 12 mm diameter bushing |
| SY-0114-C | Horizontal Stabilizer Actuator Aft | (2450, 0, 480) | ±0.3 mm | Bushing | 12 mm diameter bushing |

### 5.3 Environmental Control System Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SY-0201-L | Air Conditioning Pack Attachment Forward | (1100, -100, 100) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0202-L | Air Conditioning Pack Attachment Aft | (1200, -100, 100) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0203-R | Air Conditioning Pack Attachment Forward | (1100, 100, 100) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0204-R | Air Conditioning Pack Attachment Aft | (1200, 100, 100) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0205-L | Outflow Valve Attachment | (2100, -290, 250) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0206-R | Outflow Valve Attachment | (2100, 290, 250) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0207-C | Forward Pressure Relief Valve | (350, 0, 350) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0208-C | Aft Pressure Relief Valve | (2100, 0, 350) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0209-C | Mixing Manifold Attachment | (1100, 0, 100) | ±1.0 mm | Target | 15 mm diameter target |
| SY-0210-L | Forward Distribution Duct Reference | (650, -100, 450) | ±2.0 mm | Target | 15 mm diameter target |
| SY-0211-R | Forward Distribution Duct Reference | (650, 100, 450) | ±2.0 mm | Target | 15 mm diameter target |
| SY-0212-L | Mid Distribution Duct Reference | (1350, -100, 450) | ±2.0 mm | Target | 15 mm diameter target |
| SY-0213-R | Mid Distribution Duct Reference | (1350, 100, 450) | ±2.0 mm | Target | 15 mm diameter target |
| SY-0214-L | Aft Distribution Duct Reference | (1800, -100, 450) | ±2.0 mm | Target | 15 mm diameter target |
| SY-0215-R | Aft Distribution Duct Reference | (1800, 100, 450) | ±2.0 mm | Target | 15 mm diameter target |

### 5.4 Quantum Propulsion System Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| SY-0301-C | Quantum Core Forward Reference | (1200, 0, 250) | ±0.2 mm | Target | 20 mm diameter target |
| SY-0302-C | Quantum Core Aft Reference | (1350, 0, 250) | ±0.2 mm | Target | 20 mm diameter target |
| SY-0303-C | Quantum Core Upper Reference | (1275, 0, 360) | ±0.2 mm | Target | 20 mm diameter target |
| SY-0304-C | Quantum Core Lower Reference | (1275, 0, 140) | ±0.2 mm | Target | 20 mm diameter target |
| SY-0305-L | Quantum Core Left Reference | (1275, -110, 250) | ±0.2 mm | Target | 20 mm diameter target |
| SY-0306-R | Quantum Core Right Reference | (1275, 110, 250) | ±0.2 mm | Target | 20 mm diameter target |
| SY-0307-C | Containment Shield Forward Reference | (1180, 0, 250) | ±0.3 mm | Target | 15 mm diameter target |
| SY-0308-C | Containment Shield Aft Reference | (1370, 0, 250) | ±0.3 mm | Target | 15 mm diameter target |
| SY-0309-C | Cryogenic System Forward Attachment | (1250, 0, 150) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0310-C | Cryogenic System Aft Attachment | (1300, 0, 150) | ±0.5 mm | Bushing | 10 mm diameter bushing |
| SY-0311-C | Quantum-Classical Interface Reference | (1250, 0, 200) | ±0.3 mm | Target | 15 mm diameter target |
| SY-0312-C | Quantum Control Unit Attachment | (1200, 0, 200) | ±0.5 mm | Bushing | 10 mm diameter bushing |

## 6. Interior Installation Measurement Points
### 6.1 Cabin Interior Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| IN-0001-C | Forward Galley Attachment | (500, 0, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0002-C | Mid Galley Attachment | (1375, 0, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0003-C | Aft Galley Attachment | (2050, 0, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0004-L | Forward Lavatory Attachment | (675, -150, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0005-R | Forward Lavatory Attachment | (675, 150, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0006-L | Mid Lavatory Attachment | (1375, -150, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0007-R | Mid Lavatory Attachment | (1375, 150, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0008-L | Aft Lavatory Attachment | (1975, -150, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0009-R | Aft Lavatory Attachment | (1975, 150, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0010-L | Forward Attendant Station | (575, -290, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0011-R | Forward Attendant Station | (575, 290, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0012-L | Mid Attendant Station | (1375, -290, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0013-R | Mid Attendant Station | (1375, 290, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0014-L | Aft Attendant Station | (2075, -290, 100) | ±2.0 mm | Target | 15 mm diameter target |
| IN-0015-R | Aft Attendant Station | (2075, 290, 100) | ±2.0 mm | Target | 15 mm diameter target |

### 6.2 Seat Track Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| IN-0101-L | Left Outboard Seat Track Forward | (650, -200, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0102-L | Left Outboard Seat Track Aft | (2000, -200, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0103-L | Left Center Seat Track Forward | (650, -100, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0104-L | Left Center Seat Track Aft | (2000, -100, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0105-C | Center Seat Track Forward | (650, 0, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0106-C | Center Seat Track Aft | (2000, 0, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0107-R | Right Center Seat Track Forward | (650, 100, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0108-R | Right Center Seat Track Aft | (2000, 100, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0109-R | Right Outboard Seat Track Forward | (650, 200, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0110-R | Right Outboard Seat Track Aft | (2000, 200, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0111-L | First Class Seat Track Reference | (800, -150, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0112-R | First Class Seat Track Reference | (800, 150, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0113-L | Business Class Seat Track Reference | (1150, -150, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0114-R | Business Class Seat Track Reference | (1150, 150, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0115-L | Economy Class Seat Track Reference | (1600, -150, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0116-R | Economy Class Seat Track Reference | (1600, 150, 100) | ±1.0 mm | Target | 10 mm diameter target |

### 6.3 Flight Deck Measurement Points
| Point ID | Description | Location (FS, BL, WL) | Tolerance | Type | Reference Feature |
|----------|-------------|------------------------|-----------|------|-------------------|
| IN-0201-L | Captain's Seat Attachment | (300, -50, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0202-R | First Officer's Seat Attachment | (300, 50, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0203-C | Observer's Seat Attachment | (330, 0, 100) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0204-L | Left Instrument Panel Reference | (280, -50, 150) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0205-R | Right Instrument Panel Reference | (280, 50, 150) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0206-C | Center Pedestal Forward Reference | (290, 0, 120) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0207-C | Center Pedestal Aft Reference | (330, 0, 120) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0208-C | Overhead Panel Forward Reference | (290, 0, 200) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0209-C | Overhead Panel Aft Reference | (330, 0, 200) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0210-C | Glareshield Reference | (270, 0, 170) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0211-L | Left Control Column Reference | (290, -50, 130) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0212-R | Right Control Column Reference | (290, 50, 130) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0213-L | Left Rudder Pedal Reference | (260, -25, 80) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0214-R | Right Rudder Pedal Reference | (260, 25, 80) | ±1.0 mm | Target | 10 mm diameter target |
| IN-0215-C | Flight Deck Door Reference | (350, 0, 150) | ±1.0 mm | Target | 10 mm diameter target |

## 7. Measurement Point Usage Guidelines
### 7.1 Manufacturing Applications
#### 7.1.1 Component Manufacturing
- Use tooling points (TL-series) for initial setup and alignment
- Verify primary structure points (PS-series) for critical components
- Tolerance verification should use the most precise measurement system available
- Document all measurements in the manufacturing record system
- Flag any out-of-tolerance conditions for engineering review

#### 7.1.2 Assembly Operations
- Use primary structure points (PS-series) for major component alignment
- Use secondary structure points (SS-series) for subassembly positioning
- Establish measurement network covering all critical points
- Perform real-time measurement during assembly operations
- Document final assembly measurements in the assembly record system

### 7.2 Quality Control Applications
#### 7.2.1 Inspection Procedures
- Develop inspection plans based on measurement point classification
- Primary structure points (PS-series): 100% inspection
- Secondary structure points (SS-series): Statistical sampling
- Systems points (SY-series): Functional verification
- Interior points (IN-series): Visual inspection with spot measurements
- Document all inspection results in the quality management system

#### 7.2.2 Non-Conformance Management
- Identify affected measurement points for any non-conformance
- Classify non-conformance based on point classification
- Primary structure points: Critical non-conformance
- Secondary structure points: Major non-conformance
- Systems and interior points: Minor non-conformance
- Develop disposition based on affected points and tolerance deviation

### 7.3 Maintenance Applications
#### 7.3.1 Structural Repairs
- Use primary and secondary structure points to establish reference system
- Verify pre-repair dimensions using appropriate measurement points
- Ensure repair restores original dimensional relationships
- Document post-repair measurements in the maintenance records
- Verify critical alignments after major repairs

#### 7.3.2 Component Replacement
- Use systems installation points (SY-series) for component positioning
- Verify interface dimensions before and after replacement
- Ensure proper alignment of all connected systems
- Document measurements in the maintenance records
- Perform functional tests to verify proper installation

### 7.4 Measurement System Selection
| Point Classification | Recommended Measurement System | Minimum Accuracy | Verification Frequency |
|---------------------|--------------------------------|------------------|------------------------|
| Primary Structure (PS) | Laser Tracker | ±0.05 mm | Each measurement |
| Secondary Structure (SS) | Laser Tracker or Photogrammetry | ±0.1 mm | Each measurement |
| Systems (SY) | Laser Tracker, Photogrammetry, or Portable CMM | ±0.2 mm | Each critical system |
| Interior (IN) | Photogrammetry or Laser Scanner | ±0.5 mm | Sampling basis |
| Tooling (TL) | Laser Tracker | ±0.05 mm | Daily verification |
| Maintenance (MX) | Portable CMM or Laser Scanner | ±0.2 mm | Each repair |

## 8. References
- Dimensional Data Report (GP-AM-EDR-06-001)
- Calibration & Measurement Procedures Document (GP-AM-EDR-06-002)
- Structural Integration Analysis Report (GP-AM-EDR-06-003)
- Internal Compartment Layout Document (GP-AM-EDR-06-004)
- Detailed Dimensions and Volume Calculation Report (GP-AM-EDR-06-005)
- Cross-Reference Diagram for Measurement Points (GP-AM-DRW-06-007)
- Manufacturing Process Specification (GP-AM-MPS-001)
- Assembly Process Specification (GP-AM-APS-001)
- Quality Control Plan (GP-AM-QCP-001)
- Maintenance Manual (GP-AM-MM-001)
