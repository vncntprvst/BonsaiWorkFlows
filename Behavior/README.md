# Behavior Workflows

This directory contains Bonsai workflows for behavioral experiment control, trial segmentation, real-time performance plotting, and behavioral event logging.

## Workflow Categories

### 1. Trial Control & State Switching
- **`SwitchTrials.bonsai`**: Manages trial-by-trial image acquisition gated by a trial trigger (`KeyDown` / `BehaviorSubject`), automatically incrementing trial counters and organizing saved TIFF frames into per-trial subdirectories.
- **`DelayedDeactivation.bonsai` / `DelayedDeactivationSwitch.bonsai`**: Implements delayed state deactivation logic using reactive timers (`Delay`, `TakeUntil`, `Switch`) for behavioral timeouts and stimulus hold periods.
- **`getHSVidTrials.bonsai`**: Extracts high-speed video trial epochs based on behavioral event triggers.

### 2. Behavioral Tracking & Locomotion Metrics
- **`WheelDistanceRun.bonsai`**: Computes cumulative running distance on a running wheel from rotary encoder / analog inputs.
- **`trackMouseTime.bonsai`**: Tracks animal position and occupancy time within defined arena regions.

### 3. Timestamp Parsing & Real-Time Visualization
- **`ParseCSV_timestamp.bonsai`**: Reads and parses behavioral CSV logs with high-resolution timestamps.
- **`PlotBehavPerf.bonsai`**: Computes and plots online behavioral performance metrics across trials.
