# https://www.codewars.com/kata/good-vs-evil

def goodVsEvil(good, evil):
    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]

    good_sum = sum(map(lambda x, y: x * y, points_good, (int(x) for x in good.split(" "))))
    evil_sum = sum(map(lambda x, y: x * y, points_evil, (int(x) for x in evil.split(" "))))

    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    if evil_sum > good_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    if good_sum == evil_sum:
        return "Battle Result: No victor on this battle field"