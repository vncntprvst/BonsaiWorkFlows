# Examples & Tutorials

This directory contains self-contained Bonsai example workflows demonstrating core reactive operators, matrix/buffer visualization, dynamic property mapping, OpenGL shaders, and OSC/audio/video patterns.

## Workflow Categories

### 1. Triggered Windows, Buffers & Matrix Visualization
- **`TriggeredWindow.bonsai` / `TriggeredWindow_vs_TriggeredBuffer.md`**: Illustrates the difference between `WindowTrigger` (`TriggeredWindow`) and `BufferTrigger` (`TriggeredBuffer`).
- **`Visualize_Mat.bonsai` / `Visualize_Mat_Buffer.bonsai` / `Visualize_Mat_Trig_Buffer_Concat.bonsai` / `Visualize_Mat_Trig_Window_SelectMany.bonsai`**: Demonstrates triggered buffering and windowing of multi-channel `Mat` streams (`AudioCapture`, `Rhd2000EvalBoard`) for real-time oscilloscope-style visualization.

### 2. Dynamic File Naming & Property Mapping
- **`FileNameInputDemo.bonsai` / `FileName_Property_Source.bonsai`**: Shows how to dynamically construct output file paths from externalized properties (`StringProperty`, `Zip`, `PythonTransform`) and map them to `VideoWriter` and `CsvWriter`.
- **`TimerTrigger_DataSave.bonsai` / `ParseCSV_timestamp_FunGen.bonsai`**: Periodic timer-driven data generation and CSV logging examples.

### 3. Timing, Clocks & Cycle Triggers
- **`stopwatch.bonsai` / `Test_clock_CPU.bonsai` / `test_cycle_trigger.bonsai`**: Benchmarks system timer intervals and demonstrates cyclic trigger generation.

### 4. Vision, Shaders & Packaged Gallery Examples
- **`Accumulate_Frames_Exposure_Control.bonsai` / `dynamic-crop.bonsai`**: Demonstrates frame accumulation and dynamic ROI cropping on camera streams.
- **`ShaderTexture.bonsai`**: Renders procedural/texture graphics using `Bonsai.Shaders`.
- **Subdirectories (`Bonsai.Examples.OscReceive`, `Bonsai.Examples.OscSend`, `Bonsai.Examples.TimeLapse`, `Bonsai.Examples.VoicePaint`)**: Official Bonsai gallery sample workflows for OSC messaging, time-lapse capture, and audio-driven painting.
