import math
from solving_discriminant import solve_discriminant, get_nature_of_root

def solve_roots(a, b, c):
    x_sub_1 = (-b - math.sqrt(b**2 - (4 * (a * c)))) / (2 * a)
    x_sub_2 = (-b + math.sqrt(b**2 - (4 * (a * c)))) / (2 * a)

    return {'x_sub_1': math.trunc(x_sub_1), 'x_sub_2': math.trunc(x_sub_2)}

def print_solution(a, b, c):
    roots = solve_roots(a, b, c)
    x_sub_1 = roots['x_sub_1']
    x_sub_2 = roots['x_sub_2']
    discriminant = solve_discriminant(a, b, c)

    print(f'a = {a}, b = {b}, c = {c}   This is what is given to us')
    print('-b \u00B1 square root of b\u00b2 - 4ac / 2a   This is the quadratic equation, this is what we\'re gonna use to find our roots')
    print('')
    print('Firstly. Let\'s predict what the outcome would look like by solving the discriminant')
    print('b\u00b2 - 4ac   Discriminant equation')
    print(f'{b}\u00b2 - 4({a})({c})   Let\'s subtitute it with the variables given to us')
    print(f'{b**2} - 4({a})({c})   Now let\'s do the first part {b}\u00b2 ({b} x {b}) = {b**2}')
    print(f'{b**2} - 4 x {a * c}   After that, {a} x {c} = {a*c}')
    print(f'{b**2} - {4 * (a * c)}   Then, 4 x {a * c} = {4 * (a * c)}')
    print(f'{discriminant}   Finally, {b**2} - {4 * (a * c)} = {discriminant}. We get our final answer for the discrimnant!')
    print('')
    print(f'For the nature of root. It is \"{get_nature_of_root(discriminant).title()}\", because...')
    print('If the discriminant is 0, it is \"Real And Equal\"')
    print('If the discriminant is above 0, it is \"Real And Unequal\"')
    print('If the discriminant is below 0, it is \"Unequal\"')
    print(f'{discriminant} = {get_nature_of_root(discriminant).title()}')
    print('')
    print('Now let\'s get the roots!')
    print('Let\'s find x\u2081 first')
    print('')
    print('x\u2081 = -b - square root of b\u00b2 - 4ac / 2a   Equation for x\u2081')
    print(f'x\u2081 = -{b} - square root of {b}\u00b2 - 4({a})({c}) / 2({a})   Now let\'s subtitute')
    print(f'x\u2081 = -{b} - square root of {discriminant} / 2({a})   Since we\'ve already solved the discriminant ({discriminant}), we can just replace that')
    print(f'x\u2081 = -{b} - square root of {discriminant} / {2 * a}   Let\'s do the divisor 2 x {a} = {2 * a}')
    print(f'x\u2081 = -{b} - {math.trunc(math.sqrt(discriminant))} / {2 * a}   The square root of {discriminant} = {math.trunc(math.sqrt(discriminant))}')
    print(f'x\u2081 = {math.trunc(-b - math.sqrt(discriminant))} / {2 * a}   Now let\'s do the dividend. -{b} - {math.trunc(math.sqrt(discriminant))} = {math.trunc(-b - math.sqrt(discriminant))}')
    print(f'x\u2081 = {x_sub_1}   Finally. A simple one! {math.trunc(-b - math.sqrt(discriminant))} / {2 * a} = {x_sub_1}')
    print('')
    print('For x\u2082. We do the same thing, but we replace \u00B1 to + this time')
    print('x\u2082 = -b + square root of b\u00b2 - 4ac / 2a   Equation for x\u2081')
    print(f'x\u2082 = -{b} + square root of {b}\u00b2 - 4({a})({c}) / 2({a})   Now let\'s subtitute')
    print(f'x\u2082 = -{b} + square root of {discriminant} / 2({a})   Since we\'ve already solved the discriminant ({discriminant}), we can just replace that')
    print(f'x\u2082 = -{b} + square root of {discriminant} / {2 * a}   Let\'s do the divisor 2 x {a} = {2 * a}')
    print(f'x\u2082 = -{b} + {math.trunc(math.sqrt(discriminant))} / {2 * a}   The square root of {discriminant} = {math.trunc(math.sqrt(discriminant))}')
    print(f'x\u2082 = {math.trunc(-b + math.sqrt(discriminant))} / {2 * a}   Now let\'s do the dividend. -{b} + {math.trunc(math.sqrt(discriminant))} = {math.trunc(-b + math.sqrt(discriminant))}')
    print(f'x\u2082 = {x_sub_2}   Finally. A simple one! {math.trunc(-b - math.sqrt(discriminant))} / {2 * a} = {x_sub_2}')
    print('')
    print('Finally, We got them!')
    print('x\u2081 ({}) + x\u2082 ({}) = {}'.format(x_sub_1, x_sub_2, x_sub_1 + x_sub_2))
    print('x\u2081 ({}) x x\u2082 ({}) = {}'.format(x_sub_1, x_sub_2, x_sub_1 * x_sub_2))

if __name__ == '__main__':
    try:
        a = int(input('A: '))
        b = int(input('B: '))
        c = int(input('C: '))
        show_solution = input('Show solution? (y/n): ').lower()

        roots = solve_roots(a, b, c)
        x_sub_1 = roots['x_sub_1']
        x_sub_2 = roots['x_sub_2']

        discriminant = solve_discriminant(a, b, c)
        nature_of_root = get_nature_of_root(discriminant)

        print('\nX\u2081 = {}\nX\u2082 = {}'.format(x_sub_1, x_sub_2))
        print('X\u2081 + X\u2082 = {}'.format(x_sub_1 + x_sub_2))
        print('X\u2081 x X\u2082 = {}'.format(x_sub_1 * x_sub_2))
        print('Discriminant: {}\nNature of root: {}'.format(discriminant, nature_of_root.title()))

        if show_solution == 'y' or show_solution == 'yes':
            print('\n-------------------- SOLUTION --------------------')
            print_solution(a, b, c)
    except ValueError:
        print('\nPlease only put numbers for A, B & C!')
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')
