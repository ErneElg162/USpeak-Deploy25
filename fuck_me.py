import math

def calcError(v, phoenemArray, r, t):
    err = 0
    for i in range(len(phoenemArray)):
        err += (r((v[i + t]) - phoenemArray[i])**2)
    return err

phoenemArray = [1,2,3]
v = [1,2,3]
calcError(v, phoenemArray, 3, 4)    
print(4)
    
    
        