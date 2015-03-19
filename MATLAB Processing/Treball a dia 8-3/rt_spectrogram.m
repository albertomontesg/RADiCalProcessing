
lattency = 0.2; %seconds
T = 5; %seconds: Temporal Window
Fs = 22e3; %22KHz
spf = Fs*lattency;

AR = dsp.AudioRecorder('OutputNumOverrunSamples',true,...
    'SampleRate', Fs, 'NumChannels', 1, 'SamplesPerFrame', spf);

audio = zeros(1,T*Fs+1);
t = -T:1/Fs:0;



for i=1:50
    [audioIn,nOverrun] = step(AR);
    audio(2:(end-spf)) = audio(spf+2:end);
    audio((end-spf+1):end) = audioIn;
    
    t = t + lattency;
    
    figure(1)
    plot(t,audio)
    axis([t(1),t(end),-2.5,2.5])
    xlabel('time (s)')
    ylabel('amplitude')
    title('Real Time Sound Recording')
    
    drawnow
end

spectrogram(audio, 256, 128, 256, Fs)


