# Check Codility link below for description of the problem
# Lesson3 – TimeComplexity – TapeEquilibrium
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

# my solution – scored 100/100 –

def solution(A):
	ls = []
	s1 = A[0]
	s2 = sum(A[1::])
	ls.append(abs(s1-s2))
	for i in range(1,len(A)-1):
		s1 += A[i]
		s2 -= A[i]
		ls.append(abs(s1-s2))
	return min(ls)
