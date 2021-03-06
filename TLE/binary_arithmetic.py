#!/usr/bin/env python

import math

def is_binary(binary):
    for bit in binary:
        if not bit in ['0', '1']:
            return False

    return True

# If a's length is longer than b
def adjust(compare_towards, target):
    if len(compare_towards) == len(target):
        return target
    else:
        amount_to_add = len(compare_towards) - len(target)
        target = ' ' * amount_to_add + target

        return target

def binary_zip(a, b):
    b = adjust(a, b)

    return [list(x) for x in zip(a, b)]

def seperate(text, amount=1):
    space = ' ' * amount
    return space.join(list(str(text))) 

def check(binary):
    first_equation = []
    second_equation = []

    result = {
        'equations': {
            'first': '',
            'second': ''
        },
        'result': 0,
    }

    for index, bit in enumerate(binary[::-1]):
        first_equation.append('({}x2^{})'.format(bit, index))
        second_equation.append(str(int(bit) * (2 ** index)))
        result['result'] += int(bit) * (2 ** index)

    first_equation = ' + '.join(reversed(first_equation))
    second_equation = '({})'.format(' + '.join(reversed(second_equation)))

    result['equations']['first'] = first_equation
    result['equations']['second'] = second_equation

    return result

def addition(a, b):
    result = bin(int(a, 2) + int(b, 2))[2:]
    adjust_count = len(seperate(result)) - len(seperate(a))
    adjust_string =  ' ' * adjust_count if adjust_count > 0 else ''

    # Handles carries
    carries = ''
    zipped = list(reversed(binary_zip(a, b)))

    for index, bit in enumerate(zipped):
        # This bit has a carry
        if len(bit) == 3:
            carries += '1'

            if bit[0] == '1' or bit[1] == '1':
                if index + 1 < len(zipped):
                    zipped[index + 1].append('1')
                else:
                    zipped.insert(index + 1, ['x', 'x', '1'])
        else:
            carries += ' '

            if bit[0] == '1' and bit[1] == '1':
                if index + 1 < len(zipped):
                    zipped[index + 1].append('1')
                else:
                    zipped.insert(index + 1, ['x', 'x', '1'])

    carries = carries[::-1]

    print('\nAddition:\n')
    print(seperate(carries))
    print(adjust_string + seperate(a))
    print(adjust_string + seperate(adjust(a, b)))
    print('-' * len(seperate(result)))
    print(seperate(result))

    print('\nChecking:\n')

    a_checking = check(a)
    b_checking = check(b)
    result_checking = check(result)

    print('{} = {} = {}'.format(a_checking['equations']['first'], a_checking['equations']['second'], a_checking['result']))
    print('{} = {} = {}'.format(b_checking['equations']['first'], b_checking['equations']['second'], b_checking['result']))
    print('{} = {} = {}'.format(result_checking['equations']['first'], result_checking['equations']['second'], result_checking['result']))

    print('\n{} + {} = {}'.format(a_checking['result'], b_checking['result'], result_checking['result']))
    print('{} + {} = {}'.format(a, b, result))

def subtraction(a, b):
    result = bin(int(a, 2) - int(b, 2))[2:]
    adjust_count = len(seperate(result)) - len(seperate(a))
    adjust_string =  ' ' * adjust_count if adjust_count > 0 else ''

    if len(result) != len(a):
        result = ' ' * (len(a) - len(result)) + result 

    zipped = list(reversed(binary_zip(a, b)))
    carries_first = ''
    carries_second = ''

    for index, bit in enumerate(zipped):
        if bit[0] == '0' and bit[1] == '1':

            bit.append('2')

            if zipped[index + 1][0] == '1':
                zipped[index + 1].append('0')
            else:
                iterations = 1

                while zipped[index + iterations][0] != '1':
                    zipped[index + iterations].append('2')
                    zipped[index + iterations].append('1')
                    iterations += 1

                zipped[index + iterations].append('0')
                iterations = 1
    for bit in zipped:
        if len(bit) >= 3:
            carries_first += bit[2]
        else:
            carries_first += ' '

        if len(bit) == 4:
            carries_second += bit[3]
        else:
            carries_second += ' '

    carries_first = carries_first[::-1]
    carries_second = carries_second[::-1]

    print('\nSubtraction:\n')
    print(seperate(carries_second))
    print(seperate(carries_first))
    print(adjust_string + seperate(a))
    print(adjust_string + seperate(adjust(a, b)))
    print('-' * len(seperate(result)))
    print(seperate(result))

    print('\nChecking:\n')

    a_checking = check(a)
    b_checking = check(b)
    result_checking = check(result.strip())

    print('{} = {} = {}'.format(a_checking['equations']['first'], a_checking['equations']['second'], a_checking['result']))
    print('{} = {} = {}'.format(b_checking['equations']['first'], b_checking['equations']['second'], b_checking['result']))
    print('{} = {} = {}'.format(result_checking['equations']['first'], result_checking['equations']['second'], result_checking['result']))

    print('\n{} - {} = {}'.format(a_checking['result'], b_checking['result'], result_checking['result']))
    print('{} - {} = {}'.format(a, b, result.strip()))

def multiplication(a, b):
    result = bin(int(a, 2) * int(b, 2))[2:]
    adjust_count = len(seperate(result)) - len(seperate(a))
    adjust_string =  ' ' * adjust_count if adjust_count > 0 else ''

    additions = []
    addition_count = 0

    for bit_b in reversed(b):
        addition = ''

        for bit_a in reversed(a):

            if bit_b == '0':
                addition += '0'
            else:
                addition += bit_a

        additions.append(addition[::-1] + '0' * addition_count)
        addition_count += 1

    print('\nMultiplication:\n')
    print(adjust_string + seperate(a))
    print(adjust_string + seperate(adjust(a, b)))
    print('-' * len(seperate(result)))

    for binary in additions:
        print(seperate(adjust(result, binary)))

    print('-' * len(seperate(result)))
    print(seperate(result))

    print('\nChecking:\n')

    a_checking = check(a)
    b_checking = check(b)
    result_checking = check(result)

    print('{} = {} = {}'.format(a_checking['equations']['first'], a_checking['equations']['second'], a_checking['result']))
    print('{} = {} = {}'.format(b_checking['equations']['first'], b_checking['equations']['second'], b_checking['result']))
    print('{} = {} = {}'.format(result_checking['equations']['first'], result_checking['equations']['second'], result_checking['result']))

    print('\n{} * {} = {}'.format(a_checking['result'], b_checking['result'], result_checking['result']))
    print('{} * {} = {}'.format(a, b, result))

def divison(a, b):
    result = bin(math.trunc(int(a, 2) / int(b, 2)))[2:]
    divisor_adjust_string = ' ' * (len(seperate(b)) + 1)

    if len(result) != len(a):
        result = ' ' * (len(a) - len(result)) + result 

    print('\nDivision:\n')
    print(divisor_adjust_string + '  ' + seperate(result))
    print(divisor_adjust_string + '-' * (len(seperate(a)) + 3))
    print('{} | {}'.format(seperate(b), seperate(a)))

    print('\nChecking:\n')

    a_checking = check(a)
    b_checking = check(b)
    result_checking = check(result.strip())

    print('{} = {} = {}'.format(a_checking['equations']['first'], a_checking['equations']['second'], a_checking['result']))
    print('{} = {} = {}'.format(b_checking['equations']['first'], b_checking['equations']['second'], b_checking['result']))
    print('{} = {} = {}'.format(result_checking['equations']['first'], result_checking['equations']['second'], result_checking['result']))

    print('\n{} / {} = {}'.format(a_checking['result'], b_checking['result'], result_checking['result']))
    print('{} / {} = {}'.format(a, b, result.strip()))

def main():
    top_binary = input('Top Binary: ')

    if not is_binary(top_binary):
        print('\nPlease only put binary!')
        exit(1)

    bottom_binary = input('Bottom Binary: ')

    if not is_binary(bottom_binary):
        print('\nPlease only put binary!')
        exit(1)
        
    operation = input('[+] Addition, [-] Subtraction, [*] Multiplication, [/] Division: ')

    if operation == '+':
        addition(top_binary, bottom_binary)
    elif operation == '-':
        subtraction(top_binary, bottom_binary)
    elif operation == '*':
        multiplication(top_binary, bottom_binary)
    elif operation == '/':
        divison(top_binary, bottom_binary)
    else:
        print('\nOperation "{}" doesn\'t exist!'.format(operation))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')
