import math

def GenerateBinary(size):
	minVal = int(math.pow(2,size-1))
	maxVal = int(math.pow(2,size))
	
	for i in range(minVal, maxVal):
		if (i%2 != 0):
			binVal = bin(i)[2:]
			print("Case #{}: {}".format(i,binVal))

# Main
# read a line with a single integer
t = int(input())

for i in range(1, t + 1):
# read a list of integers, 2 in this case
  size, m = [int(s) for s in input().split(" ")]  
 
  
  GenerateBinary(size)
  
  #print("Case #{}: {}".format(i, ,))
  # check out .format's specification for more formatting options
