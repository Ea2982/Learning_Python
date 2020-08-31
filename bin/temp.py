

>>> def make_stars(x):
...     if x > 0:
...         return True, '*' * x
...     return False, ''
...
>>> for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
...     print(s)
...
*
*****
**