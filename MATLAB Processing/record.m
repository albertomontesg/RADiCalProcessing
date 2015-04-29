function [ x ] = record( time, Fs, nBits )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

recorder = audiorecorder(Fs, nBits, 1, 4);

disp('Start recording signal');
recordblocking(recorder, time);
disp('End of recording signal');

x = getaudiodata(recorder);

end

