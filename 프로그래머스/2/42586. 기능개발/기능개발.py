import numpy as np

def solution(progresses, speeds):
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    answer = []
    for _ in range(100-min(progresses)):
        progresses += speeds
        progresses[progresses > 100] = 100
        if progresses[0] == 100:
            try :
                point = np.where(progresses < 100)[0].min()
                answer.append(int(sum(progresses[:point]==100)))
                progresses,speeds = progresses[point:], speeds[point:]
            except:
                answer.append(int(sum(progresses==100)))
                break
            
    return answer