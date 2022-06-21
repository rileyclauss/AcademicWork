def product(lst):
	# multiplies the two numbers in a two-number list
	first = lst[0]
	second = lst[1]
	product = first * second
	return product

def recProductSum(lst, sum):
	if lst == []:
		return sum
	firstElem = lst[0]
	newSum = sum + product(firstElem)
	restOfList = lst[1:]
	return recProductSum(restOfList, newSum)

print(recProductSum([[1,2], [3,4], [5,6]], 0))