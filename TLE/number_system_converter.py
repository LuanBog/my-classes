#!/usr/bin/env python

import math


def to_binary(decimal):
    binary = ''
    target = decimal

    while target > 0:
        result = target / 2
        reminder = '0' if float(result).is_integer() else '1'

        print('{}\u2081\u2080 / 2 = {} reminder. {}'.format(target, math.trunc(result) if float(result).is_integer() else result, reminder))
        
        binary += reminder

        target = math.trunc(result)

    return binary[::-1]

def to_octal(decimal):
    octal = ''
    target = decimal

    while target > 0:
        result = target / 8
        reminder = float('0.' + str(result).split('.')[1]) * 8

        print('{}\u2081\u2080 / 8 = {} reminder. {}'.format(target, math.trunc(result) if float(result).is_integer() else result, math.trunc(reminder)))
        
        octal += str(math.trunc(reminder))

        target = math.trunc(result)

    return octal[::-1]

def to_hexadecimal(decimal):
    hexadecimal = []
    target = decimal

    letters = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g'}

    while target > 0:
        result = target / 16
        reminder = float('0.' + str(result).split('.')[1]) * 16

        print('{}\u2081\u2080 / 16 = {} reminder. {}'.format(target, math.trunc(result) if float(result).is_integer() else result, math.trunc(reminder)))
        
        hexadecimal.append(str(math.trunc(reminder)))

        target = math.trunc(result) 

    for index, byte in enumerate(hexadecimal):
        if byte in letters.keys():
            letter = letters[byte]

            print('{} -> {}'.format(byte, letter))
            hexadecimal[index] = letter

    return ''.join(hexadecimal)[::-1]

def get_sub_number(to):
    if to == 'a':
        return '\u2082'
    elif to == 'b':
        return '\u2088'
    elif to == 'c':
        return '\u2081\u2086'

def main():
    try:
        print('\nConvert from:')
        from_ = input('[A] Decimal (Base 10) [More coming soon]: ').lower()

        if from_ != 'a':
            print('\nThat is not a valid choice!')
            return

        print('\nConvert to:')
        to = input('[A] Binary (Base 2), [B] Octal (Base 8), [C] Hexadecimal (Base 16): ').lower()

        if not to in ['a', 'b', 'c']:
            print('\nThat is not a valid choice!')
            return
        
        try:
            decimal = int(input('\nValue: '))
        except ValueError:
            print('\nYou can only put numbers!')
            return
        
        result = ''
        sub_number = get_sub_number(to)
        
        print('\n---------------------------------------- RESULT ----------------------------------------\n')

        if to == 'a':
            print('Decimal (Base 10) -> Binary (Base 2)\n')
            result = to_binary(decimal)
        elif to == 'b':
            print('Decimal (Base 10) -> Octal (Base 8)\n')
            result = to_octal(decimal)
        elif to == 'c':
            print('Decimal (Base 10) -> Hexadecimal (Base 16)\n')
            result = to_hexadecimal(decimal)

        print('\n{}\u2081\u2080 = {}{}'.format(decimal, result, sub_number))
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()
