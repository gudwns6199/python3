def solution(n):
    p = [0,1]
    for x in range(2,n+1):
        p.append(p[x-1]+p[x-2])
    answer = p[-1]%1234567
    return answer
