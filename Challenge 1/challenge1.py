import decimal


# Author: Rodrigo Bosarreyes

def calc_tortillas_to_bring(n: int, m: int):
    """Calculate how many tortillas you will bring"""
    if n < 0 or m < 0:
        return 'Can not be calculated'
    elif n == 0 and m == 0:
        return 0
    elif (n >= 0 and n <= 100000) and (m >= 0 and m <= 100000):
        if n > 1:
            # n = round((n / 2)) # In python 3, a decimal 2.5 is like 2.4999999, so round down to 2
            n = decimal.Decimal(n / 2).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)
            
        if m > 1:
            m = decimal.Decimal(m / 2).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)
        
        return n + m
    
def calc_tortillas_from_file(file_input: str, file_output: str):
    with open(file_output, 'w') as fo: # to save results
        with open(file_input, 'r') as f: # to read results
            for i, line in enumerate(f):
                if i == 0:
                    continue
                n, m = line.split(' ')
                result = calc_tortillas_to_bring(int(n), int(m))
                result = f'Case #{i}: {result}'
                print(result)
                fo.write(result + '\n')
                
            
if __name__ == "__main__":
    # If we want test from console input
    # c = int(input('Write the number of cases: '))
    # for i in range(c):
    #     if c >= 1 or c <= 100:
    #         n = int(input('N: '))
    #         m = int(input('M: '))
    
    #         result = calc_tortillas_to_bring(n, m)
    #         print(f'Case #{i+1}: {result}')
    
    calc_tortillas_from_file('submitInput', 'submit_output.txt')