import cmath

print(f'This is almighty formula')
a = int(input(f'input the value for a'))
b = int(input(f'input thr value for b'))
c = int(input(f'input the value for c'))

z = cmath.sqrt((pow(b,2))) - (4 * a * c)

r1 = ((-b) - z)/(2*a)
r2 = ((-b) + z)/(2*a)

print(f'roots are {r1} and {r2}')