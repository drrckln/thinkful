import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
#args = parser.parse_args()

#print args.square
#print args.square**2

parser.add_argument("--verbosity", help="increase output verbosity", action ="store_true")
args = parser.parse_args()
print args.square**2

print args.verbosity

if args.verbosity:
    print "verbosity turned on"
