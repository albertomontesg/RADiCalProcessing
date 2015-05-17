for i = 1:15
    s = int2str(i);
    y = load(strcat('sample',s,'.mat'));
    x = y.x;
    Fs = y.Fs;
    audiowrite(strcat('sample', int2str(i), '.wav'), x, Fs);
end