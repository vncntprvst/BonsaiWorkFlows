# Shared Extensions (`IncludeWorkflow` Modules)

This directory contains reusable Bonsai sub-workflows (`IncludeWorkflow` extensions) that can be embedded as modular operators inside parent workflows.

## Workflow Categories

### 1. Image Masking & Contour Extraction
- **`MaskContour.bonsai`**: Sub-workflow that accepts an image stream (`Source1`), applies morphological operations and thresholding, and extracts binary region contours.

### 2. Rotary Encoder Decoding
- **`RotaryEncoderRunCCW.bonsai`**: Quadrature decoder sub-workflow that takes two digital input channels (`Source1`, `Source2`) from a rotary encoder and outputs accumulated signed step counts (`+1` / `-1`).

### 3. Hardware & Video Trigger Control
- **`Video_ArduCtl.bonsai`**: Keyboard-triggered Arduino digital output synchronization module (`KeyDown` -> `DigitalOutput`) for starting and stopping external camera/recording triggers.
