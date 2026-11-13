# TTL Pulses & Trigger Generation Workflows

This directory contains Bonsai workflows for generating, triggering, and recording TTL pulse trains using Arduino digital outputs, DSP function generators, and Open Ephys boards.

## Workflow Categories

### 1. Programmable Pulse Trains & Arduino TTL Generators
- **`pulseArd.bonsai` / `pulseArd_TS.bonsai`**: Uses reactive timers (`Timer`, `Delay`, `BitwiseNot`) to drive periodic TTL pulses on an Arduino `DigitalOutput` pin and log pulse timestamps to CSV.
- **`PulseTrain.bonsai` / `PulseTrain-ms.bonsai` / `PulseTrains.bonsai`**: Generates parameterized pulse bursts with configurable pulse width, inter-pulse interval, and burst repeat count (`RepeatCount`).
- **`TriggerTTLTrain.bonsai`**: Uses a `FunctionGenerator` and `Threshold` gated by keyboard input (`KeyDown`, `SkipUntil`) to produce square-wave TTL pulse trains.

### 2. Open Ephys TTL & Analog Trigger Recording
- **`Read_Save_OE_TTL.bonsai`**: Acquires and saves digital TTL input states (`TtlIn`) from an Open Ephys `Rhd2000EvalBoard` to binary files (`MatrixWriter`).
- **`SingleAnalogChannel_TTL.bonsai`**: Simultaneously records a single Open Ephys board ADC channel and TTL trigger stream with threshold event detection.
