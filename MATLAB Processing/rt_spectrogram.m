
lattency = 0.2; %seconds
T = 5; %seconds: Temporal Window
total=30; %seconds
Fs = 8e3; %22KHz
spf = 512;

AR = dsp.AudioRecorder('OutputNumOverrunSamples',true,...
    'SampleRate', Fs, 'NumChannels', 1, 'SamplesPerFrame', spf);
AR.DeviceName = 'USB Audio CODEC';

audio = zeros(1,T*Fs+1);
recording = zeros(1,total*Fs);
t = -T:1/Fs:0;
f = (0:511)/512 * Fs;
win = chebwin(spf);

for i=0:(floor(total*Fs/spf))
    [audioIn,nOverrun] = step(AR);
    audio(2:(end-spf)) = audio(spf+2:end);
    audio((end-spf+1):end) = audioIn;
    recording(1+i*spf:(i+1)*spf) = audioIn;
    t = t + lattency;
    
%     figure(1)
%     plot(t,audio)
%     axis([t(1),t(end),-1,1])
%     xlabel('time (s)')
%     ylabel('amplitude')
%     title('Real Time Sound Recording')
    
    
    x = audioIn .* win;
    X = 20*log10(abs(fft(x, 512)));
    figure(2)
    plot(f, X)
    axis([f(1), f(end), -40, 0])
    xlabel('frequency (Hz)')
    ylabel('FFT Amplitud')
    title('Real time FFT')
    
    drawnow
end

% figure(2)
% spectrogram(audio, 2048, 1024, 2048, Fs)

%soundsc(audio, Fs)
