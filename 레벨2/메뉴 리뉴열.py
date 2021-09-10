from itertools import combinations

def solution(orders, course):
    answer = []
    course_s = []
    
    for n in course:
        count = []
        
        for m in range(len(orders)):
            if n > len(orders[m]):
                continue
                
            orders[m] = sorted(list(orders[m]))
            
            course_s = list(combinations(orders[m],n))
            
            for x in range(len(course_s)):
                count.append(''.join(course_s[x]))
        
        if count == []:
            continue
            
        count.sort()
        
        check = {}
        check.setdefault(count[0],1)
        count_str = 1
        
        for y in range(1,len(count)):
            if count[y-1] == count[y]:
                check[count[y-1]] += 1
            else:
                check.setdefault(count[y],1)
        print(check)        
        for k, v in check.items():
            if v == max(sorted(check.values(), reverse = True)) and v >= 2:
                answer.append(k)
                
    answer.sort()
    return answer
