%entrada de dados em uma matriz
clear
clc

coluna= input ('numero de colunas do vetor: \n');

for i = 1:coluna
        mat(i) = input ('digite un numero: \n');
end

mat

for i = 1:coluna
        nova(i) = mat(coluna+1-i);
end

nova