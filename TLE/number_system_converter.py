#!/usr/bin/env python

import math

#  Binary
def binary_to_decimal(binary, return_val=False):
    first_equation = []
    second_equation = []
    result = 0

    for index, bit in enumerate(binary[::-1]):
        first_equation.append('({} x 2^{})'.format(bit, index))
        second_equation.append(str(int(bit) * (2 ** index)))
        result += int(bit) * (2 ** index)

    first_equation = ' + '.join(reversed(first_equation))
    second_equation = ' + '.join(reversed(second_equation))

    # Checking
    print('{}\u2082 =\n{} = \n{} = \n{}\u2081\u2080'.format(binary, first_equation, second_equation, result))

    print('\n{}\u2082 = {}\u2081\u2080'.format(binary, result))

    if return_val:
        return result

# Decimal
def decimal_to_binary(decimal):
    result = ''
    target = decimal

    while target > 0:
        result_ = target / 2
        reminder = '0' if float(result_).is_integer() else '1'

        print('{}\u2081\u2080 / 2 = {} reminder. {}'.format(target, math.trunc(result_) if float(result_).is_integer() else result_, reminder))
        
        result += reminder

        target = math.trunc(result_)

    print('\n{}\u2081\u2080 = {}\u2082'.format(decimal, result[::-1]))

def decimal_to_octal(decimal):
    result = ''
    target = decimal

    while target > 0:
        result_ = target / 8
        reminder = float('0.' + str(result_).split('.')[1]) * 8

        print('{}\u2081\u2080 / 8 = {} reminder. {}'.format(target, math.trunc(result_) if float(result_).is_integer() else result_, math.trunc(reminder)))
        
        result += str(math.trunc(reminder))

        target = math.trunc(result_)

    print('\n{}\u2081\u2080 = {}\u2088'.format(decimal, result[::-1]))

def decimal_to_hexadecimal(decimal):
    result = []
    target = decimal

    letters = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g'}

    while target > 0:
        result_ = target / 16
        reminder = float('0.' + str(result_).split('.')[1]) * 16

        print('{}\u2081\u2080 / 16 = {} reminder. {}'.format(target, math.trunc(result_) if float(result_).is_integer() else result_, math.trunc(reminder)))
        
        result.append(str(math.trunc(reminder)))

        target = math.trunc(result_) 

    for index, byte in enumerate(result):
        if byte in letters.keys():
            letter = letters[byte]

            print('{} -> {}'.format(byte, letter))
            result[index] = letter

    print('\n{}\u2081\u2080 = {}\u2081\u2086'.format(decimal, ''.join(result)[::-1]))

def main():
    try:
        from_ = input('\n[A] Binary (Base 2) \n[B] Decimal (Base 10)\n\nConvert from: ').lower()

        if not from_ in ['a', 'b']:
            print('\nThat is not a valid choice!')
            return

        to = input('\n[A] Binary (Base 2) \n[B] Octal (Base 8) \n[C] Decimal (Base 10) \n[D] Hexadecimal (Base 16)\n\nConvert to: ').lower()

        if not to in ['a', 'b', 'c', 'd']:
            print('\nThat is not a valid choice!')
            return
        
        try:
            value = input('\nValue: ')
        except ValueError:
            print('\nYou can only put numbers!')
            return
        
        print('\n---------------------------------------- RESULT ----------------------------------------\n')

        # Binary to...
        if from_ == 'a':
            if to == 'c':
                if len(value.split(' ')) == 1:
                    print('Binary (Base 2) -> Decimal (Base 10)\n')
                    binary_to_decimal(value)
                else:
                    result = ''

                    print('Binaries (Base 2) -> Decimal (Base 10)\n')
                    for binary in value.split(' '):
                        print('---------- {} ----------\n'.format(binary))
                        result += str(binary_to_decimal(binary, return_val=True))
                        print('')

                    print('{}\u2082 = {}\u2081\u2080'.format(value, result))

        # Decimal to...
        elif from_ == 'b':
            if to == 'a':
                print('Decimal (Base 10) -> Binary (Base 2)\n')
                decimal_to_binary(int(value))
            elif to == 'b':
                print('Decimal (Base 10) -> Octal (Base 8)\n')
                decimal_to_octal(int(value))
            elif to == 'd':
                print('Decimal (Base 10) -> Hexadecimal (Base 16)\n')
                decimal_to_hexadecimal(int(value))
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()
