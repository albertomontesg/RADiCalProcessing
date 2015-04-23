nFFT = 4096;   % Length of the FFT to characterize the noise

[S, F, T, P] = spectrogram(signal, chebwin(nFFT), nFFT/2, nFFT, Fs);

psd = mean(P,2);
plot(F, 10*log10(psd))
