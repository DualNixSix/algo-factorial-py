def factorial(num):
	fact = 1
	for f in range(2, num + 1):  # for loop iterates; range from 2 to num; num = 5 range is (2, 6): 2, 3, 4, 5
		fact *= f  # multiply fact by f and return result
	return fact
pass