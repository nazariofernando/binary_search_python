
def binary_search(li, tar):

	li.sort()
	length = len(li)

	if len(li) <= 1:
		for n in li:
			if n == tar:
				return True
			else:
				return False

	if length % 2 == 0 and length != 0:
		length = length/2 - 1
	else:
		length = length/2

	else:
		if tar <= li[length]:
			return binary_search(li[:length+1], tar)
		else:
			return binary_search(li[length+1:], tar)
