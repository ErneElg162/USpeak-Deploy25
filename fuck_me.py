import math

def calcError(v, phoenemArray, r, t):
    err = 0
    n = len(phoenemArray)
    for i in range(n):
        err += (r * v[i + t] - phoenemArray[i]) ** 2
    return err
    

p_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
why = calcError(v_list, p_list, 1, 0)    
print(why)
    