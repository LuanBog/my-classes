#!/usr/bin/env python

def is_binary(binary):
    for octet in binary:
        if not octet in ['0', '1']:
            return False

    return True

# If a's length is longer than b
def adjust(a, b):
    if len(a) == len(b):
        return b
    else:
        amount_to_add = len(a) - len(b)
        b = ' ' * amount_to_add + b

        return b

def binary_zip(a, b):
    b = adjust(a, b)

    return [list(x) for x in zip(a, b)]

def seperate(text, amount=1):
    text = str(text)

    new_text = ''

    for letter in text:
        new_text += letter + ' ' * amount
    
    return new_text.rstrip() 

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

    for index, octet in enumerate(binary[::-1]):
        first_equation.append('({}x2^{})'.format(octet, index))
        second_equation.append(str(int(octet) * (2 ** index)))
        result['result'] += int(octet) * (2 ** index)

    first_equation = ' + '.join(reversed(first_equation))
    second_equation = '({})'.format(' + '.join(reversed(second_equation)))

    result['equations']['first'] = first_equation
    result['equations']['second'] = second_equation

    return result

def addition(a, b):
    sum = bin(int(a, 2) + int(b, 2))[2:]
    adjust_count = len(seperate(sum)) - len(seperate(a))
    adjust_string =  ' ' * adjust_count if adjust_count > 0 else ''

    # Handles carries
    carries = ''
    zipped = list(reversed(binary_zip(a, b)))

    for index, octet in enumerate(zipped):
        # This octet has a carry
        if len(octet) == 3:
            carries += '1'

            if octet[0] == '1' or octet[1] == '1':
                if index + 1 < len(zipped):
                    zipped[index + 1].append('1')
                else:
                    zipped.insert(index + 1, ['x', 'x', '1'])
        else:
            carries += ' '

            if octet[0] == '1' and octet[1] == '1':
                if index + 1 < len(zipped):
                    zipped[index + 1].append('1')
                else:
                    zipped.insert(index + 1, ['x', 'x', '1'])

    carries = carries[::-1]

    print('Addition:\n')
    print(seperate(carries))
    print(adjust_string + seperate(a))
    print(adjust_string + seperate(adjust(a, b)))
    print('-' * len(seperate(sum)))
    print(seperate(sum))

    print('\nChecking:\n')

    a_checking = check(a)
    b_checking = check(b)
    sum_checking = check(sum)

    print('{} = {} = {}'.format(a_checking['equations']['first'], a_checking['equations']['second'], a_checking['result']))
    print('{} = {} = {}'.format(b_checking['equations']['first'], b_checking['equations']['second'], b_checking['result']))
    print('{} = {} = {}'.format(sum_checking['equations']['first'], sum_checking['equations']['second'], sum_checking['result']))

    print('\n{} + {} = {}'.format(a_checking['result'], b_checking['result'], sum_checking['result']))

    print('')

    if a_checking['result'] + b_checking['result'] == sum_checking['result']:
        print('Since {} + {} = {}. This is correct!'.format(a_checking['result'], b_checking['result'], sum_checking['result']))
    else:
        print('This is wrong, please report to Luan directly on discord or create an issue on the github repository (https://github.com/LuanBog/my-classes/tree/master), so I can fix this. When making an issue, please state the two binaries that you tried to sum') # Just making sure

def main():
    try:
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
        else:
            print('\nOperation "{}" has not been implemented yet!'.format(operation))
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()
