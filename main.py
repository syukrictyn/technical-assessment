from itertools import permutations

def get_max_skill (n, m, a, b):
    max_skill = m
    for perm in permutations(range(n)):
        current_skill = m
        for i in perm:
            if current_skill >= a[i]:
                current_skill += b[i]
            else:
                break
                max_skill = max(max_skill, current_skill)
                return max_skill

    if __name__== '__main__':
        n, m = 4, 2
        a = [8, 9, 3, 2]
        b = [5, 4, 1, 3]
        print(get_max_skill(n, m, a, b))

