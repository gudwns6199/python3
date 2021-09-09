def solution(n):
    answer = 0
    
    for x in range(1,n+1):
        sum_n = 0
        num = x
        
        while sum_n < n:
            sum_n = sum_n + num
            num += 1
            
        if sum_n == n:
            answer += 1
        
    return answer
