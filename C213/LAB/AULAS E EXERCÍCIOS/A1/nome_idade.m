clear all
clc

N = input('Nome: ','s');
I = input('Idade :');

if I < 18 || I > 67
    fprintf('N�o � permitida a doa��o %s')
else
    fprintf('� permitida a doa��o')
end