

def binary_search(li, tar):

	li.sort()

	first = 0
	last = len(li) - 1
	found = False

	while first <= last and not found:
		mid = (first + last)//2
		if li[mid] == tar:
			found = True
		else:
			if tar < li[mid]:
				last = mid - 1
			else:
				first = mid + 1

	return found


lis1 = [1, 2, 3, 4, 5]
lis2 = [1, 2, 3, 4]
lis3 = [1, 2]
lis4 = [1]

a = 3
print binary_search(lis1, a)
print binary_search(lis2, a)
print binary_search(lis3, a)
print binary_search(lis4, a)




