'''str으로 들어온 수식의 연산 순서에 따른 최대 절대값 찾는 문제
1. re로 인풋 parse
2. 연산자 set에 permutation 사용해서 완전탐색
3. list로 parsing된 수식에서 우선순위 연산자 위치 -1, +1 인덱싱 후 eval로 계산
4. 수식을 우선 계산된 값으로 update'''

import re
from itertools import permutations


def calculate_set(set_, ex_l):
    print('\n[Calculation]')
    print(f'operation order: {set_}')
    print(f'expression: {"".join(ex_l)}', end='\n\n')
    
    for op in set_:
        print(f'operation: {op}')
        while op in ex_l:
            print(f"{''.join(ex_l)}", end =' -> ')
            op_loc = ex_l.index(op)
            op_result = str(eval(''.join(ex_l[op_loc-1:op_loc+2])))
            ex_l = ex_l[:op_loc-1] + [op_result] + ex_l[op_loc+2:]
            print(f"{''.join(ex_l)}")
    return abs(int(ex_l[0]))

def solution(expression):
    print(f'Input expression: {expression}')
    
    ex_split = re.findall('[+-/*//()]|\d+', expression)
    print(f'expression parsed: {ex_split}')
    
    op_list = list(filter(lambda x: x in ['+', '-', '*'], ex_split))
    print(f'operations used: {op_list}')
    
    op_sets = list(permutations(set(op_list)))
    print(f'possible operation sequences: {op_sets}')

    return max([calculate_set(set_, ex_split) for set_ in op_sets])
  
