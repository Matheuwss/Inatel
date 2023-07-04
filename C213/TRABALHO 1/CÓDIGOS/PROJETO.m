clear all
clc

load('dadosgrupo6.mat')

%DADOS/CÁLCULOS:
%Vi(s) = 30        Vo(s) = 143.938(ou 144)        Atraso(θ) = 14

%Vo(s)= lim s * H(s) * Vi(s)		    Fazendo s -> 0, temos:
%       s-> 0

%K = Vo(s) / Vi(s)
%K = 144 / 30
%K = 4.8


%FUNÇÃO (Com o valores obtidos pelo método de SMITH)
sys_ma = tf([4.8], [24 1], 'INPUTDELAY', 14)    %Com atraso
step(sys_ma*30)

sem_atraso = tf([4.8], [24 1])                  %Sem atraso (P/ CONSEGUIR USAR A FUNÇÃO FEEDBACK)
sys_mf = feedback(sem_atraso, 1)
set(sys_mf, 'INPUTDELAY', 14)
%step(sys_mf*30)

hold on                 %Retém as plotagens nos eixos atuais p/ que as novas plotagens adicionadas aos eixos não excluam as plotagens existentes
plot(t, saida,'r--')
hold off                %Define o estado de retenção como desativado p/ que os novos gráficos adicionados aos eixos limpem os gráficos existentes e redefinam todas as propriedades dos eixos.



%----------------------- CHR1 -----------------------
%sys = tf([4.8], [24 1], 'INPUTDELAY', 14)
%pid = pidstd(0.2143, 24, 7)                        %Sem ajuste
%mf = feedback(sys*pid, 1)
%step(mf*30)

%sys = tf([4.8], [24 1], 'INPUTDELAY', 14)
%pid = pidstd(0.12, 24, 2)                          %Com ajuste
%mf = feedback(sys*pid, 1)
%step(mf*30)

%----------------- Integral do Erro -----------------
%sys = tf([4.8], [24 1], 'INPUTDELAY', 14)
%pid = pidstd(0.266, 29.02, 0.2667)                 %Sem ajuste
%mf = feedback(sys*pid, 1)
%step(mf*30)

%sys = tf([4.8], [24 1], 'INPUTDELAY', 14)
%pid = pidstd(0.215, 29.02, 0.2667)                 %Com ajuste
%mf = feedback(sys*pid, 1)
%step(mf*30)