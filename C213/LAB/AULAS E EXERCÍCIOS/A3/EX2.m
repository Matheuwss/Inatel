clear all
clc

sys = tf([0.5],[10 0.5])
step(sys*2)

% K = 1
% T = 20
% ta = 60