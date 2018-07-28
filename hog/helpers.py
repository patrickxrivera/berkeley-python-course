def to_list(score):
    return list(map(int, str(score)))

def get_score(sum):
    return sum % 10 + 1
