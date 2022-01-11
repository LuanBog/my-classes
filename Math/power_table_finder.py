#!/usr/bin/env python

def find(x):
    for number in range(1, 11):
        for pow in range(1, 11):
            if number ** pow == x:
                return (number, pow)

    return None

def main():
    x = int(input('Number: '))
    result = find(x)

    if result != None:
        print('\n{}^{} = {}'.format(result[0], result[1], x))    
    else:
        print('\nNot found!')

if __name__ == '__main__':
    main()
