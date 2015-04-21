%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%              Short-Time Fourier Transform            %
%               with MATLAB Implementation             %
%                                                      %
% Author: Processing Team                              %
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
threshold = 1000000;

while indx + wlen <= xlen
    % windowing
    xw = x(indx+1:indx+wlen).*win;
    
    % FFT
    X = fft(xw, nfft);
    
    %Plot
    K = length(X);
    
    f_plot = (1:floor(K/2))*fs/K;
    f_plot = f_plot(f_plot < 1000); %Limit of f axis is 7KHz.
    fft_x = abs(X(1:length(f_plot),1));
    fft_x = 10*log10(fft_x); %FFT dB.
    figure(1);
    
    %threshold = 60;
    pos = fft_x<threshold;
    mn = mean(fft_x(pos));
    st = std(fft_x(pos));
    threshold = (mn + 5*st);
    
    plot(f_plot,fft_x,f_plot, threshold*ones(length(f_plot)),'-r');
%     
%     if indx == 0
%         d = plot(f_plot,FFT,f_plot, threshold*ones(length(f_plot)),'-r');
%     else
%         set(d, 'YData', FFT);
%         %set(d(2), 'YData', threshold*ones(length(f_plot)));
%     end
    axis([0 max(f_plot) -30 20]);

    %[pks,locs]=findpeaks(FFT,f_plot,'MinPeakWidth', 0, 'MinPeakHeight', 0);
    [pks,locs]=findpeaks(fft_x, 'MinPeakHeight', threshold);

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