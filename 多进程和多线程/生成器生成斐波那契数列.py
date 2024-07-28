"""

"""


def fun(num):
    a, b = 0, 1  # a,b分别记录第n项和第n+1项
    for i in range(num):
        yield a
        a, b = b, a + b


f = fun(10)
for i in f:
    print(i)
