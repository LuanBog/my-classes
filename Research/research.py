#!/usr/bin/env python

import math

def calculate_mean(values, show_solution=False):
    sum_ = 0

    for value in values:
        if show_solution:
            print('{} + {} = {}'.format(sum_, value, sum_ + value))
        sum_ += value

    if show_solution:
        print('{} / {} = {}'.format(sum_, len(values), sum_ / len(values)))

    return sum_ / len(values)

def calculate_mode(values):
    reoccuring_values = {}
    result = []

    for value in values:
        if not value in reoccuring_values:
            reoccuring_values[value] = 1 
        else:
            reoccuring_values[value] += 1

    reoccuring_values = dict(sorted(reoccuring_values.items(), key=lambda item: item[1], reverse=True))

    # This handles if there's multiple data with the same number of occurance
    max_value = list(reoccuring_values.values())[0]

    for key, value in reoccuring_values.items():
        if value == max_value:
            result.append(key)
    
    if len(result) == len(values):
        return []

    return result

def calculate_median(values):
    values = sorted(values)
    middle = float(len(values)) / 2

    if middle % 2 != 0:
        print('n or the number of values is {}, it\'s an even number,'.format(len(values)))
        print('we just take the middle term {}'.format(values[int(middle - .5)]))

        return values[int(middle - .5)]
    else:
        two_median_terms = [values[int(middle)], values[int(middle-1)]]

        print('n or the number of values is {}, it\'s an odd number,'.format(len(values)))
        print('so we add the two middle numbers. {} + {} = {},'.format(two_median_terms[0], two_median_terms[1], sum(two_median_terms)))
        print('then we divide it by 2. {} / 2 = {}'.format(sum(two_median_terms), sum(two_median_terms) / 2))

        return sum(two_median_terms) / 2

def calculate_range(values):
    return max(values) - min(values)

def calculate_varience(values):
    values = sorted(values)
    sample_mean = round(calculate_mean(values))

    subtracted = list(map(lambda x: (x - sample_mean), values))
    squared = list(map(lambda x: x ** 2, subtracted))
    variance = sum(squared) / (len(values) - 1)

    # Solution
    print('Mean (rounded): {}\n'.format(sample_mean))
    print('x: ' + ', '.join(map(lambda x: str(x), values)))
    print('xi - mean: ' + ', '.join(map(lambda x: str(x), subtracted)))
    print('xi - mean\u00B2: ' + ', '.join(map(lambda x: str(x), squared)))

    print('\nSum up xi - mean\u00B2: {}'.format(sum(squared)))
    print('Divide by n-1 ({}): {} / {} = {}'.format(len(values) - 1, sum(squared), len(values) - 1, variance))

    return variance

def calculate_standard_deviation(values):
    varience = calculate_varience(values)

    print('The square root of the variance ({}): {}'.format(varience, math.sqrt(varience)))

    return math.sqrt(varience)

def main():
    values = []

    print('\nType "go" to calculate.')
    while True:
        print('\nValues: ' + ', '.join(map(lambda x: str(x), values)))
        value_input = input('Value: ')

        if value_input.lower() != 'go':
            values.append(float(value_input))
        else:
            break

    print('\n-------------------- MEAN --------------------\n')

    print('Solution:\n')
    mean = calculate_mean(values, show_solution=True)

    print('\nMean: ' + str(mean))
    
    print('\n-------------------- MEDIAN --------------------\n')

    print('Solution:\n')
    median = calculate_median(values)

    print('\nMedian: ' + str(median))

    print('\n-------------------- MODE --------------------\n')
    
    mode = calculate_mode(values)

    print('Solution:\n')
    if len(mode) == 1:
        print('Took the value that appeared frequently in the set\n')
    else:
        print('Took the values that appeared frequently in the set\n')

    print('Mode: ' + ', '.join(map(lambda x: str(x), mode)))

    print('\n-------------------- RANGE --------------------\n')

    print('Solution:\n')
    print('The difference of the maximum value and minimum value. {} - {} = {}'.format(max(values), min(values), max(values) - min(values)))

    range_ = calculate_range(values)
    print('\nRange: ' + str(range_))    

    print('\n-------------------- VARIANCE --------------------\n')

    print('Solution:\n')
    variance = calculate_varience(values)
    print('\nVariance: ' + str(variance))    

    print('\n-------------------- STANDARD DEVIATION --------------------\n')

    print('Solution:\n')
    standard_deviation = calculate_standard_deviation(values)
    print('\nStandard Deviation: ' + str(standard_deviation))

    print('\n-------------------- RESULT --------------------\n')

    print('Values given: ' + ', '.join(map(lambda x: str(x), values)))
    print('Values sorted: ' + ', '.join(map(lambda x: str(x), sorted(values))))
    print('')
    print('Mean: ' + str(mean))
    print('Median: ' + str(median))
    print('Mode: ' + ', '.join(map(lambda x: str(x), mode)))
    print('Range: ' + str(range_))   
    print('Variance: ' + str(variance))    
    print('Standard Deviation: ' + str(standard_deviation))

if __name__ == '__main__':
    main()
