def solution(s):
    answer = []
    txt = []
    s = s.split()
    for n in range(len(s)):
        txt.append(int(s[n]))

    answer.append(str(min(txt)))
    answer.append(str(max(txt)))
    
    answer = ' '.join(answer)
    
    
    return answer
