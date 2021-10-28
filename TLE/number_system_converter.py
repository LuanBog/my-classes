#!/usr/bin/env python

import math

LETTERS = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g'}

#  Binary
def group_binary(binary, count):
    result = []
    byte = '' # idk what to name this

    counter = 0

    for index, bit in enumerate(binary[::-1]):
        if counter == count:
            result.append(byte[::-1])

            byte = ''
            counter = 0

        byte += bit
        counter += 1

    result.append(byte[::-1])

    result = list(reversed(result))

    for i, j in enumerate(result):
        if len(j) != count:
            result[i] = '0'*(count - len(j)) + j

    return result


def binary_to_decimal(binary):
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

def binary_to_octal(binary):
    result = []
    grouped = group_binary(binary, 3)

    print('{}\u2082 =\n{} =\n'.format(binary, ' '.join(grouped)))

    byte_result = 0
    first_equation = []
    second_equation = []

    for byte in grouped:
        print('{}\u2082 ='.format(byte))

        for index, bit in enumerate(byte[::-1]):
            first_equation.append('({} x 2^{})'.format(bit, index))
            second_equation.append(str(int(bit) * (2 ** index)))
            byte_result += int(bit) * (2 ** index)

        result.append(str(byte_result))

        first_equation = ' + '.join(reversed(first_equation))
        second_equation = ' + '.join(reversed(second_equation))

        print('{}\u2082 =\n{} = \n{} = \n{}\u2081\u2080\n'.format(binary, first_equation, second_equation, byte_result))

        first_equation = []
        second_equation = []
        byte_result = 0

    print('{} =\n{}\u2088'.format(' '.join(result), ''.join(result)))

    print('\n{}\u2082 = {}\u2088'.format(binary, ''.join(result)))

def binary_to_hexadecimal(binary):
    result = []
    grouped = group_binary(binary, 4)

    print('{}\u2082 =\n{} =\n'.format(binary, ' '.join(grouped)))

    byte_result = 0
    first_equation = []
    second_equation = []

    for byte in grouped:
        print('{}\u2082 ='.format(byte))

        for index, bit in enumerate(byte[::-1]):
            first_equation.append('({} x 2^{})'.format(bit, index))
            second_equation.append(str(int(bit) * (2 ** index)))
            byte_result += int(bit) * (2 ** index)

        result.append(str(byte_result))

        first_equation = ' + '.join(reversed(first_equation))
        second_equation = ' + '.join(reversed(second_equation))

        print('{}\u2082 =\n{} = \n{} = \n{}\u2081\u2080\n'.format(binary, first_equation, second_equation, byte_result))

        first_equation = []
        second_equation = []
        byte_result = 0

    print('{} =\n'.format(' '.join(result), ''.join(result)))

    for index, bit in enumerate(result):
        if bit in LETTERS.keys():
            letter = LETTERS[bit]

            print('{} -> {}'.format(bit, letter))
            result[index] = letter
    
    print('\n{} =\n{}\u2081\u2086'.format(' '.join(result), ''.join(result)))

    print('\n{}\u2082 = {}\u2081\u2086'.format(binary, ''.join(result)))
 
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

    while target > 0:
        result_ = target / 16
        reminder = float('0.' + str(result_).split('.')[1]) * 16

        print('{}\u2081\u2080 / 16 = {} reminder. {}'.format(target, math.trunc(result_) if float(result_).is_integer() else result_, math.trunc(reminder)))
        
        result.append(str(math.trunc(reminder)))

        target = math.trunc(result_) 

    for index, bit in enumerate(result):
        if bit in LETTERS.keys():
            letter = LETTERS[bit]

            print('{} -> {}'.format(bit, letter))
            result[index] = letter

    print('\n{}\u2081\u2080 = {}\u2081\u2086'.format(decimal, ''.join(result)[::-1]))

def main():
    try:
        value = input('\nValue: ')        
        value_type = input('\n[A] Binary (Base 2) \n[B] Octal (Base 8) \n[C] Decimal (Base 10) \n[D] Hexadecimal (Base 16)\n\nWhat is ({}): '.format(value)).lower()

        if value_type == 'a':
            print('\n-------------------- TO DECIMAL --------------------\n')
            binary_to_decimal(value)
            print('\n-------------------- TO OCTAL --------------------\n')
            binary_to_octal(value)
            print('\n-------------------- TO HEXADECIMAL --------------------\n')
            binary_to_hexadecimal(value)
        elif value_type == 'c':
            print('\n-------------------- TO BINARY --------------------\n')
            decimal_to_binary(int(value))
            print('\n-------------------- TO OCTAL --------------------\n')
            decimal_to_octal(int(value))
            print('\n-------------------- TO HEXADECIMAL --------------------\n')
            decimal_to_hexadecimal(int(value))
        else:
            print('\nInvalid choice!')

    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()