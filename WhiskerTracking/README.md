# Whisker Tracking Workflows

This directory contains Bonsai workflows, modular `IncludeWorkflow` extensions (`Extensions/`), and IronPython scripts for real-time and offline high-speed **whisker tracking**, head-masking, and kinematic parameter extraction.

## Workflow Categories

### 1. Single & Multi-Whisker Tracking with Head Masking
- **`WhiskerTracking_HM_Markers.bonsai` / `WhiskerTracking_hor_HM_Markers.bonsai` / `WhiskerTracking_ver_HM_Markers.bonsai` / `WhiskerTracking_wHO.bonsai`**: Extracts head outline masks (`Extensions/HeadMask.bonsai`) and color/marker masks (`Extensions/ColorMask.bonsai`), then tracks single or multiple whiskers in horizontal or vertical head orientations (`Extensions/TrackWhisker_*`).
- **`WhiskerTracking_SaveWhiskerData_2.4.bonsai` / `WhiskerTracking_SaveWhiskerData_Bottommost.bonsai` / `WhiskerTracking_SaveWhiskerData_VerticalSorting.bonsai`**: Tracks whisker contours (`FindContours`, `BinaryRegionAnalysis`), sorts whiskers spatially via `PythonTransform`, and logs base, centroid, tip, orientation, and curvature metrics to CSV.
- **`SingleChannelRecording_WhiskerTracking_v2.4.bonsai`**: Synchronizes Open Ephys (`Rhd2000EvalBoard`) single-channel recording with online high-speed whisker tracking.

### 2. Batch Offline Whisker Tracking
- **`Batch_WhiskerTracking_SaveWhiskerData.bonsai` / `Batch_WhiskerTracking_SaveWhiskerData_HorizontalSorting.bonsai` / `Batch_WhiskerTracking_SaveWhiskerData_VerticalSorting.bonsai` / `Batch_WhiskerTracking_SaveWhiskerData_KAXP.bonsai`**: Enumerates all video files in a target folder (`GetFiles`) and runs automated whisker tracking and CSV export across each video sequentially (`CreateObservable` + `Concat`).

### 3. Mask Generation & Video Overlay Visualization
- **`HeadOutline.bonsai` / `CreateMask_SplitByFrameIndex.bonsai`**: Generates binary head/fur masks from video frames to isolate whisker shafts.
- **`LargestWhiskerTracking_MultiColorVideoOverlay.bonsai` / `WhiskerLabelCoordinates_onVideo.bonsai`**: Renders multi-color tracked whisker centroids, bases, and tips overlaid on video frames.

### 4. Reusable Sub-Workflows (`Extensions/`) & Python Scripts
- **`Extensions/`**:
  - `ColorMask.bonsai`: HSV color-segmentation mask for dye-labeled whiskers.
  - `HeadMask.bonsai`: Morphological head-silhouette mask generator.
  - `TrackWhisker_Multiple_HorizontalHeadPosition.bonsai`, `TrackWhisker_Multiple_VerticalHeadPosition.bonsai`, `TrackWhisker_Single_Bottom.bonsai`, `TrackWhisker_Single_HorizontalHeadPosition.bonsai`, `TrackWhisker_Single_VerticalHeadPosition.bonsai`: Modular whisker contour extraction and sorting sub-workflows.
- **`*.py` Scripts**: Reference IronPython scripts for whisker base identification, minimum-distance base tracking, vertical/horizontal sorting, and centroid validation.
