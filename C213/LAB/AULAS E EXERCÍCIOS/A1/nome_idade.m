clear all
clc

N = input('Nome: ','s');
I = input('Idade :');

if I < 18 || I > 67
    fprintf('Não é permitida a doação %s')
else
    fprintf('É permitida a doação')
end