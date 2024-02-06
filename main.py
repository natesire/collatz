# Collatz Conjecture
# 3n+1 works for any positive n
# 6n+1 works for 4, 8
# 9n + 1 works for 3, 6, 7, 8

# what about 4n+1
# works for 4, 8
# 6 and 10 stuck in a large infinite loop

# pick any positive n from 1 to 9 inclusive
# can try larger numbers too
def formulaIfOdd(n, multiplyBy=3):
    return multiplyBy * n + 1    

def calculateConjecture(n, multBy=3):
    print("Conjecture for " + str(n))
    while(1):
        if n == 1.0:
            break
    
        # if r is even then divide by 2
        if n % 2 == 0.0:
            n = n / 2
            print(n)
        else: 
            n = formulaIfOdd(n, multBy)
            print(n)
    return n

# start at, multiply * n + 1
calculateConjecture(3)
calculateConjecture(3, 3)
calculateConjecture(1000, 3)

# 8 works with any multiplier. it is the infinite number. God's number. twisted zero into plane of existance.

# n=8 works for any k*n+1
calculateConjecture(8, 1)
calculateConjecture(8, 2)
calculateConjecture(8, 3)
calculateConjecture(8, 4)
calculateConjecture(8, 5)
calculateConjecture(8, 6)
calculateConjecture(8, 7)
calculateConjecture(8, 8)
calculateConjecture(8, 9)
calculateConjecture(8, 91)
calculateConjecture(8, 912)
