import numpy as np

def solution(s):
    word = np.array(list(s.lower()))
    if np.sum(word == 'p') == np.sum(word == 'y') :
        return True
    else : 
        return False