def solution(numbers, n):
    res = 0
    for num in numbers:
        res += num
        if res > n:
            return res