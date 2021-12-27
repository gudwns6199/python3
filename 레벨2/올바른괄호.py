def solution(s):
    answer = True
    open_s = []
    s_lst = list(s)
    
    for i in range(len(s_lst)):
        if len(open_s) == 0:
            if s_lst[i] == ')':
                answer = False
                break
        
        else:
            if s_lst[i] == ')':
                open_s.pop()
                continue
                
        open_s.append(s_lst[i])

    if len(open_s) != 0:
        answer = False
        
    return answer
