import sys

if len(sys.argv) == 1:
    input_val = raw_input("Please enter upper limit:")
elif len(sys.argv) > 1:
    input_val = sys.argv[1]
        
try:
    n = int(input_val)
except ValueError:
    print "Please supply a numerical input."
    n = int(raw_input("Please enter upper limit:"))

print "Fizz buzz counting up to " + str(n)

i = 1

while (i<=n):
    if i % 3 == 0 and i % 5 == 0:
        print "fizz buzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i
    i +=1