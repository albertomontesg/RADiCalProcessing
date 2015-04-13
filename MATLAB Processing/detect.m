function [ Fd, threshold ] = detect( x, nfft, threshold, plot )
%detect Extract information from one sample's window
%   It makes the fft and then returns the frequencis where peaks over
%   the threshold are find

X = abs(fft(x, nfft));
%X = 20*log10(X);
X = X(1:nfft/2);

% Update threshold
pos = X<threshold;
mn = mean(X(pos));
st = std(X(pos));
threshold = (mn + 5*st);

[ampl,Fd]=findpeaks(X, 'MinPeakHeight', threshold);
if plot ~= 0
    set(plot, 'YData', X);
    
%     a = zeros(1,length(Fd));
%     display(ampl)
%     for i=1:length(Fd)
%         a(i) = annotation(plot, 'textarrow', [Fd(i), Fd(i)]*2/nfft, [ampl, ampl+.1]/2, ...
%             'String', 'Target');
%     end
    
    %delete(a)
end
if isempty(Fd) == false
    display(ampl)
    display(Fd)
    [M, I] = max(ampl);
    Fd = Fd(I);
else
    Fd = 0;
end

end