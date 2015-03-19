clc;clear; close all;
Fs=44.1e3;
load('sample1.mat');
load('sample2.mat');
load('sample3.mat');
smpl(sample1,sample2,sample3);

%sound(sample1,Fs)

%espectrograma mostra 1

figure(2);
suptitle('Sample 1 spectrogram');

subplot(2,1,1)

spectrogram(sample1,chebwin(256),128,256,Fs);
view([0 0]);
 
subplot(2,1,2)
spectrogram(sample1,chebwin(256),128,256,Fs);
view([90 0]);


%espectrograma mostra 2
%{
figure(3)

title('Sample 2 Espectrogram')
subplot(2,1,1)
spectrogram(sample2,256,128,512,Fs);
view([0 0]);
 
subplot(2,1,2)
spectrogram(sample2,256,128,512,Fs);
view([90 0]);
%}


%{
espectrograma mostra 3
figure(4)

title('Sample 3 Espectrogram')
subplot(2,1,1)
spectrogram(sample3,256,128,512,Fs);
view([0 0]);
 
subplot(2,1,2)
spectrogram(sample3,256,128,512,Fs);
view([90 0]);
%}
