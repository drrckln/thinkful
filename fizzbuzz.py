import sys

# sys.argv is a list of strings
# assume that a person will only put 1 additional argument
# ignore the rest
# python fizzbuzz.py 10

def fizzbuzz():
    if len(sys.argv) > 1:
        # user supplied value
        # sys.argv is ['fizzbuzz.py', '10']
        user_input = sys.argv[1]
        # user_input would be '10'
    else:
        #alternate
        user_input = raw_input("How far do you want to go? (1-?): ")

    # You'll notice here that no matter what happens, right now user_input is a
    # string

    while True:
        try:
            user_input = int(user_input)
            break
        except:
            print "That's not a number!"
            user_input = raw_input("How far do you want to go? (1-?): ")

    user_range = range(1,user_input+1)

    # do with a while loop as well
    for num in user_range:
        if num % 3 == 0 and num % 5 == 0:
            print "Fizz Buzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num
