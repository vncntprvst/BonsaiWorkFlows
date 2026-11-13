# FFmpeg Video Encoding Workflows

This directory contains Bonsai workflows that stream raw image frames (`cv:ImageWriter`) over Windows named pipes (`\\.\pipe\video`) into **FFmpeg** for high-throughput, lossless, or hardware-accelerated compression.

## Workflow Categories

### 1. Basler High-Speed Camera to FFmpeg Pipe
- **`Basler_FFmpeg.bonsai` / `2BaslerCam_ffmpeg.bonsai`**: Streams 1 or 2 Basler cameras (`PylonCapture`) to named pipes and spawns `ffmpeg` via `PythonTransform` (`os.system` / `subprocess`) for real-time H.264/MPEG-4 encoding without dropped frames.

### 2. Lossless, TIFF & Audio-Video Synchronized Encoding
- **`ffmpeg_loseless.bonsai` / `ffmpeg-video.bonsai` / `ffmpegwriter.bonsai`**: Configures FFmpeg named-pipe encoding for lossless (`libx264 -crf 0` / `huffyuv`) or standard compressed video output.
- **`ffmpeg_tiff.bonsai`**: Streams camera frames into multi-page or sequential TIFF files via FFmpeg.
- **`ffmpeg-audio-video-sync.bonsai`**: Simultaneously pipes video (`\\.\pipe\video`) and audio (`\\.\pipe\audio`) streams into a single muxed FFmpeg output container.
- **`20+ FFmpeg Commands.pdf`**: Reference guide for common FFmpeg command-line flags and codecs.
