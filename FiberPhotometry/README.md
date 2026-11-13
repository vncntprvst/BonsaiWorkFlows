# Fiber Photometry Workflows

This directory contains Bonsai workflows and MATLAB utilities for acquiring multi-wavelength fiber photometry signals synchronized with behavioral video and electrophysiology.

## Workflow Categories

### 1. Neurophotometrics FP3002 Acquisition
- **`SA-FP-Protocol.bonsai`**: Full acquisition pipeline for the **Neurophotometrics FP3002** system (`Neurophotometrics`), demultiplexing `L560`, `L410`, and `L470` fluorescence channels (`PhotometryData`, `PhotometryWriter`), logging hardware digital inputs (`DigitalInput`), and recording synchronized behavioral video (`VideoCaptureDevice`).

### 2. Camera-Based & Open Ephys Fiber Photometry
- **`FiberPhotometry.bonsai`**: Acquires fiber photometry fluorescence ROIs using a Point Grey / FLIR camera (`Bonsai.PointGrey.FlyCapture`), extracts multi-region crop intensities, and logs embedded hardware frame timestamps.
- **`16Ch_OE_FiberPhotometry.bonsai`**: Combines 16-channel Open Ephys (`Rhd2000EvalBoard`) recording with synchronized fiber photometry ROI extraction and video recording.

### 3. Timestamp Decoding Utilities
- **`PG_Bonsai_TimestampDecoder.m`**: MATLAB function for decoding 32-bit Point Grey embedded cycle timestamps (`second_count`, `cycle_count`, `cycle_offset`) exported by Bonsai.
