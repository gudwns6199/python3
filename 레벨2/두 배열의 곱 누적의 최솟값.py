def solution(A,B):
    answer = 0

    A.sort(reverse = True)
    B.sort()
    
    for n in range(len(A)):
        answer += A[n]*B[n]

    return answer
