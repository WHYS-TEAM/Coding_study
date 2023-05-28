def solution(n, computers):
  
  ''''Computer node들을 iter하면서
  edge로 연결된 모든 다른 computer를 방문하면
  network_num을 +1하는 로직
  
  que: 연결되어 있어서 앞으로 방문 할 노드
  visited: 방문한 노드'''
  
  network_num, que, visited = 0, [], []

  for node in range(n):
      print()
      print(f'[ node: {node} ]')
      if node not in visited:
          que.append(node)

          while que:
              print()
              curr = que.pop(0)
              print('Q', que, 'V', visited, 'Com', computers[curr])
              visited.append(curr)
              for idx, edge in enumerate(computers[curr]):
                  print(f'curr:{curr}, idx:{idx}, edge:{edge}, que:{que}, visited:{visited}')
                  if idx != curr and idx not in visited and edge:
                      que.append(idx)
                      print('que update', que)
          network_num += 1
          print('network_num', network_num)
          
return network_num
