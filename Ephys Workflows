Ephys Workflows

from this old thread
https://groups.google.com/d/msg/bonsai-users/ZdHnXKxgnA8/wWYSW98dZiQJ


* Hardware: RHD2000 evaluation board or OpenEphys acquisition board. In order for this workflow to work, you also need the proper FPGA bitfile (see FAQ). The workflow records output data from multiple amplifiers, so you can connect headstages to the board for up to 256 channels simultaneous recording. It also records data from the board ADC and digital TTL inputs.
* Outputs: This workflow also outputs 3 files:
  - amplifier.bin: the raw unsigned 16-bit values acquired from the amplifiers in column-major format
  - adc.bin: same for the board ADCs
  - sync.bin: the raw unsigned 8-bit value representing the board TTL digital inputs

The workflow also provides two basic visualizations: LFP and Spikes. For each of them you need to select the channel (or channels) that you want to visualize. I've left it by default to visualize only 1 channel to ensure good operation. Visualizing simultaneously 256 channels at 30 kHz may prove challenging. Future versions of Bonsai will try to address this by using more optimized filtering and visualization routines, but for now it should be no problem to visualize something between 32-64 channels simultaneously. The ADC and TTL inputs from the board can be used to record extra sensors and signals synchronously with the neural data. This can again be used to solve synchronization between video and ephys, either by passing signals from the camera to the ephys system or from an external signal source (e.g. Arduino) to both of them.


Open in Matlab:
https://groups.google.com/d/msg/bonsai-users/rzXpXU1Z3ZM/k2FjFrWTLicJ

mcode:
%read it
fileName = 'amplifier2014-11-25T22_09_28.bin'; %amplifierData, numChannels = 32;
data = fopen(fileName);
numChannels = 32;
A = fread(data,[numChannels,Inf],'uint16'); %read in m x n matrix, m = numChannels
%sanity
if size(A,1) ~= numChannels
    error('numChanels does not match desired raw data import')
else
    warning('sanity check input passed')
end
whos A

%plot it
figure,
kk_stackedLinePlot(A(1:numChannels/4,1:1e4)), title(sprintf('plot of %s',fileName)); %plot first 8 channels, first 1e4 samps
xlabel('samples'), ylabel('Chan#')