def stair_case(n):
	ways = [None]*(n+1)
	ways[0], ways[1] = 1, 1

	if n>1:
		for i in range(1, n+1):
			ways[i] = ways[i-1] + ways[i-2]

	return ways[n]


if __name__ == "__main__":

	t = int(input("Number of times you want to run this Program: "))
	for i in range(t):
		n = int(input(f"\n{i+1}. Number of Stairs: "))
		print(f"There are {stair_case(n)} ways.\n")

