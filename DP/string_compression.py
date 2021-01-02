def string_compression(s):
	n = len(s)
	string = ''
	count = 1
	for i in range(n):
		if i<n-1:
			if s[i] == s[i+1]:
				count += 1
			elif s[i] != s[i+1]:
				string = string + s[i] + str(count)
				count = 1
				
		#edge_case:
		elif i==n-1:
			if (s[i] == s[i-1]):
				string = string + s[i] + str(count)
			elif (s[i] != s[i-1]):
				string = string + s[i] + '1'
	return string



print(string_compression('CCCCCCHHHHHHHHHHHHOOOOOO'))