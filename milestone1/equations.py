# STEP 1: parse the equation to extract the coefficients a, b, c

eq = 'x^2 +4x +    (-8) =  0'
eq = ''.join(eq.split(' '))
eq = f'|{eq[:-2]}|'  # slice the equation to shorten it, mark boundaries
eq = eq.replace('|x^2', '1x^2').replace('|-x^2', '-1x^2')  # set 1 if no a
eq = eq.replace('+x', '+1x').replace('-x', '-1x')  # set 1 if no b
eq = eq.replace('x^2|', 'x^2+0+0').replace('x|', 'x+0')  # set 0 if no bx or c
eq = eq.replace('(', '').replace(')', '').replace('|', '')  # remove extra char
a, bc = eq.split('x^2')  # extract a
bc = bc.replace('x', ' ').replace('+', ' ')  # prepare to split the rest
a = int(a)
b = int(bc.split()[0])
c = int(bc.split()[1])

# STEP 2: calculate the answer

x1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
print(f'The roots of the equation are {x1} and {x2}')
