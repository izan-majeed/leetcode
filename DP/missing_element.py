def missing_element(arr, sub):
	for i in arr:
		if i not in sub:
			return i

def missing_element_II(arr, sub):
	return sum(arr)-sum(sub)

def missing_element_III(arr, sub):
	arr.sort()
	sub.sort()
	for i in range(len(arr)):
		if arr[i] != sub[i]:
			return arr[i]


print(missing_element([11, 44, 55, 90, 1, 90], [44, 1, 90, 11]))
print(missing_element_II([11, 44, 55, 90, 1], [44, 1, 90, 11]))
print(missing_element_III([11, 44, 55, 90, 1], [44, 1, 90, 11]))