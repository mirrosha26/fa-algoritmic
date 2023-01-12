def flip(pancakes,how_sort, pk):
	print(pancakes, end =" ")
	print(pk+ 1)
	how_sort.append(pk+ 1)
	start = 0
	while start < pk:
		a = pancakes[start]
		pancakes[start] = pancakes[pk]
		pancakes[pk] = a
		start += 1
		pk -= 1

def max_pancake(pancakes, n):
	m = 0
	for i in range(0,n):
		if pancakes[i] > pancakes[m]:
			m = i
	return m


def pancake_sort(pancakes, n):
	how_sort = []
	curr_size = n
	while curr_size > 1:
		mi = max_pancake(arr, curr_size)
		if mi != curr_size-1:
			if mi != 0:
				flip(pancakes, how_sort, mi)
			flip(pancakes, how_sort, curr_size-1)
		curr_size -= 1
	return how_sort


# тест
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
print(pancake_sort(arr, n))
