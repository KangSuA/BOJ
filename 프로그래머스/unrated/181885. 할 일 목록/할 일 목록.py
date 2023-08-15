def solution(todo_list, finished):
    return [s for i,s in enumerate(todo_list) if not finished[i] ]