def solution(my_string, queries):
    for s,e in queries:
        my_string = my_string[:s] + my_string[e:s:-1] + my_string[s] + my_string[e+1:]
    return my_string