def solution(m, f):
    # convert to integer
    count, m, f = 0, int(m), int(f)
    
    # Let (m, f) be a 2-tuple of positive integers
    # Let a(m, f) = (m + f, f)
    # Let b(m, f) = (m, m + f)
    # m >= 1, f >= 1: Given
    # f < m + f and m < m + f
    # solution(m, f) = solution(f, m)
    
    # While it is possible to use these functions alone to solve the problem
    # by iterating through them until a match is found, we can actually work
    # backwards to find a solution
    
    # There is a very simple way to reduce (m, f) to its parent (a, b)
    # If m > f, m = a + b and f = b. We can then find a: m - f = a + b - b
    # Else, f = a and m = a + b. b = f - m
    
    # There is a faster way to reduce, however
    # Let (c, d) = a^n(m, f), where a^n is some n recursions of a
    # If we also assume that b(x, y) = (m, f), we can state that f > m
    # (c, d) = (m + nf, f)
    # (m + nf) / f = m / f + nf / f = n
    # (m + nf) % f = (m % f + nf % f) %f = (m % f) % f = m % f = m (Due to the special case f > m)
    # This means we can reduce by a^n instead of b^n
    
    # If all valid tuples (m, f) are represented as a tree,
    # where root = (1, 1) and children are a(head) and b(head)
    # All valid tuples must then have an ancestor (1, f) or (m, 1)
    # which can be solved in constant time
    
    # We can also state that no valid tuples, excepting the base (1, 1), will
    # have values where m = f, because these cannot be reduced to (1, f)
    # m + f = m -> f = 0; m + f = f -> m = 0
    # Using this property, we can define failure states
    # Let m = f
    # a(m, f) = (2m, m); b(m, f) = (m, 2m).
    # If we then define failure as f = cm or m = fm, we can identify
    # many failure states in constant time, and the rest will reduce to one
    # of them
    # This failure state can also be checked efficiently, assuming f != 1 and m != 1
    # min(f, m) % max(f, m) = 0 if and only if f = cm or m = cf
    
    # Check victory
    while min(m, f) != 1:
        # Check failure
        if max(m, f) % min(m, f) == 0:
            return 'impossible'
        # Given m and f, we can calculate the parent state
        count += max(m, f)/min(m, f)
        m, f = max(m, f) % min(m, f), min(m, f)
    
    return str(count + max(m, f) - 1)
    
print solution('4', '7')
print solution('1', '2')
