# Sqrt in logn time

USing newtonian method (See reference) approximating the square root.
The algorithm uses recursion with almost halved values ending up in log n iterations

Time O(n) = log n
Space O(n) = log n.

Stack trace:
Taking a example 9
recursqrt(9)
- recursqrt(5)
    - recursqrt(3.4)

# References
https://cp-algorithms.com/num_methods/roots_newton.html