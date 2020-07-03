# Check Codility link below for description of the problem
# Lesson3 – CountingElements – MissingInteger
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

# my solution – scored 100/100 –


def solution(A):
    dictA = {a for a in A}
    for i in range(1,len(A)+2):
        if i not in dictA:
            return i
