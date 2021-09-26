def solve(a, b, c):
    first = (b ** 2)
    second = (4 * a) * c
    discriminant = first - second
    
    return discriminant

def get_full_discriminant_equation(a, b, c):
    return f'{b}\u00b2-4({a})({c})'

def get_nature_of_root(number):
    if number == 0:
        return 'real and equal'
    elif number > 0:
        return 'real and unequal'
    else:
        return 'unequal'

if __name__ == '__main__':
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))

    result = solve(a, b, c)
    nature_of_root = get_nature_of_root(result)
    full_discriminant_equation = get_full_discriminant_equation(a, b, c)

    print('Equation: b\u00b2-4ac\nSolved Equation: {} = {}\nNature of root: {}'.format(full_discriminant_equation, result, nature_of_root))
