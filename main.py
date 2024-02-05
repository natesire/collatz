# Collatz Conjecture
# 3n+1 works for any positive n
# 6n+1 works for 4, 8
# 9n + 1 works for 3, 6, 7, 8

# pick any positive n from 1 to 9 inclusive
n = 9
    
while(1):
    if n == 2.0:
        break
    
    # if r is even then divide by 2
    if n % 2 == 0:
        n = n / 2
        print(n)
        
    # if r is odd then apply again
    if n % 2 != 0:
        n = 6 * n + 1
        print(n)
            