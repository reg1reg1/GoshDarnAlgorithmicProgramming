noprimes = {j for i in range(2,8) for j in range (i*2,100,i)}
primes = [i for i in range(2,100) if i not in noprimes]
print primes