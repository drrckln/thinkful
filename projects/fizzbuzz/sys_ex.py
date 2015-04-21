import sys

print sys.argv

if len(sys.argv) > 1:
    my_input = sys.argv[1]
else:
    my_input = raw_input("Pick a number: ")


for num in range(1,my_input+1):
    print num
