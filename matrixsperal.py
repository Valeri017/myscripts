def print_(*kwargs):
    for y in kwargs:
        a = print (''.join(["%4d"%x for x in y])
    return a
 
SIZE = 13
 
def change(matrix, step, val): 
    if step >= SIZE - step:
        return matrix
    
    for i in range(step, SIZE - step):
        matrix[SIZE - step - 1][i] =    SIZE - 1  - 3*step + i + val
        matrix[i][SIZE - step - 1] = 3*(SIZE - 1) - 5*step - i + val
        matrix[step][i]            = 4*(SIZE - 1) - 7*step - i + val
        matrix[i][step]            =              -   step + i + val
        
    return change(matrix,  step + 1, 4*(SIZE - 1) - 8*step + val)
        
 
matrix = [[0 for x in range(SIZE)] for y in range(SIZE)]
print_(*change(matrix, 0, 0))
