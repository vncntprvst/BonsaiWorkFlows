# Arduino Workflows

This directory contains Bonsai workflows for interfacing with **Arduino** microcontrollers via Firmata (`Bonsai.Arduino`) or raw serial communication (`Bonsai.System.IO.Ports`).

## Workflow Categories

### 1. Digital Input & Triggered Actions
- **`SendKey_on_DigIn.bonsai` / `SendKey_on_DigIn_Python.bonsai` / `SendKey_Python.bonsai`**: Monitors an Arduino digital input pin (`DigitalInput`) and triggers simulated keyboard shortcuts (`SendKeys`) when a rising TTL edge is detected.
- **`Conditional_Data_Write.bonsai` / `ConditionalSourceStart.bonsai` / `parsecondition.bonsai`**: Demonstrates conditional data logging and acquisition gating controlled by Arduino digital/analog inputs.

### 2. Digital Output, LED Control & Synchronization Pulses
- **`LED_Blink.bonsai` / `TriggerPulses.bonsai`**: Generates periodic or key-triggered TTL output pulses on Arduino digital output pins (`DigitalOutput`).
- **`KeyPress_SyncOut.bonsai` / `KbStartEnd_Firmata.bonsai`**: Sends synchronization TTL pulses to an Arduino upon keyboard events (`KeyDown`) to synchronize external recording equipment.
- **`ROITrigger_ArduinoIO.bonsai`**: Closed-loop video ROI activity detector that drives an Arduino digital output pin when movement is detected inside a region of interest.

### 3. Serial Communication & Analog Acquisition
- **`Example_Read_Arduino_Data.bonsai` / `SerialCom.bonsai` / `KbStart_SerialWrite.bonsai`**: Reads and writes raw serial messages or analog input streams over a configured COM port (`SerialPort.config`).
- **`MinimalistFirmata.txt`**: Reference Arduino sketch notes for minimal Firmata/serial communication.
