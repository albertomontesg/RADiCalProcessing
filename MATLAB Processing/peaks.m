
% Fs=22e3;
% load('audio.mat');
v = randi([3,35],10,1);
t0 = randi([0,10],10,1);
[X,Fs]=generate(v, t0, 20, 1);
[S,F,T,P] = spectrogram(X, 256, 128, 512, Fs);
psd = 10*log10(abs(S*1e3));

figure(1)
psd_t = psd(:,429);
subplot(1,1,1)
plot(F,psd_t)
hold on

[mu, sig]=normfit(psd_t, 1e-3);
thresehold = mu+3*sig;

[pks,locs,W]=findpeaks(psd_t,F,'MinPeakWidth', 0, 'MinPeakHeight', thresehold);
text(locs+.02,pks,strcat(num2str((1:numel(pks))'),num2str(W,'%.2f')))

sum(pks>thresehold)
plot(F, thresehold*ones(size(F,1)), '-r')
hold off


%%
subplot(2,1,2)
plot(unwrap(angle(S(:,429))))

%%
% Inizialize peaks
pks = zeros(size(P));
bw = zeros(size(P));
for i=1:size(psd,2)
    [mu, sig]=normfit(P(:,i), 1e-3);
    thresehold = mu+3*sig;
    [pk, loc, b] = findpeaks(abs(P(:,i)), F, 'MinPeakWidth', 0, 'MinPeakHeight', thresehold);
    for j=1:length(loc)
        pks(loc(j)==F,i) = pk(j);
        bw(loc(j)==F,i) = b(j);
    end
end
figure(2)
surf(T,F,10*log10(abs(pks*1e3)))
xlabel('time (s)')
ylabel('frequency (Hz)')
zlabel('PSD (dBm)')

figure(3)
surf(T,F,bw)
xlabel('time (s)')
ylabel('frequency (Hz)')
zlabel('Bandwidth (Hz)')
