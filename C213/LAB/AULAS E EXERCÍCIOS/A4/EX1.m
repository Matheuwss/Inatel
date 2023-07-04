clear all
clc

%A) FUN��O FINAL (MF)
sys1 = tf([1], [1 0.56 0])
sys2 = series(sys1, 4)
sys3 = feedback(sys2, 1)
step(sys3)

%B)
%Wn = raiz de 4 = 2 rad/s          
%Qsi = 0.56/2*2 = 0.14

%TEMPO DE ATRASO (td): 0.423s
%TEMPO DE SUBIDA(tr): 0.867s
%Tempo de pico: 1.57s
%M�ximo pico (m�ximo sobressinal ou apenas sobressinal): 0.64
%Tempo de acomoda��o (ts): 13.1s

%C) 60%
step(sys3*60)

%D) Erro = 0