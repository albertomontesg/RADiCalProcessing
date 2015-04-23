time = 60;  % seconds of recording
Fs = 44100; % Hz of sampling frequency
nBits = 16; % number of bits


recorder = audiorecorder(Fs, nBits, 1, 4);

disp('Start recording signal');
recordblocking(recorder, time);
disp('End of recording signal');

signal = getaudiodata(recorder);
plot(signal)