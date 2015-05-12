%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%              Short-Time Fourier Transform            %
%               with MATLAB Implementation             %
%                                                      %
% Author: Processing Team                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [stft, f, t, final_info] = stft(x, wlen, h, nfft, fs)
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

% enable resolution values
resolution_values = 1;
info = zeros(1,5); %5 cols, N_ped, N_veh, v_min, v_max, v_avg
Flimit = 1600;
F_generator = 9.65e9;
f_lim_ped = 200; %Frequency limit for assuming pedestrians

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


% arrange of plots
%figure();

%h1 = plot(x,x);
%hold on;
%h2 = plot(x,x);

mTextBox = uicontrol('style','text');
mTextBoxPosition = get(mTextBox,'Position');
set(mTextBox,'Position',[mTextBoxPosition + [400 310 10 0]]);



while indx + wlen < xlen
     
    % windowing and removing of mean
    xw = x(indx+1:indx+wlen).*win;
    xw = xw-mean(xw);
    
    % FFT
    X = fft(xw, nfft);
    
    %Plot
    K = length(X);
    
    f_plot = (1:floor(K/2))*fs/K;
    fft_x = abs(X(1:length(f_plot),1));
    
     % get resolution values
    if(resolution_values && col==1)
        freq_res = f_plot(2)-f_plot(1);
        display(freq_res);

        temp_res = wlen/fs;
        display(temp_res);
        pause(2);
    end
    
    
    %Threshold caluclation
    f_lim = 1500; %f_limit_change_ramp
    g = 10; %gain_form_change_to_0
    
    aux = 1:length(fft_x);
    pos = aux(fft_x'<threshold);  
    mn = mean(fft_x(pos(f_plot(pos)>f_lim)));
    st = std(fft_x(pos));
    threshold = (mn + 5*st);
    flat_threshold_dB = 20*log10(threshold); %threshold in dB.

   
    ramp_threshold_dB = flat_threshold_dB-g/f_lim*(f_plot-f_lim); %ramp threshold in dB.
    threshold_dB = max(ramp_threshold_dB, flat_threshold_dB*ones(1,length(f_plot)));
    
    
    %Show
    
    set(mTextBox,'String',strcat('Time = ',num2str(indx/fs)));
        
    f_plot = f_plot(f_plot < Flimit); %Limit of f axis is 5KHz.
    fft_x = fft_x(1:length(f_plot)); 
    FFT = 20*log10(fft_x); %FFT dB.
    threshold_plot = threshold_dB(1:length(f_plot));
    
    %set(h1,'XData',f_plot,'YData',FFT);
    %set(h2,'XData',f_plot,'YData', threshold_plot);
    %set(h2,'Color','red');
    drawnow;
    
    plot(f_plot,FFT,f_plot, threshold_plot,'-r');
    axis([0 max(f_plot) -80 50]);
    
    

    %[pks,locs]=findpeaks(FFT,f_plot,'MinPeakWidth', 0, 'MinPeakHeight', 0);
    %[pks,locs]=findpeaks(fft_x, 'MinPeakHeight', threshold);
    
    
    %Power from 0 to 200 Hz to estimate average number of pedestrians
    pos_ped = f_plot(f_plot<f_lim_ped);
    power_ped = sum(fft_x(length(pos_ped)));
    N_ped = 0*power_ped; %TBD
    
    %Power from 200 to 1.5KHz to estimate average number of vehicles
    integers = 1:length(f_plot);
    pos_vehicles = integers(f_plot>=f_lim_ped);
    power_vehicles = sum(fft_x(pos_vehicles));  
    N_veh = 0*power_vehicles; %TBD
    
    %Creation of PDF of velocities to estimate average speed of vehicles
    pdf_v = [zeros(1,length(pos_ped)) fft_x(pos_vehicles)']; %%ajustar lengths per al plot
    pdf_v = max(pdf_v, threshold);
    pdf_v = pdf_v - threshold;
    pdf_v = pdf_v/sum(pdf_v); %Normalization
    %plot(f_plot,pdf_v); pause(1);
    f_mean = (f_plot(1:length(pdf_v)))*pdf_v'; %Expected value
    %display(f_mean); pause(3);
    v_avg = f_mean*(3e8/(2*F_generator)*3.6);
    
    %Finding peaks
    
    [pks,locs]=findpeaks(FFT,'MinPeakHeight', 0);
    
    locs_2 = locs(pks' > threshold_dB(locs));
    pks_2 = pks(pks' > threshold_dB(locs));
    
    locs = locs_2;
    pks = pks_2; 
    
    v = (f_plot(locs)*3e8/(2*F_generator))*3.6;
    
    str1 = '\leftarrow objectiu a: ';
    str = cell(length(v),1);
    for i = 1:length(v)
        str{i} = strcat(str1,' ',num2str(v(i),2),'km/h');
        text(f_plot(locs(i)),pks(i),str{i});
        display(pks);
    end
    
    %Determining v_min & v_max
    v_min = max(min(v));
    v_max = max(max(v),0);
    if(size(v_min) == [1 0]) v_min = 0; end
    if(size(v_max) == [1 0])v_max = 0; end
    
    %UPDATES
    
    % update the stft matrix
    stft(:,col) = X(1:(rown));
    
    % update the indexes
    indx = indx + h;
    col = col + 1;
    
    % Gathering info
    aux2 = [N_ped N_veh v_min v_max v_avg];
    info = [info; aux2];
    
end
aux3 = info(:,3);
aux3 = aux3(aux3 > f_lim_ped*3e8/(2*F_generator)*3.6);
final_info = [mean(info(:,1)) mean(info(:,2)) min(aux3) max(info(:,4)) mean(info(:,5))];
display(final_info);
% calculate the time and frequency vectors
t = (wlen/2:h:xlen-wlen/2-1)/fs;
f = (0:rown-1)*fs/nfft;

end