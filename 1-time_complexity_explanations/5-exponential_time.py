'''
Exponential Time complexity refers to an algorithm whose growth doubles with each additon to the input data set. 2^n

Examining every subset of a set/array can be an example for this one.

If the list is:

[] - 0 elements => 1 subset (2^0)
[a] - 1 elements => 2 subsets => [], [a] (2^1)
[a,b] - 2 elements => 4 subsets => [], [a] , [b] , [a.b] (2^2)
[a,b,c] - 3 elements => 8 subsets => [], [a] , [b] , [c], [a.b], [a,c], [b,c], [a,b,c] (2^3)
.
.
.


'''
