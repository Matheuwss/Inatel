clear all
clc

%DADOS:
%Tempo de acomoda��o (ts): 2
%SOBRE PICO ENTRE 10 E 20%

%Portanto, consultando o gr�fico, Qsi = 0.5

%C�LCULOS:
%ts = 4 / Qsi * Wn   --> 2 = 4/0.5 * Wn
%Logo, Wn =  4


%FUN��O
sys = tf([16], [1 4 16])
step(sys)

%TEMPO DE ATRASO (td): 0.324s
%TEMPO DE SUBIDA(tr): 0.606s
%TEMPO DE PICO (tp): 0.898s