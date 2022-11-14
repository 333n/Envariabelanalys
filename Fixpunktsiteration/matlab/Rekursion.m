% Fixpunkt iteration med Rekursion 


% Ett godtycklig gissning på x
x_gues = 2;
% Kör 50 iteration med x_gues som start värde
FixedPointIteration(x_gues, 50)


% Utryck som ska undersökas
% x^2 - x - 1 = 0 => x = 1 + (1/x)
function xr = FixedPointIteration(xn, iteration)
    x = 1 + (1/xn);
    
    if iteration <= 0
        xr = x;
    else 
        xr = FixedPointIteration(x, iteration-1);
    end
end


