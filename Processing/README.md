# Batch Video & Audio Processing Workflows

This directory contains offline batch-processing workflows for converting and analyzing recorded datasets.

## Workflow Categories

### 1. Batch Video Luminance-to-Audio Sonification & CSV Export
- **`musciaverage_csv_autonamed_v2.bonsai`**: Enumerates all `.avi` files in a directory (`GetFiles`), computes average ROI luminance per frame (`Crop`, `Grayscale`, `Average`), modulates an audio sine wave (`FunctionGenerator`), muxes video and audio pipes via FFmpeg (`\\.\pipe\video`, `\\.\pipe\audio`), and exports frame-by-frame luminance values to auto-named CSV files.
