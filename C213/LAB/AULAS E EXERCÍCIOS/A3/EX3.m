clear all
clc

sys = tf([6],[450 3])

sys1 = feedback(sys,1)

step(sys1)

% K = 0.667
% T = 49
% ta = 196