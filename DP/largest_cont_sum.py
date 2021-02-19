def largest_cont_sum(a):
    curr_sum, max_sum = a[0], a[0]
    for num in a[1:]:
        curr_sum = max(num, curr_sum+num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(largest_cont_sum([11, 22, 33, 44, 55, -66, -77, 88, 99]))
print(largest_cont_sum([11, 22, 33, 44, 55, -66, -77, -88, 99]))
print(largest_cont_sum([11, 22, 33, 44, -55, -66, -77, 88, 99]))