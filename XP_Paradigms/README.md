# Experimental Paradigms (`XP_Paradigms`)

This directory contains complete, integrated experimental paradigm workflows combining high-speed camera capture, FFmpeg video piping, rotary encoder wheel tracking, Arduino TTL synchronization, and behavioral stimulus delivery.

## Workflow Categories

### 1. Whisker & Somatosensory Behavioral Paradigms
- **`XP_FreeWhisk.bonsai` / `XP_TouchStim.bonsai` / `XP_Video.bonsai`**: Production experimental recording paradigms acquiring 500 Hz Basler high-speed video (`PylonCapture`) piped to FFmpeg (`\\.\pipe\video`), simultaneous behavioral webcam recording, quadrature rotary encoder wheel distance/velocity logging, and Arduino digital sync inputs/outputs.
- **`Mise_En_Place.bonsai`**: Pre-experiment camera alignment, ROI positioning, and illumination check workflow.

### 2. Closed-Loop & Classical Conditioning Paradigms
- **`CloseLoop_XP.bonsai`**: Real-time closed-loop paradigm triggering Arduino digital stimulation when online tracked behavioral/video metrics cross defined thresholds.
- **`Classical_Conditioning_v2.bonsai` / `Classical_Conditioning_v3.bonsai`**: Classical conditioning trial controllers pairing timed Arduino digital cue/reward outputs (`Timer`, `Delay`, `RepeatCount`) with Point Grey (`FlyCapture`) or USB (`VideoCaptureDevice`) video and ROI tracking.
