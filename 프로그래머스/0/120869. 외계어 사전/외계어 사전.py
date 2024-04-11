from itertools import permutations

def solution(spell, dic):
    combinaions = permutations(spell)
    for combo in combinaions:
        if ''.join(combo) in dic:
            answer = 1
            break
        else:
            answer = 2
    return answer