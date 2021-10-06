#!/usr/bin/env python

import math

def to_binary(decimal, show_solution_only=False):
    binary = ''
    target = decimal

    while target > 0:
        result = target / 2
        reminder = '0' if float(result).is_integer() else '1'

        if show_solution_only:
            print('{}\u2081\u2080 / 2 = {} reminder. {}'.format(target, math.trunc(result) if float(result).is_integer() else result, reminder))
        
        binary += reminder

        target = math.trunc(result)

    if not show_solution_only:
        return binary[::-1]
    else:
        return None

def main():
    # print('Convert from:')
    # from_ = input('[A] Decimal (Base 10) [More coming soon]: ')
    # print('Convert to:')
    # to = input('[A] Binary (Base 2): ')
    decimal = int(input('Decimal value: '))

    print('\n---------------------------------------- RESULT ----------------------------------------\n')
    to_binary(decimal, show_solution_only=True)
    result = to_binary(decimal)
    print('{}\u2081\u2080 = {}\u2082'.format(decimal, result))

if __name__ == '__main__':
    main()