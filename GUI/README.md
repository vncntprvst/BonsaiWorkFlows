# GUI & Visualization Workflows

This directory contains Bonsai workflows demonstrating interactive user interface controls (`Bonsai.Gui`) and real-time data plotting (`Bonsai.Gui.ZedGraph`).

## Workflow Categories

### 1. Interactive Controls & Property Binding
- **`Button_Timer.bonsai`**: Uses a `ButtonBuilder` GUI control to trigger a timed pulse sequence and toggle state labels dynamically.
- **`Path_Setting.bonsai`**: Demonstrates interactive file/directory path configuration using GUI text inputs bound to downstream writers.

### 2. Real-Time Rolling Graphs
- **`RollingGraph.bonsai`**: Streams continuous time-series signals into a `RollingGraphBuilder` (`ZedGraph`) panel for live visualization.
