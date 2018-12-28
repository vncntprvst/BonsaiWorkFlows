Using TriggeredWindow / SelectMany vs TriggeredBuffer / Concat to visualize event aligned signal.

See discussion here: 
https://groups.google.com/forum/#!topic/bonsai-users/_9HGCzL6JRk

and example workflow: visualize Mat.bonsai

When visualizing buffers that are longer than the native buffer size (e.g. 60 samples -> 6000), TriggeredWindow may be preferrable: add a ([optional: delayed]) buffer upstream, and that buffer will be displayed as soon as the window is triggered. In contrast,  TriggeredBuffer will start counting from the moment it is triggered.
See SingleChannelRecording_WhiskerTracking_v2.4.bonsai
