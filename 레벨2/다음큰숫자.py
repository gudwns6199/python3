from collections import Counter
def solution(n):
    answer = 0
    a= list(bin(n))
    a=a[2:]
    a_chc = (Counter(a))
    c = n+1
    while c > n:
        c_list = list(bin(c))
        c_list = c_list[2:]
        c_chc = Counter(c_list)
        if c_chc['1'] == a_chc['1']:
            break
        c += 1
        
    answer = c
    return answer
