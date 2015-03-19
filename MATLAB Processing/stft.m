%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%              Short-Time Fourier Transform            %
%               with MATLAB Implementation             %
%                                                      %
% Author: M.Sc. Eng. Hristo Zhivomirov       12/21/13  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [stft, f, t] = stft(x, wlen, h, nfft, fs)
close all;
% function: [stft, t, f] = mystftfun(x, fs, wlen, h, nfft)
% x - signal in the time domain
% wlen - length of the hamming window
% h - hop size
% nfft - number of FFT points
% fs - sampling frequency, Hz
% f - frequency vector, Hz
% t - time vector, s
% stft - STFT matrix (time across columns, freq across rows)

% represent x as column-vector if it is not
if size(x,2) > 1
    x = x';
end

% length of the signal
xlen = length(x);

% form a periodic hamming window
%win = hamming(wlen, 'periodic');
%Changed to Chebyshev window
win = chebwin(wlen);

% form the stft matrix
rown = ceil((1+nfft)/2);            % calculate the total number of rows
coln = 1+fix((xlen-wlen)/h);        % calculate the total number of columns
stft = zeros(rown, coln);           % form the stft matrix

% initialize the indexes
indx = 0;
col = 1;

% perform STFT
while indx + wlen <= xlen
    % windowing
    xw = x(indx+1:indx+wlen).*win;
    
    % FFT
    X = fft(xw, nfft);
    
    %Plot
    K = length(X);
    threshold = 60;
    f_plot = (1:floor(K/2))*fs/K;
    f_plot = f_plot(f_plot < 7000); %Limit of f axis is 7KHz.
    FFT = 20*log(abs(X(1:length(f_plot),1))); %FFT dB.
    figure(1);
    plot(f_plot,FFT,f_plot, threshold*ones(length(f_plot)),'-r');
    axis([0 max(f_plot) 0 20*log(500)]);

    %[pks,locs]=findpeaks(FFT,f_plot,'MinPeakWidth', 0, 'MinPeakHeight', 0);
    [pks,locs]=findpeaks(FFT);

    locs = locs(pks > threshold);
    pks = pks(pks > threshold);
    if(pks>0) 
        display(locs);
    end

    str1 = '\leftarrow cotxe';
    text(locs+.02,pks,str1);
    drawnow


    
    
    
    % update the stft matrix
    stft(:,col) = X(1:(rown));
    
    % update the indexes
    indx = indx + h;
    col = col + 1;
    
    %Display the time
    display(indx/fs);
    %if(indx/fs < 0.75)
        %pause(0.01);
    %else
    %    pause(0.15);
    
end

% calculate the time and frequency vectors
t = (wlen/2:h:xlen-wlen/2-1)/fs;
f = (0:rown-1)*fs/nfft;

end