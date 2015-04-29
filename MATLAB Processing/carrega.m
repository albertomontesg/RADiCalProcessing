function [ x ] = carrega(j)
s = int2str(j);
y = load(strcat('sample',s,'.mat'));
x = y.recording;
x = x - mean(x);
end

