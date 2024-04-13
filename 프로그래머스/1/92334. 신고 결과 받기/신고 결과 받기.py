from collections import Counter

def solution(id_list, report, k):
    repo_dict = {}
    repo_mail = dict(zip(id_list,[0]*len(id_list)))
    for repo in report:
        repo_user,repo_target = repo.split(' ')
        if repo_target not in repo_dict.keys():
            repo_dict[repo_target] = [repo_user]
        else:
            repo_dict[repo_target].append(repo_user)
            
    for repo_user in repo_dict.values():
        if len(set(repo_user)) >= k:
            for user in set(repo_user):
                repo_mail[user] += 1

    return list(repo_mail.values())