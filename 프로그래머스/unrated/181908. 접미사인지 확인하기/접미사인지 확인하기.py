def solution(my_string, is_suffix):
    return int(is_suffix in [my_string[-i:] for i in range(len(my_string))])