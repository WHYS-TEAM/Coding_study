def solution(numbers, target):
    '''모든 경우의 수 결과 저장 후 target 수 return'''
    
    print(f'numbers: {numbers} | target: {target}')
    
    # 다 더하면 target이 되는 경우
    if sum(numbers) == target: return 1
    
    # 연산 수행 결과 저장
    results = []
    for opt_set in itertools.product('+-', repeat=len(numbers)):
        print(f'\nopt_set: {opt_set}')
            
        value = 0
        for o,n in zip(opt_set, numbers):
            if o == '+': value += n
            else: value -= n
            print(value, end=' ')
        print(f'\nvalue: {value}')
        
        results.append(value)
        print(f'results: {results}')
    
    # results 중 target 수 return
    return results.count(target)

# solution([1,1,1,1,1], 3)
solution([4,1,2,1], 4)
