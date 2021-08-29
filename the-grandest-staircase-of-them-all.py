# Every valid staircase has at least a set h of heights.
# The problem states that h[i] > h[i + 1], meaning that every element of h is distinct
# sum(h) = n.
# h is then a distinct partition of n.
# There is no simple formula to calculate the number of distinct partitions of n.
# There is, however, a generator function: product[i=1, inf](1 + x^i). 
# The number of distinct partitions is the coefficient of x^n when the product is expanded to n

def solution(n):
  # Store coefficients (1 at position represents 1*x^0 = 1)
  coefficients = [1] + [0] * n

  # Multiply (1 + x^i) into the stored polynomial
  for i in range(1, n + 1):

    # Distribute (1 + x^i) into the stored polynomial
    for j in range(n, i - 1, -1):
      coefficients[j] += coefficients[j - i]
  
  # For any n, exactly one distinct partition of n will be [n], which represents a single step and is not valid for the problem.
  return coefficients[n] - 1

#print solution(0)
#print solution(1)
#print solution(2)
#print solution(3)
#print solution(4)
print solution(5)
#print solution(6)
#print solution(7)
#print solution(8)
#print solution(9)
#print solution(10)
#print solution(200)

