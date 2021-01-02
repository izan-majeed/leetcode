def cal_sum_array(arr):
	n = len(arr)
	sum_array = [None] * n
	sum_array[0] = arr[0]

	for i in range(1, n):
		sum_array[i] = sum_array[i-1] + arr[i]
	return sum_array
	

def sum_of_the_range(sum_array, l, h):
	if l==0:
		return sum_array[h]
	else:
		return (sum_array[h] - sum_array[l-1])


arr = [1, -2, 3, 10, -8, 0]
sum_array = cal_sum_array(arr)

print(sum_of_the_range(sum_array, 3, 5))
print(sum_of_the_range(sum_array, 4, 4))
print(sum_of_the_range(sum_array, 0, 3))
print(sum_of_the_range(sum_array, 1, 2))


