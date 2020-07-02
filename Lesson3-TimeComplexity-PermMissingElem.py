# Check Codility link below for description of the problem
# Lesson3 – TimeComplexity – PermMissingElem
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

# my solution – scored 100/100 –


def solution(A):
	N = len(A)
	if 1 not in A:
		return 1
	elif N+1 not in A:
		return N+1
	else:
		A.sort()
		for i,e in enumerate(A):
			if i+1!=e:
				return e-1
