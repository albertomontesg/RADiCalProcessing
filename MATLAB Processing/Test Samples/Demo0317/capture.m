lattency = 0.2; %seconds
T = 5; %seconds: Temporal Window
Fs = 44.1e3; %22KHz
spf = Fs*lattency;

AR = dsp.AudioRecorder('OutputNumOverrunSamples',true,...
    'SampleRate', Fs, 'NumChannels', 1, 'SamplesPerFrame', spf);
AR.DeviceName = 'Built-in Input';

audio = zeros(1,T*Fs+1);
t = -T:1/Fs:0;
save = [];
for i=1:100
    [audioIn,nOverrun] = step(AR);
    audio(2:(end-spf)) = audio(spf+2:end);
    audio((end-spf+1):end) = audioIn;
    save = [save; audioIn];
    t = t + lattency;
    
    figure(1)
    plot(t,audio)
    axis([t(1),t(end),-.2,.2])
    xlabel('time (s)')
    ylabel('amplitude')
    title('Real Time Sound Recording')
    
    drawnow
end

figure(2)
spectrogram(audio, 2048, 1024, 2048, Fs)

soundsc(audio, Fs)