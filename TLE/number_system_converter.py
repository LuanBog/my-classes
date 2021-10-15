#!/usr/bin/env python

import math

#  Binary

def binary_to_decimal(binary):
    first_equation = []
    second_equation = []
    result = 0

    for index, octet in enumerate(binary[::-1]):
        first_equation.append('({} x 2^{})'.format(octet, index))
        second_equation.append(str(int(octet) * (2 ** index)))
        result += int(octet) * (2 ** index)

    first_equation = ' + '.join(reversed(first_equation))
    second_equation = ' + '.join(reversed(second_equation))

    print('{}\u2082 =\n{} = \n{} = \n{}\u2081\u2080'.format(binary, first_equation, second_equation, result))

    print('\n{}\u2082 = {}\u2081\u2080'.format(binary, result))


# Decimal
def decimal_to_binary(decimal):
    binary = ''
    target = decimal

    while target > 0:
        result = target / 2
        reminder = '0' if float(result).is_integer() else '1'

        print('{}\u2081\u2080 / 2 = {} reminder. {}'.format(target, math.trunc(result) if float(result).is_integer() else result, reminder))
        
        binary += reminder

        target = math.trunc(result)

    return binary[::-1]

def decimal_to_octal(decimal):
    octal = ''
    target = decimal

    while target > 0:
        result = target / 8
        reminder = float('0.' + str(result).split('.')[1]) * 8

        print('{}\u2081\u2080 / 8 = {} reminder. {}'.format(target, math.trunc(result) if float(result).is_integer() else result, math.trunc(reminder)))
        
        octal += str(math.trunc(reminder))

        target = math.trunc(result)

    return octal[::-1]

def decimal_to_hexadecimal(decimal):
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
        from_ = input('[A] Binary (Base 2), [B] Decimal (Base 10): ').lower()

        if not from_ in ['a', 'b']:
            print('\nThat is not a valid choice!')
            return

        print('\nConvert to:')
        to = input('[A] Binary (Base 2), [B] Octal (Base 8), [C] Decimal (Base 10), [D] Hexadecimal (Base 16): ').lower()

        if not to in ['a', 'b', 'c', 'd']:
            print('\nThat is not a valid choice!')
            return
        
        try:
            value = input('\nValue: ')
        except ValueError:
            print('\nYou can only put numbers!')
            return
        
        result = ''
        sub_number = get_sub_number(to)
        
        print('\n---------------------------------------- RESULT ----------------------------------------\n')

        # Binary to...
        if from_ == 'a':
            if to == 'c':
                print('Binary (Base 2) -> Decimal (Base 10)\n')
                result = binary_to_decimal(value)
        # Decimal to...
        elif from_ == 'b':
            if to == 'a':
                print('Decimal (Base 10) -> Binary (Base 2)\n')
                result = decimal_to_binary(int(value))
            elif to == 'b':
                print('Decimal (Base 10) -> Octal (Base 8)\n')
                result = decimal_to_octal(int(value))
            elif to == 'd':
                print('Decimal (Base 10) -> Hexadecimal (Base 16)\n')
                result = decimal_to_hexadecimal(int(value))

            print('\n{}\u2081\u2080 = {}{}'.format(value, result, sub_number))
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()
