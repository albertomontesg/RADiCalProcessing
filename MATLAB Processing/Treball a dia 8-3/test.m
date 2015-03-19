
T = 0:0.001:2;
X = chirp(T,0,1,150);
[S,F,T,P] = spectrogram(X(1:400),256,250,256,1E3);
Length=1.868;
figure(1)
sf = surf(T,F,abs(S));
sf.EdgeColor = 'none';

view(0,90);
axis([T(1), Length, F(1), F(end)]);
set(sf, 'ZData', abs(S))
xlabel('Time (s)')
ylabel('Frequency (Hz)')
title('Linear chirp')

for i=1:5
    [S,F,T,P] = spectrogram(X(1:(400*i)),256,250,256,1E3);
    set(sf, 'XData', T)
    set(sf, 'YData', F)
    set(sf, 'ZData', abs(S))
    
    pause(0.5)
    
    drawnow
    
end

