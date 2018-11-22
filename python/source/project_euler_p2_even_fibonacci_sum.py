import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

# Statement: Even fibonacci sequence items below 4MM  

limit = int(sys.argv[1])

fib = [0, 1, 1]
answer = 0
while fib[-1] < limit:
	max_copy = fib[-1]
	fib[-1] = fib[-1] + fib[-2]
	fib[-3] = fib[-2]
	fib[-2] = max_copy
	if fib[-1] % 2 == 0:
		answer += fib[-1]

print("Answer is ", answer)
