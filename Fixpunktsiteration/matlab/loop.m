% Fixpunkt iteration med loop

% Ett godtycklig gissning på x
x_gues = 2;

% Kör 10 itersoner med x_gues som start värde
for n = 1:1000
    x_gues = FixedPointIteration(x_gues);
end

disp(x_gues)


% Utryck som ska undersökas
function x = FixedPointIteration(xn)
    % x^2 - x - 1 = 0 => x = 1 + (1/x)
    x = 1 + (1/xn);
end


