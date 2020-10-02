#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""

N=(input('enter an number')).strip()
N=int(N)
print(N,end=" ")
C=N**(1/3)
C = (round(C))
import math
if math.sqrt(N)==int(math.sqrt(N)) and C==int(C):
    print('is both a perfect square and a perfect cube.')
elif math.sqrt(N)==int(math.sqrt(N)):
    print('is only a perfect square.')
elif C==int(C):
    print('is only a perfect cube.')