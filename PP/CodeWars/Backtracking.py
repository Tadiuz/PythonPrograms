# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

# My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.

# Task
# Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

# If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:

# Examples
# decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

# For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

# Note
# Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

# The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

# [x1 ... xk] or
# "x1 ... xk" or
# Just [x1 ... xk] or
# Some [x1 ... xk] or
# {x1 ... xk} or
# "[x1,x2, ... ,xk]"
# depending on the language (see "Sample tests")

# Note for Bash
# decompose 50 returns "1,3,5,8,49"
# decompose 4  returns "Nothing"
# Hint
# Very often xk will be n-1.



def is_valid_state(lista, n):


	if n in lista:
		return False

	if n <= 0:
		return False

	return True
    # check if it is a valid solution


# def get_candidates(state):
#     return []

def search(lista, n, value, minimum):

	if sum([i**2 for i in lista]) == N:
		print("Here with: ", lista)
		return True

	for i in range(0, minimum + 1):
		print(lista, "n: ",n-i, "value: ",value, end=" ")
		
		if is_valid_state(lista, n-i):
			lista.append(n-i)
			new_value = value - (n-i)**2
			new_exp = int((new_value)**(1/2))
			print("new_exp:  ", new_exp, end=" ")
			print("new_value:  ", new_value, end=" ")
			
			new_n = new_exp
			new_min = new_n//2 #- (int((n-i)**(1/2)) -1)
			print("new_min:  ", new_min, end=" ")
			print("New list: ", lista)
			input()
			
			if search(lista, new_n, new_value, new_min):
				return True
		
			lista.pop()

		
	return False
N = 0

def solve(n):
	"""
	
	:return list containing the elements
	"""
	global N
	N = n**2
	value = n**2 - (n-1) ** 2

	lista = []

	if search(lista, n-1, n**2, int(n/2)):
		print("Ok")
	print(lista)

lista = solve(7100)



# def is_valid_state(lista, n):

# 	if n in lista:
# 		return False

# 	if n <= 0:
# 		return False

# 	return True

# def search(lista, n, value, minimum):

# 	if sum([i**2 for i in lista]) == N:
# 		return True

# 	for i in range(0, minimum + 1):
# 		if is_valid_state(lista, n-i):
# 			lista.append(n-i)
# 			new_value = value - (n-i)**2
# 			new_exp = int((new_value)**(1/2))

# 			new_n = new_exp
# 			new_min = new_n//2
			
# 			if search(lista, new_n, new_value, new_min):
# 				return True
# 			lista.pop()
# 	return False

# N = 0
# def solve(n):
# 	"""
	
# 	:return list containing the elements
# 	"""
# 	print(n," ", n**2)
# 	global N
# 	N = n**2
# 	value = n**2 - (n-1) ** 2
# 	lista = []
	
# 	if search(lista, n-1, n**2, int(n/2)):
# 		return lista[::-1]

# def decompose(n):   
# 	return solve(n)
