# Wide-Field Imaging Workflows

This directory contains Bonsai workflows and camera configurations for dual-wavelength / dual-camera **wide-field cortical calcium/hemodynamic imaging** ($\Delta F/F$) using Basler (`Bonsai.Pylon`) and PCO (`Bonsai.Pco`) cameras.

## Workflow Categories

### 1. Online $\Delta F/F$ Computation & Frame De-Interleaving
- **`WideField_DFoF.bonsai`**: De-interleaves alternating blue/green excitation frames by frame index (`ElementIndex`, `Mod`), computes triggered baseline fluorescence averages (`WindowTrigger`, `ConvertScale`, `IncrementalMean`), and saves de-interleaved TIFF stacks.

### 2. Single- & Dual-Camera Wide-Field + Behavioral Recording
- **`WideField_OneCam.bonsai`**: Single-camera Basler wide-field imaging pipeline with hardware frame counter and timestamp logging.
- **`WideField_TwoCam.bonsai` / `WideField2Cams.bonsai`**: Synchronized acquisition from a wide-field imaging camera (Basler or PCO Edge via `Bonsai.Pco.PcoCapture`) and a behavioral monitoring camera (`BaslerConfig/`).

### 3. Camera Configurations (`BaslerConfig/` & `PCOConfig/`)
- **`BaslerConfig/`**: Pylon `.pfs` parameter files for `WideFieldCam.pfs` and `BehaviorCam.pfs`.
- **`PCOConfig/`**: Build notes (`compiling Bonsai.PCO.md`, `16-bit video with ffmpeg.txt`) and compiled `Bonsai.Pco` (`0.2.0`) NuGet package and native `SC2_Cam.dll` libraries for PCO sCMOS cameras.
