def latest(scores):
    return scores[-1]


def personal_best(scores):
    top_score = 0
    for i in range(len(scores)):
        if scores[i] > top_score:
            top_score = scores[i]
    return top_score


def personal_top_three(scores):
    if len(scores) == 0:
        return None
    sorted_scores = sorted(scores)
    if len(scores) >= 3:
        return [sorted_scores[-1], sorted_scores[-2], sorted_scores[-3]]
    elif len(scores) == 2:
            return [sorted_scores[-1], sorted_scores[-2]]
    elif len(scores) == 1:
            return [sorted_scores[-1]]


