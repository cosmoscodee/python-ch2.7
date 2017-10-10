import math
import mymath

# 두개다 pi 가 있음

print(math.pi)
print(mymath.pi)

x = 1


def f():
    y = x + 1
    print(x)

    def g():
        a = y + 1

    for i in range(5):
        g()
        print(y)


f()
