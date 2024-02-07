# importing matplotlib module 
from matplotlib import pyplot as plt


n=12
z=[]
 
while(1):
    if n == 1.0:
        break
            # if r is even then divide by 2
    if n % 2 == 0.0:            
        n = n / 2
        z.append(n)
    else: # if odd apply the 3n + 1
        n = 3*n+1
        z.append(n)
            
 
# raise number to power
# 2^0 = 1
2**2
 
# x-axis values
y = [1**2, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9]
 
# Y-axis values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

o = [1,2,3,4,5,6,7,8,9]
 
# Function to plot
plt.plot(x, y)
plt.plot(o, z)
 
# function to show the plot
plt.show()