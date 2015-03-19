function [ output_args ] = smpl(s1,s2,s3)
%smpl Summary of this function goes here
%   Detailed explanation goes here

Fs=44100;
N1=length(s1);
N2=length(s2);
N3=length(s3);

n1=transpose(0:N1-1);
n2=transpose(0:N2-1);
n3=transpose(0:N3-1);

subplot(3,1,1);
plot(n1,s1)
title('Sample 1');
subplot(3,1,2);
plot(n2,s2)
title('Sample 2');

subplot(3,1,3);
plot(n3,s3)
title('Sample 3');

end

