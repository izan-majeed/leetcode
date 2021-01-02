def longest_increasing_subseq(arr):
	n = len(arr)
	LIS = [1]*n
	max_length = 1

	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j]:
				LIS[i] = max(LIS[i], LIS[j]+1)

	for i in range(n):
		max_length = max(max_length, LIS[i])

	return max_length

print(longest_increasing_subseq([11, 23, 10, 37, 21, 50, 80]))
