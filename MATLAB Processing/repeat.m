tmp = load('Samples 2015-04-28/environment.mat');
i = tmp.i;
i = i -1;
display(strcat('Back to capture number ', int2str(i)))
save('Samples 2015-04-28/environment.mat', 'i')