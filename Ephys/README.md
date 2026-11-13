# Electrophysiology (Ephys) Workflows

This directory contains Bonsai workflows for extracellular electrophysiology acquisition, real-time spike/LFP processing, and closed-loop stimulation using **Open Ephys / Intan RHD2000** (`Bonsai.Ephys`) and **Bonsai.Dsp**.

## Workflow Categories

### 1. Multi-Channel Open Ephys / RHD2000 Acquisition
- **`16Ch_OE.bonsai` / `16Ch_OE_AUXchannels.bonsai` / `32Ch_OE_AUXchannels.bonsai`**: Acquires 16- or 32-channel amplifier data alongside auxiliary accelerometer/analog channels from an `Rhd2000EvalBoard`, applies bandpass filtering (`FrequencyFilter`), and streams binary data to disk (`MatrixWriter`).
- **`AcuteRecording_32chnlDemo.bonsai`**: Full 32-channel acute recording pipeline with channel remapping (`SelectChannels`), spike detection (`DetectSpikes`), audio monitoring (`AudioPlayback`), synchronized video recording, and TTL timestamp logging.
- **`AnalogIn_OE_SingleChannelRecording.bonsai`**: Records single-channel electrode and board ADC signals with spike waveform extraction.
- **`ephys.bonsai` / `ephys_amplifiers.bonsai` / `intan_selectchannels.bonsai`**: Basic acquisition templates for `Rhd2000EvalBoard` and `IntanEvalBoard` amplifier channel selection and binary logging.

### 2. Offline Playback & Multi-Channel File Splitting
- **`readephys.bonsai`**: Reads recorded binary electrophysiology files (`MatrixReader`) for offline filtering and visualization.
- **`multichannelwriter.bonsai`**: Reusable sub-workflow (`MultiChannelWriter`) that dynamically splits an incoming multi-channel `Mat` stream into separate per-channel binary files (`channels/channel_{i}.bin`).

### 3. Closed-Loop & Multi-Frequency Stimulation Protocols
- **`EEG_stim_protocol.bonsai`**: Synchronizes EEG acquisition with programmable stimulation pulse trains.
- **`slim_test_multi_frequency.bonsai`**: Multi-arena activity bout detector and programmable multi-frequency Arduino TTL stimulation controller.
- **`Ephys_Workflows_Notes.md`**: Notes on channel mapping, filter settings, and binary file formats.
