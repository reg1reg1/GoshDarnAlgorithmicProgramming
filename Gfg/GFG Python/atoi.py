# your task is to complete this function
# function should return an integer
def valid(x):
    for i in range(0, len(x)):
        if ord(x[i]) < 48 or ord(x[i]) > 57:
            return False
    return True
    
def atoi(string):
    if not valid(string):
        return -1
    z = ord(string[0])-ord('0')
    #print("init z",z)
    for i in range(1,len(string)):
        z = z*10+(ord(string[i])-ord('0'))
        #print(z)
    return z
try:
t =int(input())  
for i in range(0,t):
    strinp = input()
    #print("Input string",strinp)
    ans=atoi(strinp)
    print(ans)
except :
     print "Unexpected error:", sys.exc_info()[0]
    