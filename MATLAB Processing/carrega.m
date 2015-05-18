function [ x ] = carrega(j)
s = int2str(j);
y = load(strcat('sample',s,'.mat'));
x = y.x;
x = x - mean(x);
end

