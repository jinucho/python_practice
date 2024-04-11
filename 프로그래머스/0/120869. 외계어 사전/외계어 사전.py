def solution(spell, dic):
    for word in dic:
        if len(spell) == len(word) and all(s in set(word) for s in spell):
            answer = 1
            break
        else :
            answer = 2
    return answer