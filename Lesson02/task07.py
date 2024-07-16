import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

num = 7_901_903_776
print(num)

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)

print(0.1 + 0.2)
pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
print(pi)
