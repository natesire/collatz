# Collatz Conjecture
# 3n+1 works for any positive n
# 6n+1 works for 4, 8
# 9n + 1 works for 3, 6, 7, 8

# pick any positive n from 1 to 9 inclusive
# can try larger numbers too
# 3n+1 will toggle even odd so applying it to odds will result in evens
# this means there won't be consecutive odd growth
# more chances to find a power of 2 that reduces all the way down to the 4,2,1 loop
def formulaIfOdd(n, multiplyBy=3):
    return multiplyBy * n + 1    

# def function with named parameters

def calculateConjecture(n, multiplyBy=3):
    print("Conjecture for " + str(n) + " is multiplied by " + str(multiplyBy) + " * n + 1")
    while(1):
        if n == 1.0:
            break
    
        # if r is even then divide by 2
        if n % 2 == 0.0:
            n = n / 2
            print(n)
        else: # if odd apply the 3n + 1
            n = formulaIfOdd(n, multiplyBy)
            print(n)
            
        print("DR: " + str(digitalRoot(n)))
    return n

def digitalRoot(n):
    return (n - 1) % 9 + 1

# 3n+1 toggles odds and evens
# turning all odds to evens means you always eventually hit a power of 2 which reduces back to the 4,2,1 loop
#calculateConjecture(n=3, multiplyBy=3)
calculateConjecture(n=12, multiplyBy=3)
# the digital root always stays on the doubling plane. never 3,6,9
# the median number should revolve around 2^n
# calculateConjecture(n=1000, multiplyBy=3) # digital root 1,2,4,5,7,8

# large number loop for 4n+1
# no has proved large number loop(s) don't exist for 3n+1
# calculateConjecture(6,4) # digital root 1,5,2
# calculateConjecture(10,4) # digital root 1,8,9

# will it ever hit a number that's a power of 2? that's the question
# these reduce to 4,2,1
# calculateConjecture(1,4)
# calculateConjecture(2,4)
# calculateConjecture(3,4) # too large to know, breaks the number limit
# calculateConjecture(4,4)
# calculateConjecture(5,4)
# calculateConjecture(7,4) # too large to know, breaks the number limit
# calculateConjecture(8,4)
# calculateConjecture(9,4) # too large to know, breaks the number limit

# 8 works with any multiplier. it is the infinite number. God's number. twisted zero into plane of existance.
# opposite, pick same n for different k*n+1
# n=8 works for all k*n+1
# this just shows that all multiples of n=2 will reduce back to the 4,2,1 loop
'''calculateConjecture(8, 1)
calculateConjecture(8, 2)
calculateConjecture(8, 3)
calculateConjecture(8, 4)
calculateConjecture(8, 5)
calculateConjecture(8, 6)
calculateConjecture(8, 7)
calculateConjecture(8, 8)
calculateConjecture(8, 9)
calculateConjecture(8, 91)
calculateConjecture(8, 91212) # try some big number'''

# 6n+1 turns any number odd which means it can never be a power of 2
# that's why either infinite loop or large number loop
# calculateConjecture(3, 6) # infinite
#calculateConjecture(4, 6) # 4,2,1
# calculateConjecture(5, 6) #infinite
# calculateConjecture(6, 6) #loop
#calculateConjecture(7, 6) # infinite
#calculateConjecture(8, 6) # 4,2,1