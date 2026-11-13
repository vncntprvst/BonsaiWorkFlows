# Video Operations & Image Processing (`VideoOp`)

This directory contains Bonsai workflows for real-time and offline video processing, ROI activity detection, head-centered reference frame alignment, frame slicing/splitting, and timestamped video recording.

## Workflow Categories

### 1. Head-Centered Reference Frame Alignment & Tracking
- **`HeadCenteredVideo.bonsai` / `Head_Centered_RefFrame.bonsai`**: Tracks animal head position and orientation (`Threshold`, `FindContours`, `BinaryRegionAnalysis`, `LargestBinaryRegion`) and applies a dynamic affine warp (`WarpAffine`) to stabilize the video in a head-centered coordinate frame.
- **`tracking_boxcenter_v2.bonsai` / `multiblob.bonsai`**: Tracks single or multiple binary blobs/centroids across arena ROIs.

### 2. ROI Activity Detection & Closed-Loop Triggers
- **`videoROI.bonsai` / `testROILoc.bonsai` / `MultiRoiEntryToExitIntervalAnalysis.bonsai` / `MultiRoiEntryToExitIntervalAnalysis_Frames.bonsai`**: Measures pixel activity (`RoiActivity`, `RoiActivityDetected`) across multiple user-defined ROIs and computes entry-to-exit intervals in time or frame counts.
- **`ROI_Activation_DigOutput.bonsai` / `KeyStroke_ROI_trigger_Arduino_Video.bonsai`**: Triggers Arduino digital outputs when activity inside a video ROI crosses a threshold.
- **`FindLEDonset.bonsai` / `LEDtimes.bonsai` / `Find_Wall_Movement_Frame_Number.bonsai` / `Get_Stim_VideoFrameIndex_Time.bonsai` / `ManualStimFrameIndex.bonsai`**: Detects stimulus LED onset frames or mechanical wall movements from video ROI luminance changes.

### 3. Video Slicing, Splitting, Concatenation & Transforms
- **`SliceVideo.bonsai` / `videosplit.bonsai` / `SplitVideoByFrameIndex.bonsai` / `SplitVideoByFrameIndex_SplitLeft.bonsai` / `SplitVideoByFrameIndex_SplitRight.bonsai` / `GetVideoTrialsFromCSV.bonsai`**: Segments or de-interleaves video files by frame index or trial CSV timestamps.
- **`ConcatVideos.bonsai` / `MultiViewVideoConcatSave.bonsai` / `Batch_Videos.bonsai` / `Batch_VideoProc_PyGenerateCSV.bonsai`**: Concatenates multiple camera views horizontally/vertically (`Concat`) or batch-processes directories of video files.
- **`2DFourierTransform.bonsai` / `Rotate_Video_90deg.bonsai` / `FrameDiff.bonsai` / `Resample_Video.bonsai` / `video_crop_record.bonsai` / `videoloop.bonsai` / `Webcam_Flipped.bonsai` / `multi-page_tiff_magick.bonsai` / `WhiskerFilter.bonsai`**: Spatial/frequency transforms (`Dft`), 90-degree rotation, frame differencing, cropping, flipping, and whisker morphological filtering.

### 4. Timestamped, Periodic & Triggered Video Recording
- **`JustVideo_TimeStamped.bonsai` / `Just2Video_TimeStamped.bonsai` / `RecordVideo_AndTimestamp.bonsai` / `Record_TSVideo_TS.bonsai` / `Pulse_Record_TS_Video_AndTimestamps.bonsai` / `Record2Videos_WebC_HSC_TS_ROIs.bonsai`**: Records 1 or 2 camera streams with inter-frame interval calculation and CSV timestamp logs.
- **`PeriodicRecording.bonsai` / `RecordingDynamicStartStop.bonsai` / `RecordTriggeredVideo.bonsai` / `VideoRec_KeyPress.bonsai` / `FPS_Estimate.bonsai` / `16Ch_OE_Video.bonsai` / `WheelRunDistanceVideo.bonsai`**: Keyboard-, timer-, or TTL-gated video recording and online frame-rate estimation.
