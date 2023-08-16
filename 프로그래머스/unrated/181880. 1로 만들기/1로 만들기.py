def solution(num_list):
    res = 0
    for n in num_list:
        while n!=1:
            if n%2:
                n = (n-1)//2
            else:
                n//=2
            res += 1
    return res