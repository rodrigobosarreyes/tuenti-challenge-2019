from fractions import Fraction
import numpy as np

#Author: Rodrigo Bosarreyes
def calc_candies_attenders(m):
    original = list(m) # Original list
    m = list(set(m))

    X = np.lcm.reduce(m)
        
    P = m # Parameters (Numbers of the list sin repetirse xd)
    T = [original.count(n) for n in P] # Count in original list for each item
    C = [] # candies
    A = [] # attendees
    for i, v in enumerate(P):
        C.append((X * T[i]))
        A.append(int((X * T[i]) / v))
        
    C = sum(C)
    A = sum(A)
    
    return Fraction(C, A)

    

def read_from_file(file_input: str, file_output: str):
    with open(file_output, 'w+') as fo:
        with open(file_input, 'r') as fi:
            total_cases = int(fi.readline().rsplit()[0])
            for case in range(total_cases):
                count_list = int(fi.readline().rsplit()[0])
                m = fi.readline()
                m = m.rstrip("\n")
                m = [int(x) for x in m.split(' ')]
                r = calc_candies_attenders(m)
                
                result = f'Case #{case+1}: {r}'
                print(result)
                fo.write(result+'\n')

if __name__ == "__main__":
    read_from_file('./4/submitInput', './4/submitOutput21.txt')
    # read_from_file('./4/testInput', './4/submitOutput2121.txt')