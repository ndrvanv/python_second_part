import sys

STEP = 2 ** 16
num = 1

for _ in range(30):
    print(sys.getrefcount(num), num)
    num *= STEP