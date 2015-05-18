x=[];
for i=1:15
    temp = carrega(i);
    x = [x', temp']';
end
Fs = 44100;
audiowrite(strcat('allSamples.wav'), x, Fs);