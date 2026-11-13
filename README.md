# Bonsai Workflows Repository

A curated, tested collection of **Bonsai** (`2.9.2`) reactive workflows for neuroscience experiments, including high-speed whisker tracking, extracellular electrophysiology (Open Ephys / Intan), fiber photometry, wide-field cortical imaging, Arduino/Bpod hardware synchronization, and FFmpeg video streaming.

All **188** workflows and sub-workflows in this repository have been upgraded to the modern `https://bonsai-rx.org/2018/workflow` (`Version="2.9.2"`) schema and verified from the terminal against **Bonsai 2.9.2**.

---

## Directory Structure

| Directory | Description |
| :--- | :--- |
| [`Arduino/`](Arduino/README.md) | Arduino Firmata (`Bonsai.Arduino`) and serial (`Bonsai.System.IO.Ports`) digital/analog I/O, TTL triggers, and simulated key presses |
| [`Behavior/`](Behavior/README.md) | Behavioral trial control, delayed state switching, wheel distance tracking, and online performance plotting |
| [`BPod/`](BPod/README.md) | Sanworks Bpod state machine integration via Open Sound Control (`Bonsai.Osc`) and video-based triggers |
| [`DLC/`](DLC/README.md) | DeepLabCut (`Bonsai.DeepLabCut`) online/offline pose estimation for whisker and reach tracking |
| [`Ephys/`](Ephys/README.md) | Open Ephys / Intan (`Bonsai.Ephys`) 16/32-channel acquisition, spike detection, multi-channel binary splitting, and closed-loop stimulation |
| [`Examples/`](Examples/README.md) | Tutorials and reference patterns for `WindowTrigger` vs. `BufferTrigger`, `Mat` visualization, dynamic file naming, shaders, and OSC |
| [`Extensions/`](Extensions/README.md) | Shared reusable `IncludeWorkflow` sub-workflows (`MaskContour`, `RotaryEncoderRunCCW`, `Video_ArduCtl`) |
| [`FiberPhotometry/`](FiberPhotometry/README.md) | Neurophotometrics FP3002 (`Neurophotometrics`) and Point Grey camera-based fiber photometry acquisition and timestamp decoding |
| [`GUI/`](GUI/README.md) | Interactive GUI controls (`Bonsai.Gui`) and live rolling graphs (`Bonsai.Gui.ZedGraph`) |
| [`LabJack/`](LabJack/README.md) | LabJack (`Bonsai.LabJack`) multi-channel analog input acquisition |
| [`Motor/`](Motor/README.md) | Video-triggered closed-loop Arduino servo control |
| [`Processing/`](Processing/README.md) | Batch offline video processing, ROI luminance sonification, and automated CSV export |
| [`Pulses/`](Pulses/README.md) | Programmable TTL pulse-train generators (`Bonsai.Arduino`, `Bonsai.Dsp`) and Open Ephys TTL recording |
| [`RotaryEncoder/`](RotaryEncoder/README.md) | Quadrature rotary encoder decoding and running-wheel velocity/distance tracking |
| [`Video/`](Video/README.md) | Multi-camera USB/DirectShow, Basler (`Bonsai.Pylon`), Point Grey (`Bonsai.PointGrey`), screen capture, and [`Video/FFmpeg/`](Video/FFmpeg/README.md) named-pipe encoding |
| [`VideoOp/`](VideoOp/README.md) | Real-time and offline video operations: head-centered reference frame stabilization, multi-ROI activity analysis, video slicing/splitting, and timestamped capture |
| [`WhiskerTracking/`](WhiskerTracking/README.md) | High-speed single- and multi-whisker tracking, head/color masking (`WhiskerTracking/Extensions/`), and batch kinematic CSV export |
| [`WideField/`](WideField/README.md) | Single- and dual-camera wide-field cortical imaging ($\Delta F/F$) with Basler and PCO (`Bonsai.Pco`) cameras |
| [`XP_Paradigms/`](XP_Paradigms/README.md) | Full behavioral and sensory experimental paradigms (free whisking, touch stimulation, closed-loop, and classical conditioning) |

