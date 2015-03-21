lattency = 0.2; %seconds
T = 5; %seconds: Temporal Window
Fs = 44.1e3; %22KHz
spf = Fs*lattency;
TotalTime = 10; %seconds

AR = dsp.AudioRecorder('OutputNumOverrunSamples',true,...
    'SampleRate', Fs, 'NumChannels', 1, 'SamplesPerFrame', spf,...
    'DeviceDataType', '16-bit integer');
AR.DeviceName = 'Built-in Microph';

audio = zeros(1,T*Fs+1);
t = -T:1/Fs:0;
save = zeros(1,TotalTime*Fs);
for i=1:(TotalTime*Fs/spf)
    [audioIn,nOverrun] = step(AR);
    audio(2:(end-spf)) = audio(spf+2:end);
    audio((end-spf+1):end) = audioIn;
    save((i-1)*spf+1:i*spf)= audioIn;
    t = t + lattency;
    
    figure(1)
    plot(t,audio)
    axis([t(1),t(end),-1,1])
    xlabel('time (s)')
    ylabel('amplitude')
    title('Real Time Sound Recording')
    
    drawnow
end

figure(2)
spectrogram(audio, 2048, 1024, 2048, Fs)

soundsc(audio, Fs)