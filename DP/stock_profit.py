def stock_profit(a):
	min_ele = a[0]
	max_profit = 0

	for i in range(1, len(a)):
		min_ele = min(a[i], min_ele)
		max_profit = max(a[i]-min_ele, max_profit)

	return max_profit


print(stock_profit([11, 44, 55, 90, 1, 90]))