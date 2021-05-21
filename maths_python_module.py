Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import maths
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.ceil(2.3)
3
>>> math.floor(2.3)
2
>>> math.ceil(2.38)
3
>>> int(2.3)
2
>>> int(2.3) + 1
3
>>> math.factorial(5)
120
>>> math.fabs(-2.3)
2.3
>>> math.fabs(2.3)
2.3
>>> math.gcd(4,5,12)
1
>>> math.gcd(4,12)
4
>>> math.lcm(2,3)
6
>>> math.lcm(50,100)
100
>>> math.perm(4,2)
12
>>> math.comb(4,2)
6
>>> math.remainder(2,3)
-1.0
>>> math.remainder(3,2)
-1.0
>>> a = [1,2,3,4]
>>> math.prod(a)
24
>>> 