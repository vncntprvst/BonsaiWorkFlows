# DeepLabCut (DLC) Workflows

This directory contains Bonsai workflows and helper Python scripts for **DeepLabCut** (`Bonsai.DeepLabCut`) pose estimation and whisker/reach coordinate extraction.

## Workflow Categories

### 1. Whisker & Pose Coordinate Extraction
- **`DLC_WhiskerLabelCoordinates_onVideo.bonsai` / `DLC_WhiskerLabelCoordinates_onImages.bonsai`**: Runs DeepLabCut pose estimation on video files or image sequences to extract whisker base, center, and tip coordinates.
- **`DLC_WhiskerLabelCoordinates.bonsai.template`**: Template workflow for configuring DLC model paths and label extraction pipelines.

### 2. Reach Extraction & Post-Processing Scripts
- **`DLC_ExtractReaches.bonsai` (`DLC_ExtractReaches.txt`)**: Segments reaching movements from video using tracked pose coordinates.
- **Python Helper Scripts (`base center tip.py`, `Compensating for moving base.py`, `track whiskers code.py`, `tracking variable base issue.py`)**: IronPython snippets used inside `PythonTransform` nodes to sort whisker labels, compensate for head/base motion, and format coordinate outputs.
