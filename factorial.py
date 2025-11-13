def factorial(num):
	fact = 1
	for f in range(1, num + 1):  # for loop iterates; range from 1 to num; num = 5 range is (1, 6): 1, 2, 3, 4, 5
		fact *= f  # multiply fact by f and return result
	return fact