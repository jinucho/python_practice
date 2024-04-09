from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    common_elements = count_X & count_Y
    if not common_elements:
        return "-1"
    answer = ''.join([key*common_elements[key] for key in sorted(list(common_elements.keys()),reverse=True)])
    
    if answer == "0"*len(answer):
        return "0"
    return answer

