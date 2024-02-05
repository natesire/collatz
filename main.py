# Collatz Conjecture
# 3n+1 works for any positive n
# 6n+1 works for 4, 8
# 9n + 1 works for 3, 6, 7, 8

# what about 4n+1
# works for 4, 8
# 6 and 10 stuck in a large infinite loop

# pick any positive n from 1 to 9 inclusive
# can try larger numbers too
n = 3
    
def formula(n):
    return 3 * n + 1    
    
while(1):
    if n == 1.0:
        break
    
    # if r is even then divide by 2
    if n % 2 == 0.0:
        n = n / 2
        print(n)
    else: 
        n = formula(n)
        print(n)