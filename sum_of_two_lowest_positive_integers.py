# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers

def sum_two_smallest_numbers(numbers):
    smallest = []
    for i, n in enumerate(numbers):
        if n > 0:
            smallest.append(n)
        if len(smallest) == 2:
            break
    
    for n in numbers[i+1:]:
        if smallest[0] > smallest[1]:
            smallest[0], smallest[1] = smallest[1], smallest[0]
        if n < smallest[1]:
            smallest[1] = n
    
    return sum(smallest)