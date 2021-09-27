def solve_discriminant(a, b, c):
    first = (b ** 2)
    second = 4 * (a * c)
    discriminant = first - second
    
    return discriminant

def get_full_discriminant_equation(a, b, c):
    return f'{b}\u00b2 - 4({a})({c})'

def get_nature_of_root(number):
    if number == 0:
        return 'real and equal'
    elif number > 0:
        return 'real and unequal'
    else:
        return 'unreal'

def print_solution(a, b, c):
    result = solve_discriminant(a, b, c)

    print(f'a = {a}, b = {b}, c = {c}   This is what is given to us')
    print('b\u00b2 - 4ac   This is the equation we\'re working with')
    print(f'{get_full_discriminant_equation(a, b, c)}   Let\'s replace the variables with the the variables given to us')
    print(f'{b**2} - 4({a})({c})   Now let\'s do the first part {b}\u00b2 ({b} x {b}) = {b**2}')
    print(f'{b**2} - 4 x {a * c}   After that, {a} x {c} = {a*c}')
    print(f'{b**2} - {4 * (a * c)}   Then, 4 x {a * c} = {4 * (a * c)}')
    print(f'{result}   Finally, {b**2} - {4 * (a * c)} = {result}. We get our final answer for the discrimnant!')
    print('')
    print(f'For the nature of root. It is \"{get_nature_of_root(result).title()}\", because...')
    print('If the number is 0, it is \"Real And Equal\"')
    print('If the number is above 0, it is \"Real And Unequal\"')
    print('If the number is below 0, it is \"Unreal\"')

if __name__ == '__main__':
    try:
        a = int(input('A: '))
        b = int(input('B: '))
        c = int(input('C: '))
        show_solution = input('Show solution? (y/n): ').lower()

        result = solve_discriminant(a, b, c)
        nature_of_root = get_nature_of_root(result)
        full_discriminant_equation = get_full_discriminant_equation(a, b, c)

        print('\nEquation: b\u00b2 - 4ac\nSolved Equation: {} = {}\nNature of root: {}'.format(full_discriminant_equation, result, nature_of_root.title()))

        if show_solution == 'y' or show_solution == 'yes':
            print('\n-------------------- SOLUTION --------------------')
            print_solution(a, b, c)
    except ValueError:
        print('\nPlease only put numbers for A, B & C!')
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')
