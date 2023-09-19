def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = None
    max_key = None

    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            max_key = key

    return max_key


scores_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Aloni': 150}

best_student = best_score(scores_dict)