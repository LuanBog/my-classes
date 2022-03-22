#!/usr/bin/env python

def calculate(total_weighted_price_last_year, total_weighted_price_this_year):
    cpi = round((total_weighted_price_this_year / total_weighted_price_last_year) * 100, 2)
    inflation_rate = round(((cpi - 100) / 100) * 100, 2)
    purchasing_power = round(100 / cpi, 2)

    print('\n-------------------- RESULT --------------------')
    print('\nCPI: {} \nInflation Rate: {}%\nPurchasing Power: {}'.format(cpi, inflation_rate, purchasing_power))

    print('\n-------------------- SOLUTION --------------------')
    
    print('\nCPI = (Total weight price this year / Total weight price last year) * 100')
    print(f'    = ({total_weighted_price_this_year} / {total_weighted_price_last_year}) * 100')
    print(f'    = ({total_weighted_price_this_year / total_weighted_price_last_year}) * 100')
    print(f'    = {(total_weighted_price_this_year / total_weighted_price_last_year) * 100}')
    print(f'CPI = {cpi} (rounded to 2)')

    print('\nInflation rate = ((CPI - 100) / 100) * 100')
    print(f'               = (({cpi} - 100) / 100) * 100')
    print(f'               = ({cpi - 100} / 100) * 100')
    print(f'               = {cpi - 100 / 100} * 100')
    print(f'               = {cpi - 100 / 100 * 100}')
    print(f'Inflation rate = {inflation_rate}% (rounded to 2)')

    print('\nPurchasing power = 100 / CPI')
    print(f'                 = 100 / {cpi}')
    print(f'                 = {100 / cpi}')
    print(f'Purchasing power = {purchasing_power} (rounded to 2)')

def main():
    try:
        total_weighted_price_last_year = int(input('Total Weighted Price Last Year: '))
        total_weighted_price_this_year = int(input('Total Weighted Price This Year: '))

        calculate(total_weighted_price_last_year, total_weighted_price_this_year)
    except ValueError:
        print('\nPlease only put numbers!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')
