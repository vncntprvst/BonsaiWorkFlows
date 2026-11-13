# Motor & Servo Control Workflows

This directory contains Bonsai workflows for closed-loop motor and servo actuation (`Bonsai.Arduino`).

## Workflow Categories

### 1. Video-Triggered Servo Control
- **`flycapture_triggeringSERVO.bonsai`**: Tracks object area in a live Point Grey camera stream (`FlyCapture`, `Crop`, `BackgroundSubtraction`, `FindContours`, `LargestBinaryRegion`) and drives an Arduino servo output (`ServoOutput`) when the detected region crosses an area threshold.
