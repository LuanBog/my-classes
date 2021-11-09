#!/usr/bin/env python

import math

def hex_number_to_letter(value, reverse=False):
    LETTERS = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g'}

    if not reverse:
        for index, bit in enumerate(value):
            if bit in LETTERS.keys():
                letter = LETTERS[bit]

                print('{} -> {}'.format(bit, letter))
                value[index] = letter
    else:
        for index, bit in enumerate(value):
            for number, letter in LETTERS.items():
                if bit.lower() == letter:
                    value[index] = number
                    print('{} -> {}'.format(bit, number))

    return value

def seperate(text, amount=1):
    space = ' ' * amount
    return space.join(list(str(text))) 

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

    return result

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

    return ''.join(result)

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

    print('')
    result = hex_number_to_letter(result)

    print('\n{} =\n{}\u2081\u2086'.format(' '.join(result), ''.join(result)))

    print('\n{}\u2082 = {}\u2081\u2086'.format(binary, ''.join(result)))
 
    return ''.join(result)

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

    return result[::-1]

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

    return result[::-1]

def decimal_to_hexadecimal(decimal):
    result = []
    target = decimal

    while target > 0:
        result_ = target / 16
        reminder = float('0.' + str(result_).split('.')[1]) * 16

        print('{}\u2081\u2080 / 16 = {} reminder. {}'.format(target, math.trunc(result_) if float(result_).is_integer() else result_, math.trunc(reminder)))
        
        result.append(str(math.trunc(reminder)))

        target = math.trunc(result_) 

    print('')
    result = hex_number_to_letter(result)

    print('\n{}\u2081\u2080 = {}\u2081\u2086'.format(decimal, ''.join(result)[::-1]))

    return ''.join(result[::-1])

# Octal
def get_factors(number, factors):
    # Example:
    # number = 5
    # components = [4, 2, 1]
    # 4 + 1 is 5, so return [4, 1], else return []

    number = int(number)

    # Checks if number is in one of the components
    for factor in factors:
        if number == factor:
            return [factor]    

    # Sums up everything
    if sum(factors) == number:
        return factors

    # Bruteforce
    a = 0
    b = 1
    c = 2

    while a != len(factors) - 1:
        if b == len(factors):
            a += 1
            b = 0

        if factors[a] + factors[b] == number:
            return [factors[a], factors[b]]

        b += 1


    # Does bruteforce again but with an extra number (I know this can never exeed 4)
    if len(factors) == 4:
        a = 0
        b = 1
        c = 2

        # while a != len(factors):
        while True:
            if factors[a] + factors[b] + factors[c] == number:
                return [factors[a], factors[b], factors[c]]

            if a == len(factors) - 2:
                break

            # if b == len(factors):
            #     a += 1
            # elif c == len(factors):
            #     b += 1
            # else:
            #     c += 1
            
            if c == 2:
                c += 1
            elif b == 1:
                b += 1
            else:
                a += 1

    return []

def octal_to_binary(octal):
    result = []
    factorables = [4, 2, 1]

    print('{}\u2088 =\n{} =\n'.format(octal, ' '.join(octal)))

    byte = ''

    for bit in octal:
        factors = get_factors(bit, factorables)

        for factor in factorables:
            if factor in factors:
                byte += '1'
            else:
                byte +=  '0'

        print('{} ='.format(bit))
        print('4 2 1')
        print(seperate(byte))

        print('')

        result.append(byte)
        byte = ''

    print(' '.join(result))

    if result[0][0] == '0':
        while result[0][0] == '0':
            result[0] = result[0][1:]

    print('{}\u2082'.format(''.join(result)))

    print('\n{}\u2088 = {}\u2082'.format(octal, ''.join(result)))

    return ''.join(result)

def octal_to_decimal(octal):
    first_equation = []
    second_equation = []
    result = 0

    for index, bit in enumerate(octal[::-1]):
        first_equation.append('({} x 8^{})'.format(bit, index))
        second_equation.append(str(int(bit) * (8 ** index)))
        result += int(bit) * (8 ** index)

    first_equation = ' + '.join(reversed(first_equation))
    second_equation = ' + '.join(reversed(second_equation))

    # Checking
    print('{}\u2088 =\n{} = \n{} = \n{}\u2081\u2080'.format(octal, first_equation, second_equation, result))

    print('\n{}\u2088 = {}\u2081\u2080'.format(octal, result))

    return result

def octal_to_hexadecimal(octal):
    # Convert to binary
    print('Convert to binary\n')
    binary = octal_to_binary(octal)    
    print('\nConvert binary to hexadecimal\n')
    result = binary_to_hexadecimal(binary)

    print('\n{}\u2088 = {}\u2081\u2086'.format(octal, result))

    return result

# Hexadecimal
def hexadecimal_to_binary(hexadecimal):
    result = []
    factorables = [8, 4, 2, 1]

    hexadecimal_copy = hexadecimal
    hexadecimal = list(hexadecimal)

    print('{}\u2081\u2086 =\n'.format(''.join(hexadecimal)))

    hexadecimal = hex_number_to_letter(hexadecimal, reverse=True)

    print('\n{} =\n'.format(' '.join(hexadecimal)))

    byte = ''

    for bit in hexadecimal:
        factors = get_factors(bit, factorables)

        for factor in factorables:
            if factor in factors:
                byte += '1'
            else:
                byte += '0'

        print('{} ='.format(bit))
        print('8 4 2 1')
        print(seperate(byte))

        print('')

        result.append(byte)
        byte = ''

    print(' '.join(result))

    if result[0][0] == '0':
        while result[0][0] == '0':
            result[0] = result[0][1:]

        print(' '.join(result))

    print('{}\u2082'.format(''.join(result)))

    print('\n{}\u2081\u2086 = {}\u2082'.format(''.join(hexadecimal_copy), ''.join(result)))

    return ''.join(result)

def hexadecimal_to_decimal(hexadecimal):
    first_equation = []
    second_equation = []
    result = 0

    hexadecimal_copy = hexadecimal
    hexadecimal = list(hexadecimal)

    print('{}\u2081\u2086 =\n'.format(''.join(hexadecimal)))
    hexadecimal = hex_number_to_letter(hexadecimal, reverse=True)

    for index, bit in enumerate(hexadecimal[::-1]):
        first_equation.append('({} x 16^{})'.format(bit, index))
        second_equation.append(str(int(bit) * (16 ** index)))
        result += int(bit) * (16 ** index)

    first_equation = ' + '.join(reversed(first_equation))
    second_equation = ' + '.join(reversed(second_equation))

    # Checking
    print('\n{} =\n{} = \n{} = \n{}\u2081\u2080'.format(' '.join(hexadecimal), first_equation, second_equation, result))

    print('\n{}\u2081\u2086 = {}\u2081\u2080'.format(''.join(hexadecimal_copy), result))

    return result

def hexadecimal_to_octal(hexadecimal):
    print('Convert to binary\n')
    binary = hexadecimal_to_binary(hexadecimal)
    print('\nConvert binary to hexadecimal\n')
    octal = binary_to_octal(binary)

    print('\n{}\u2081\u2086 = {}\u2088'.format(hexadecimal, octal))

    return octal

def main():
    value = input('\nValue: ')        
    value_type = input('\n[A] Binary (Base 2) \n[B] Octal (Base 8) \n[C] Decimal (Base 10) \n[D] Hexadecimal (Base 16)\n\nWhat is ({}): '.format(value)).lower()

    if value_type == 'a':
        print('\n-------------------- TO OCTAL --------------------\n')
        octal = binary_to_octal(value)
        print('\n-------------------- TO DECIMAL --------------------\n')
        decimal = binary_to_decimal(value)
        print('\n-------------------- TO HEXADECIMAL --------------------\n')
        hexadecimal = binary_to_hexadecimal(value)

        binary = value
    elif value_type == 'b':
        print('\n-------------------- TO BINARY --------------------\n')
        binary = octal_to_binary(value)
        print('\n-------------------- TO DECIMAL --------------------\n')
        decimal = octal_to_decimal(value)
        print('\n-------------------- TO HEXADECIMAL --------------------\n')
        hexadecimal = octal_to_hexadecimal(value)

        octal = value
    elif value_type == 'c':
        value = int(value)

        print('\n-------------------- TO BINARY --------------------\n')
        binary = decimal_to_binary(value)
        print('\n-------------------- TO OCTAL --------------------\n')
        octal = decimal_to_octal(value)
        print('\n-------------------- TO HEXADECIMAL --------------------\n')
        hexadecimal = decimal_to_hexadecimal(value)

        decimal = value
    elif value_type == 'd':
        value = value.lower()

        print('\n-------------------- TO BINARY --------------------\n')
        binary = hexadecimal_to_binary(value)
        print('\n-------------------- TO OCTAL --------------------\n')
        octal = hexadecimal_to_octal(value)
        print('\n-------------------- TO DECIMAL --------------------\n')
        decimal = hexadecimal_to_decimal(value)

        hexadecimal = value
    else:
        print('\nInvalid choice!')
        exit(1)

    print('\n-------------------- RESULT --------------------\n')
    print('Binary / Base 2: {}\u2082'.format(binary))
    print('Octal / Base 8: {}\u2088'.format(octal))
    print('Decimal / Base 10: {}\u2081\u2080'.format(decimal))
    print('Hexadecimal / Base 16: {}\u2081\u2086'.format(hexadecimal))

    print('\nNote: Check if you\'re actually using the right value type!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')