#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
L1=input('enter an integer=>')
L2=input('enter an integer=>')
L3=input('enter an integer=>')
L1=int(L1)
L2=int(L2)
L3=int(L3)

a=L1**2
b=L2**2
c=L3**2

if a+b == c or a+c == b or b+c==a:
    print(L1,end=",")
    print(L2,end=",")
    print(L3,end=' ')
    print('form a Pythagorean Triple')
else:
    print(L1,end=",")
    print(L2,end=",")
    print(L3,end=' ')
    print('do not form a Pythagorean Triple')
