#!/usr/bin/env python

def perfect_x(x):
    for i in range(2, 11):
        attached = ' x '.join([str(i) for j in range(x)])
        print('{} = {}'.format(attached, i ** x))

def attach_suffix(number):
    last_number = int(str(number)[-1])    
    suffix = ''

    if last_number == 1:
        suffix = 'st'
    elif last_number == 2:
        suffix = 'nd'
    elif last_number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    return str(number) + suffix

def main():
    try:
        x = int(input('Perfect x: '))

        if x == 2:
            print('\nPerfect sqares (2nd):')
        elif x == 3:
            print('\nPerfect cubes (3rd):')
        else:
            print('\nPerfect {} numbers:'.format(attach_suffix(x)))

        perfect_x(x)
    except ValueError:
        print('\nPlease only put numbers!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')
