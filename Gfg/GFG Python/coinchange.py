# Dynamic Programming Python implementation of Coin 
# Change problem
# How many ways can we make the change
#Variation : Min number of coins used to make the change
def count(S, m, n):
 
    
    table = [0 for k in range(n+1)]
 
    
    table[0] = 1
 
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
            print("table[%d] is %d"%(j,table[j]))
 	
    return table[n]
 
arr = [9, 20, 13, 11]
m = len(arr)
n = 31
x = count(arr, m, n)
print (x)
