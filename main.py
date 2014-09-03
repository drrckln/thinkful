import sys
from fizzbuzz import fizzbuzz

sys.argv.append(1)

for num in range(30,40):
    sys.argv[1] = num
    fizzbuzz()
