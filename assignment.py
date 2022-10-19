import cmath
def print_area():
    print(f'we want to get the area of a circle')
    pi = 3.14
    radius = float(input(f'Enter your radius is'))
    area = pi * pow(radius, 2)
    print(f'Your area is {area}')


def change_yeas():
    time_in_years = input(f'Enter the proposed time in year')
    # since 1 year is approximately 315,360 sec
    time_in_sec = int(time_in_years) * 315360
    print(f'{time_in_years} years is equivalent to {time_in_sec}')


def quadratic(a, b, c):
    a = int(input(f'input the value for a'))
    b = int(input(f'input thr value for b'))
    c = int(input(f'input the value for c'))

    z = cmath.sqrt((pow(b, 2))) - (4 * a * c)

    r1 = ((-b) - z) / (2 * a)
    r2 = ((-b) + z) / (2 * a)

    print(f'roots are {r1} and {r2}')

