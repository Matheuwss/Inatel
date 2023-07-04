clear all
clc

%A) SEM PERTURBA��O (MATLAB)
sys1 = tf([10], [2 1])
sys2 = series(3, sys1)

sys3 = feedback(sys2, 1)
step(sys3)


%T -> 2/31 = 0.0645
%K -> 30/31 = 0.9677
%Valor final -> Vo(s)= lim s * 1/s * 30/2s+31   ->   Vo(s)= 1*30/31 = 0.9677

%Erro -> Vo(s) - Vi(s)  -> 0.9677 - 1 = -0.0323

%B)COM PERTURBA��O (SIMULINK)
%Valor final -> 1.29
%Erro -> 0,29