from typing import Optional
# def show_count(count,word):
#     if count == 1:
#         return f'1 {word}'
#     count_str = str(count) if count else 'no'
#     return f'{count_str} {word}s'

# def show_count(count:int,singular:str,plural:str = '') ->str:
#     if count == 1:
#         return f'1 {singular}'
#     count_str = str(count) if count else 'no'
#     if not plural:
#         plural = singular + 's'
#     return f'{count_str} {plural}'

def show_count(count:int,singular:str,plural:Optional[str] = None) ->str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'


print(show_count(0,'bird'))