def flip(pancakes, pk):
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
	curr_size = n
	while curr_size > 1:
		mi = max_pancake(arr, curr_size)
		if mi != curr_size-1:
			flip(pancakes, mi)
			flip(pancakes, curr_size-1)
		curr_size -= 1

# тест
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
pancake_sort(arr, n)
print(arr)