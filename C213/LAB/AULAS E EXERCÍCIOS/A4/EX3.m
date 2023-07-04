clear all
clc

%Q3
%(A) Determine a fun��o de TRANSFER�NCIA DO SISTEMA.

%Degrau de amplitude 3
%Pico = 4.5 e TP = 1.2s

%Qsi = 0.2 (TABELA)
% Wd = ?/TP ---> 3.14/1.2 = 2.618
% Wn = 2.67

sys = tf([7.1289],[1 1.068 7.1289])
step(sys*3)

%(B) Calcule o erro em regime permanente p/ um degrau unit�rio.
% Erro = 1 - 1 = 0

%(C) Determine os par�metros do SISTEMA DE SEGUNDA ORDEM:
%TEMPO DE SUBIDA (tr): 0.679s
%TEMPO DE PICO (tp): 1.2s
%M�ximo pico (m�ximo sobressinal ou apenas sobressinal: 0.5
%Tempo de acomoda��o: 7.34s