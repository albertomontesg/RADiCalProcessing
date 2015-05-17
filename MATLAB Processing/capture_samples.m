time = 30;  % seconds of recording
Fs = 44100; % Hz of sampling frequency
nBits = 16; % number of bits
win = 4096; % length of the window
over = 1024;% overlaping
nFFT = 4096;% number of samples to do the FFT
%%
% Load environment variables
tmp = load('Samples 2015-04-28/environment.mat');
i = tmp.i;

% Recording
x = record(time, Fs, nBits);

% Saving
i = i+1;
save(strcat('Samples 2015-05-14/sample', int2str(i), '.mat'), 'x', 'Fs')
save('Samples 2015-05-14/environment.mat', 'i')
display('Saved')

% Display the signal and the spectrogram
figure(1)
plot(x)
figure(2)
spectrogram(x, chebwin(win), over, nFFT, Fs)

%%
% Pass to the algorithm
figure(3)
stft(recording, win, over, nFFT, Fs);