function [  ] = rt_detection( x, Fs )
%rt_detection Given a long sample taken, for each temporal window finds and
%return the detected information.
%   Detailed explanation goes here

WLEN = 512;
H = WLEN/2;
NFFT = 1024;
threshold = 1e7;

DEBUG = false;


% represent x as column-vector if it is not
if size(x,2) > 1
    x = x';
end

% length of the signal
xlen = length(x);
% Chebyshev window
win = chebwin(WLEN);

% initialize the indexes
indx = 0;
col = 1;

% form the stft matrix
%rown = ceil((1+NFFT)/2);            % calculate the total number of rows
coln = 1+fix((xlen-WLEN)/H);        % calculate the total number of columns
%stft = zeros(rown, coln);           % form the stft matrix

f = (1:(NFFT/2))/NFFT*Fs;
S = zeros(1,(NFFT/2));

pl = 0;
if DEBUG == true
    figure(2)
    h = plot(f,S);
    axis([0, Fs/2, 0, 2]);
    pl = h;
end

figure(1)
f = zeros(1,coln);
g = plot(f);


while indx + WLEN <= xlen
    % windowing
    xw = x(indx+1:indx+WLEN).*win;
    
    [Fd, threshold] = detect(xw, NFFT, threshold, pl);
    
    f(col) = Fd;
    set(g, 'YData', f);
        
    drawnow
    % update the indexes
    indx = indx + H;
    col = col + 1;
end

