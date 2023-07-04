clear all
clc

load('dadosgrupo6.mat')

op = menu('QUAL O MÉTODO DESEJADO: ', 'CHR1', 'Integral do Erro')

if(op == 1)

    Kp = {'Insira o valor de KP'};
    KP = inputdlg(Kp);
    kp = str2num(char(KP(1)));

    Ti = {'Insira o valor de Ti'};
    TI = inputdlg(Ti);
    ti = str2num(char(TI(1)));

    Td = {'Insira o valor de Td'};
    TD = inputdlg(Td);
    td = str2num(char(TD(1)));

    sys = tf([4.8], [24 1])
    pid = pidstd(kp, ti, td)
    mf = feedback(sys*pid, 1)
    set(mf, 'INPUTDELAY', 14)
    step(mf*30)

else if (op == 2)
    
    Kp = {'Insira o valor de KP'};
    KP = inputdlg(Kp);
    kp = str2num(char(KP(1)));

    Ti = {'Insira o valor de Ti'};
    TI = inputdlg(Ti);
    ti = str2num(char(TI(1)));

    Td = {'Insira o valor de Td'};
    TD = inputdlg(Td);
    td = str2num(char(TD(1)));

    sys = tf([4.8], [24 1])
    pid = pidstd(kp, ti, td)
    mf = feedback(sys*pid, 1)
    set(mf, 'INPUTDELAY', 14)
    step(mf*30)

    end
end