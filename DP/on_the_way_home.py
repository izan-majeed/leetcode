def ways(n, m):
	grid = [[None]*m]*n

	for i in range(m):
		grid[n-1][i] = 1
	for i in range(n):
		grid[i][m-1] = 1

	for i in range(n-2,-1,-1):
		for j in range(m-2,-1,-1):
			grid[i][j] = grid[i][j+1] + grid[i+1][j]

	return grid[0][0]
	

if __name__ == "__main__":

	t = int(input("Number of times you want to run this Program: "))
	for i in range(t):
		n, m = map(int, input(f"\n{i+1}. Grid Size (n*m): ").split())
		result = ways(n, m)
		print(f"There are {result} ways.\n")

