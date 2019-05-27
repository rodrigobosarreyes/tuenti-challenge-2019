import numpy as np

# Author: Rodrigo Bosarreyes
typewriter = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-']
]

def find_index_of(v: str):
    for i, value in enumerate(typewriter):
        if v in value:
            return np.array([i, value.index(v)])
        
def decrypt(transmitter: str, msg: str):  
    # First of all we need to how much need sumar 
    letter = find_index_of(transmitter)
    letter_encripted = find_index_of(msg[-1])
    R = letter - letter_encripted

    result = ""
    for le in msg:
        if le is not ' ':
            letter_encrypted = find_index_of(le)
            D = letter_encrypted + R
            if D[0] >= 4:
                D[0] = D[0] - 4
            if D[1] >= 10:
                D[1] = D[1] - 10
            result += typewriter[D[0]][D[1]]
        else:
            result += le

    return result

def read_from_file(file_in: str, file_out: str):
    with open(file_out, 'w+') as fo:
        with open(file_in, 'r') as fi:
            total_cases = int(fi.readline().rsplit()[0])
            for case in range(total_cases):
                transmitter = fi.readline().rsplit('\n')[0]
                msg = fi.readline()
                msg = msg.rsplit('\n')[0]
                r = decrypt(transmitter, msg)
                result = f'Case #{case+1}: {r}'
                
                print(result)
                fo.write(result+'\n')
                
if __name__ == "__main__":
    read_from_file('./5/submitInput', './5/submitOutput.txt')
