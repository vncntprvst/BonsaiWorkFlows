# BPod Workflows

This directory contains Bonsai workflows for integrating **Sanworks Bpod** behavioral state machines with video tracking and Open Sound Control (`Bonsai.Osc`) communication.

## Workflow Categories

### 1. Video-Based Closed-Loop OSC Triggers
- **`Basic_Video_Based_OSC_Trigger.bonsai` / `Light_bottom_0320_speed.bonsai`**: Tracks animal position and velocity from a live camera stream (`CameraCapture`, `FindContours`, `BinaryRegionAnalysis`) and sends real-time trigger messages over UDP/OSC (`Osc.config`) to Bpod or MATLAB when spatial/velocity thresholds are met.

### 2. Bpod + Video / Photometry Synchronization
- **`SA-FP-Protocol.bonsai`**: Simultaneously records behavioral video (`VideoWriter`) and logs incoming OSC trial/event messages from MATLAB/Bpod (`ReceiveMessage`) with synchronized timestamps to CSV.
