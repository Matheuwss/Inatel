clear all
clc

A = rand(4,5);
B = rand(4,5);

C = (A + B)*10

for i=1:4
    for j=1:5
        if C(i,j) > 10
            C(i,j)=0;
        else
        end
    end
end

C