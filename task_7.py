from math import factorial


def fact(n):
    for i in range(1, n+1):
        yield factorial(i)


g = fact(10)
for b in g:
    print(b)
print()
print(g)
