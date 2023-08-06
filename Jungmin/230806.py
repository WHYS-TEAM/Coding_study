def solution(n, words):
    unique_word = set()
    for idx in range(len(words)):
        player_num = (idx % n) + 1
        specific_turn = (idx // n) + 1
        if len(words[idx]) > 1 and words[idx] not in unique_word:
            if idx == 0:
                unique_word.add(words[idx])
            elif words[idx - 1][-1] == words[idx][0]:
                unique_word.add(words[idx])
            else:
                return [player_num, specific_turn]
        else:
            return [player_num, specific_turn]
    return [0, 0]