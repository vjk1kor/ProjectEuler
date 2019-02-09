# Problem-1
# https://projecteuler.net/problem=1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


print ("The solution has been implemented in a generic sense.")
print ("Here you will be able to find the sum of the numbers divisible by either of 2 given numbers upto a certain number.")
print ("In order to get the answer for the original Euler problem, enter the 1st number as 3, the 2nd number as 5 and the final number as 1000.\n")

print ("Enter the 1st number: ", end='')
firstN = int(input())
print ("Enter the 2nd number: ", end='')
secondN = int(input())
print ("Enter the upper limit: ", end='')
upperLimit = int(input())

firstNUpper = 0
i = upperLimit - 1
while (0 != i % firstN):
    i = i - 1
firstNUpper = i

secondNUpper = 0
i = upperLimit - 1
while (0 != i % secondN):
    i = i - 1
secondNUpper = i

# LCM
# First define GCD function
def gcd (x, y):
    """This function implements the Euclidian algorithm
    to find G.C.D. of two numbers"""

    while (y):
        x, y = y, (x % y)

    return x

# Define LCM function
def lcm (x, y):
    """This function takes two
    integers and returns the L.C.M."""

    lcm = (x*y)//gcd(x,y)
    return lcm

lcm = lcm(firstN, secondN)
lcmUpper = 0
i = upperLimit - 1
while (0 != i % lcm):
    i = i - 1
lcmUpper = i

# The sum is calculated in the follwoing manner
# If the first number is 3, then
# Sum of all number divisble by 3 is;
# SUM = 3+6+9+12+...+999
# SUM = 3*(1+2+3+4+...+333)
# And the sum of numbers divisible by 5 is;
# SUM  = 5+10+15+20+...+995
# SUM = 5*(1+2+3+4+...+199)
# The sum on N natural numbers can be expressed as N*(N+1)/2

def sumDivisibleBy(n, p):
    return n*((p/n)*((p/n)+1)/2)

summation = sumDivisibleBy(firstN, firstNUpper) + sumDivisibleBy(secondN, secondNUpper) - sumDivisibleBy(lcm, lcmUpper)

print ("The sum of all multiples of", firstN, "and", secondN, "below", upperLimit, "is:", int(summation))