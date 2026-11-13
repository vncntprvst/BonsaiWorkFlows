# Video Acquisition Workflows

This directory contains Bonsai workflows for single- and multi-camera video capture, hardware-triggered high-speed acquisition, screen recording, and FFmpeg video piping.

## Workflow Categories

### 1. Multi-Camera & Webcam Acquisition
- **`2Cams.bonsai` / `2CamRecLogs.bonsai` / `3Cams.bonsai` / `4CamsRecording.bonsai` / `WebCams_RecLogs_noTimer.bonsai`**: Captures synchronized video streams from 2, 3, or 4 DirectShow/USB cameras (`VideoCaptureDevice` / `CameraCapture`) with frame timestamp logging (`CsvWriter`).
- **`Dino-Lite.bonsai`**: Acquisition workflow configured for Dino-Lite USB digital microscopes.
- **`Read_Video.bonsai`**: Basic video file playback template (`FileCapture`).

### 2. Basler Pylon & Point Grey High-Speed Cameras
- **`BaslerCamRecord.bonsai` / `BaslerVideo_Debug.bonsai` / `HSCam_Pylon_tests.bonsai`**: Acquires high-speed video from Basler USB3 cameras (`Bonsai.Pylon.PylonCapture`) using `.pfs` camera configuration files in `VideoSettings/` and optional Arduino trigger control (`Extensions/Video_ArduCtl.bonsai`).
- **`PointGrey_Flea3_Video_Trigger.bonsai`**: Hardware-triggered acquisition for Point Grey Flea3 cameras (`Bonsai.PointGrey.FlyCapture`), using embedded GPIO pin states (`GpioPinState`) to trigger windowed video recording (`WindowTrigger`).

### 3. Screen Capture & FFmpeg Piping
- **`Screen_VideoCapture.bonsai` / `Screen_VideoCapture_ffmpeg.bonsai`**: Captures desktop screen regions (`ScreenCaptureStream`) and writes either directly via `VideoWriter` or through an FFmpeg named pipe.
- **`cam_pipe_to_ffmpeg_quick_sync.bonsai`**: Pipes live camera frames (`ImageWriter` -> `\\.\pipe\video`) to an automatically launched FFmpeg process alongside synchronized Arduino TTL timestamps.
- **Subdirectories**:
  - [`FFmpeg/`](FFmpeg/README.md): Dedicated workflows for lossless, multi-camera, TIFF, and audio-video synchronized FFmpeg encoding.
  - [`VideoSettings/`](VideoSettings/README.md): Basler Pylon `.pfs` parameter files for 100 Hz / 500 Hz triggered and free-running camera modes.
