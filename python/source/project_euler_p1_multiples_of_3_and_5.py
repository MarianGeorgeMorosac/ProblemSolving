import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

# Statement: Sum of all multiples of 3 and 5 below 1000 = ?

limit = int(sys.argv[1])

answer = sum([ i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(0, limit)])

print("Answer is ", answer)
