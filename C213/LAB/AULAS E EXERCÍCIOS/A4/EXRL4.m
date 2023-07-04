clear all
clc

sys = tf([1], [1 0.56 0])
mf = feedback(sys, 1)
%step(mf)

%salvando os valoes do gráfico EM UMA VARIÁVEL, p/ obter valores de
%desejados (neste caso, de pico)
s = step(mf)
pico = 0;

for i=1:length(s)
    if s(i)>pico
        pico = s(i);
    end
end

pico