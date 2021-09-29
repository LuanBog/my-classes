#!/usr/bin/env python

import math
from fractions import Fraction

def get_nature_of_root(number):
    if number == 0:
        return 'real and equal'
    elif number > 0:
        return 'real and unequal'
    else:
        return 'unreal'

def solve_discriminant(a, b, c):
    first = (b ** 2)
    second = 4 * (a * c)
    discriminant = first - second
    
    return discriminant

def solve_roots(a, b, c):
    x_sub_1 = (-b - math.sqrt(b**2 - (4 * (a * c)))) / (2 * a)
    x_sub_2 = (-b + math.sqrt(b**2 - (4 * (a * c)))) / (2 * a)

    # Checks if they're a whole number, if not, that usually means we should make them to a fraction
    if not float(x_sub_1).is_integer():
        x_sub_1 = Fraction(math.trunc((-b - math.sqrt(b**2 - (4 * (a * c))))), math.trunc((2 * a)))
    else:
        x_sub_1 = math.trunc(x_sub_1)
    
    if not float(x_sub_2).is_integer():
        x_sub_2 = Fraction(math.trunc((-b + math.sqrt(b**2 - (4 * (a * c))))), math.trunc((2 * a)))
    else:
        x_sub_2 = math.trunc(x_sub_2)

    return {'x_sub_1': x_sub_1, 'x_sub_2': x_sub_2}

def print_solution(a, b, c):
    roots = solve_roots(a, b, c)
    x_sub_1 = roots['x_sub_1']
    x_sub_2 = roots['x_sub_2']

    discriminant = solve_discriminant(a, b, c)
    nature_of_root = get_nature_of_root(discriminant)

    print(f'a = {a}, b = {b}, c = {c}   This is what is given to us')
    print('-b \u00B1 square root of(b\u00b2 - 4ac) / 2a   This is the quadratic equation, this is what we\'re gonna use to find our roots')
    print('')
    print('Firstly. Let\'s solve the discriminant, because that will show us the nature of roots')
    print('b\u00b2 - 4ac   Discriminant equation')
    print(f'{b}\u00b2 - 4({a})({c})   Let\'s subtitute it with the variables given to us')
    print(f'{b**2} - 4({a})({c})   Now let\'s do the first part {b}\u00b2 ({b} x {b}) = {b**2}')
    print(f'{b**2} - 4 x {a * c}   After that, {a} x {c} = {a*c}')
    print(f'{b**2} - {4 * (a * c)}   Then, 4 x {a * c} = {4 * (a * c)}')
    print(f'{discriminant}   Finally, {b**2} - {4 * (a * c)} = {discriminant}. We get our final answer for the discrimnant!')
    print('')
    print(f'For the nature of root. It is \"{nature_of_root.title()}\", because...')
    print('If the discriminant is 0, it is \"Real And Equal\"')
    print('If the discriminant is above 0, it is \"Real And Unequal\"')
    print('If the discriminant is below 0, it is \"Unreal\"')
    print(f'{discriminant} = {nature_of_root.title()}')
    if nature_of_root == 'real and equal':
        print('Because our nature of root is "{}". This tells us that x\u2081 and x\u2082 are going to be equal'.format(nature_of_root.title()))
    elif nature_of_root == 'real and unequal':
        print('Because our nature of root is "{}". This tells us that x\u2081 and x\u2082 are going to be different'.format(nature_of_root.title()))
    else:
        print('{}... Too complex for me right now... This is so unreal'.format(nature_of_root.title()))
    print('')
    print('Now let\'s get the roots!')
    print('')
    print('Let\'s find x\u2081 first')
    print('x\u2081 = -b - square root of(b\u00b2 - 4ac) / 2a   Equation for x\u2081')
    print(f'x\u2081 = -{b} - square root of({b}\u00b2 - 4({a})({c})) / 2({a})   Now let\'s subtitute')
    print(f'x\u2081 = -{b} - square root of({discriminant}) / 2({a})   Since we\'ve already solved the discriminant ({discriminant}), we can just replace {b}\u00b2 - 4({a})({c})')
    print(f'x\u2081 = -{b} - square root of({discriminant}) / {2 * a}   Let\'s do the divisor 2 x {a} = {2 * a}')
    print(f'x\u2081 = -{b} - {math.trunc(math.sqrt(discriminant))} / {2 * a}   The square root of {discriminant} = {math.trunc(math.sqrt(discriminant))}')
    print(f'x\u2081 = {math.trunc(-b - math.sqrt(discriminant))} / {2 * a}   Now let\'s do the dividend. -{b} - {math.trunc(math.sqrt(discriminant))} = {math.trunc(-b - math.sqrt(discriminant))}')
    if type(x_sub_1) != Fraction:
        print(f'x\u2081 = {x_sub_1}   Finally. A simple one! {math.trunc(-b - math.sqrt(discriminant))} / {2 * a} = {x_sub_1}')
    else:
        print(f'x\u2082 = {x_sub_1}   Finally. Since {math.trunc(-b - math.sqrt(discriminant))} / {2 * a} = {(-b - math.sqrt(discriminant)) / (2 * a)} (a decimal number). Let\'s leave it as it is {x_sub_1}')
    print('')
    print('For x\u2082. We do the same thing, but we replace \u00B1 to + this time')
    print('x\u2082 = -b + square root of(b\u00b2 - 4ac) / 2a   Equation for x\u2082')
    print(f'x\u2082 = -{b} + square root of({b}\u00b2 - 4({a})({c})) / 2({a})   Now let\'s subtitute')
    print(f'x\u2082 = -{b} + square root of({discriminant}) / 2({a})   Since we\'ve already solved the discriminant ({discriminant}), we can just replace {b}\u00b2 - 4({a})({c})')
    print(f'x\u2082 = -{b} + square root of({discriminant}) / {2 * a}   Let\'s do the divisor 2 x {a} = {2 * a}')
    print(f'x\u2082 = -{b} + {math.trunc(math.sqrt(discriminant))} / {2 * a}   The square root of {discriminant} = {math.trunc(math.sqrt(discriminant))}')
    print(f'x\u2082 = {math.trunc(-b + math.sqrt(discriminant))} / {2 * a}   Now let\'s do the dividend. -{b} + {math.trunc(math.sqrt(discriminant))} = {math.trunc(-b + math.sqrt(discriminant))}')
    if type(x_sub_2) != Fraction:
        print(f'x\u2082 = {x_sub_2}   Finally. A simple one! {math.trunc(-b - math.sqrt(discriminant))} / {2 * a} = {x_sub_2}')
    else:
        print(f'x\u2082 = {x_sub_2}   Finally. Since {math.trunc(-b - math.sqrt(discriminant))} / {2 * a} = {(-b - math.sqrt(discriminant)) / (2 * a)} (a decimal number). Let\'s leave it as it is {x_sub_2}')
    print('')
    print('Finally, now that we got them, we can solve \"the sum of the roots\" and \"the product the of roots\"')
    print('x\u2081 ({}) + x\u2082 ({}) = {}'.format(x_sub_1, x_sub_2, x_sub_1 + x_sub_2))
    print('x\u2081 ({}) x x\u2082 ({}) = {}'.format(x_sub_1, x_sub_2, x_sub_1 * x_sub_2))

# Temporary function. Will be removed as soon as solving for unreal quadratic equations feature is made
def print_solution_discriminant_only(a, b, c):
    discriminant = solve_discriminant(a, b, c)
    nature_of_root = get_nature_of_root(discriminant)

    print('Here\'s how we get the discriminant')
    print('b\u00b2 - 4ac   Discriminant equation')
    print(f'{b}\u00b2 - 4({a})({c})   Let\'s subtitute it with the variables given to us')
    print(f'{b**2} - 4({a})({c})   Now let\'s do the first part {b}\u00b2 ({b} x {b}) = {b**2}')
    print(f'{b**2} - 4 x {a * c}   After that, {a} x {c} = {a*c}')
    print(f'{b**2} - {4 * (a * c)}   Then, 4 x {a * c} = {4 * (a * c)}')
    print(f'{discriminant}   Finally, {b**2} - {4 * (a * c)} = {discriminant}. We get our final answer for the discrimnant!')
    print('')
    print(f'For the nature of root. It is \"{nature_of_root.title()}\", because...')
    print('If the discriminant is 0, it is \"Real And Equal\"')
    print('If the discriminant is above 0, it is \"Real And Unequal\"')
    print('If the discriminant is below 0, it is \"Unreal\"')
    print(f'{discriminant} = {nature_of_root.title()}')
    if nature_of_root == 'real and equal':
        print('Because our nature of root is "{}". This tells us that x\u2081 and x\u2082 are going to be equal'.format(nature_of_root.title()))
    elif nature_of_root == 'real and unequal':
        print('Because our nature of root is "{}". This tells us that x\u2081 and x\u2082 are going to be different'.format(nature_of_root.title()))
    else:
        print('{}... Too complex for me right now... This is so unreal'.format(nature_of_root.title()))

def main():
    try:
        a = int(input('A: '))

        if a == 0:
           print('\nif a = 0, then it is not a quadratic equation!')
           return

        b = int(input('B: '))
        c = int(input('C: '))
        show_solution = input('Show solution? (y/n): ').lower()

        discriminant = solve_discriminant(a, b, c)
        nature_of_root = get_nature_of_root(discriminant)

        # Delete when solving for unreal quadratic equations is made
        if discriminant < 0:
            print('\nDiscriminant (b\u00b2 - 4ac): {}\nNature of root: {}'.format(discriminant, nature_of_root.title()))
            
            if show_solution == 'y' or show_solution == 'yes':
                print('\n---------------------------------------- SOLUTION ----------------------------------------')
                print('')
                print_solution_discriminant_only(a, b, c)

            print('\nDeveloper note: for \"Unreal\" quadratic equations. This requires 2 complex solutions which I have no idea how to do yet. Stay updated for that feature and good luck with math :D')
            return

        roots = solve_roots(a, b, c)
        x_sub_1 = roots['x_sub_1']
        x_sub_2 = roots['x_sub_2']

        print('\n---------------------------------------- RESULT ----------------------------------------')
        
        print('\nDiscriminant (b\u00b2 - 4ac): {}\nNature of root: {}'.format(discriminant, nature_of_root.title()))
        print('\nX\u2081 = {}\nX\u2082 = {}'.format(x_sub_1, x_sub_2))
        print('X\u2081 + X\u2082 = {}'.format(x_sub_1 + x_sub_2))
        print('X\u2081 x X\u2082 = {}'.format(x_sub_1 * x_sub_2))

        if show_solution == 'y' or show_solution == 'yes':
            print('\n---------------------------------------- SOLUTION ----------------------------------------')
            print('')
            print_solution(a, b, c)
    except ValueError:
        print('\nPlease only put numbers for A, B & C!')
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()
