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
        return values[int(middle - .5)]
    else:
        two_median_terms = [values[int(middle)], values[int(middle-1)]]
        return sum(two_median_terms) / 2

def calculate_range(values):
    return max(values) - min(values)

def calculate_varience(values):
    values = sorted(values)
    sample_mean = round(calculate_mean(values))

    subtracted = map(lambda x: (x - sample_mean), values)
    squared = map(lambda x: x ** 2, subtracted)

    return sum(squared) / (len(values) - 1)

def calculate_standard_deviation(values):
    varience = calculate_varience(values)
    return math.sqrt(varience)

values = [9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]

mean = calculate_mean(values)
mode = calculate_mode(values)
median = calculate_median(values)
range_ = calculate_range(values)
variance = calculate_varience(values)
standard_deviation = calculate_standard_deviation(values)

print('Mean: {}\nMode: {}\nMedian: {}\nRange: {}\nVariance: {}\nStandard Deviation: {}'.format(mean, ', '.join(map(lambda x: str(x), mode)), median, range_, variance, standard_deviation))
