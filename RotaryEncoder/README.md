# Rotary Encoder Workflows

This directory contains Bonsai workflows for reading quadrature rotary encoders via Arduino digital inputs (`Bonsai.Arduino`) to measure running-wheel position, direction, and velocity.

## Workflow Categories

### 1. Quadrature Decoding & Running-Wheel Tracking
- **`RotaryEncoder.bonsai` / `RotaryEncoder_Inputs.bonsai`**: Reads two digital quadrature channels from an Arduino (`DigitalInput` pins 2 and 3) and decodes clockwise/counter-clockwise rotation steps using the `Extensions\RotaryEncoderRunCCW.bonsai` sub-workflow.
- **`RotaryEncoder_MouseRunsCCW.bonsai`**: Detects sustained counter-clockwise running bouts on a behavioral wheel and triggers downstream events.
- **`wheelcount.bonsai`**: Accumulates wheel tick counts and logs timestamped wheel movement to CSV.
