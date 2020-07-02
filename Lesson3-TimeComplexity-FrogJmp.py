# Check Codility link below for description of the problem
# Lesson3 – TimeComplexity – FrogJmp
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

# my solution – scored 100/100 –

def solution(X, Y, D):
	if X==Y:
		return 0
	elif X<Y:
		r=(Y-X)%D
		if r==0:
			return int((Y-X)/D)
		else:
			return int((Y-X)/D)+1
