function [ x, Fs ] = generate(v, t0 ,SNR, n)
%GENERATE2 Summary of this function goes here
%   n = 0, no noise. n=1, adds noise.
f0 = 10.525e9;
c = 3e8;
Fs=44.1e3; %Hz
N0 = 10e-9*Fs;
A = sqrt(10^(SNR/10)*N0); %Amplitud de senyal
T=10; %segons
t = 0:1/Fs:T;
x = normrnd(0,N0,1,length(t))*n;

lambda = c/f0;
fd = -2/lambda.*v;
d = 12./v;
smoothness = 1/3;
for i = 1:length(d)
    u(i,:) = (atan((t-t0(i)+d(i)/2)/smoothness) + pi/2)/pi - (atan((t-t0(i)-d(i)/2)/smoothness) + pi/2)/pi; 
    u(i,:) = u(i,:)/max(u(i,:)); %Normalitzaci? de la pot?ncia
    
end

a = A*u;

for i= 1:length(v)
    x = x+a(i,:).*sin(2*pi*fd(i)*(t>=t0(i)-d(i)/2).*(t<=t0(i)+d(i)/2).*t);
end
figure(10)
subplot(2,2,1)
plot(t,x);
subplot(2,2,2)
plot(abs(fft(x)))
subplot(2,2,3)
spectrogram(x,256,128,256,Fs);
view([0 0]);
title('Power vs Frequency')

subplot(2,2,4)
spectrogram(x,256,128,256,Fs);
view([90 0]);
title('Power vs Time')

%sound(x,Fs);

end

