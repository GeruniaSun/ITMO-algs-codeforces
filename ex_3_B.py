def find_winner(moves: list[str]) -> str:
    names = list(set([s.split()[0] for s in moves]))
    scores = {name: {'score': 0, 'move': -1} for name in names}
    final_scores = {}

    for move in moves:
        name, score = move.split()
        score = int(score)
        final_scores[name] = final_scores.get(name, 0) + score

    max_score = max(final_scores.values())

    for i, move in enumerate(moves):
        name, score = move.split()
        scores[name]['score'] += int(score)

        if int(scores[name]['score']) >= max_score and scores[name]['move'] == -1:
            scores[name]['move'] = i

    return sorted(scores.items(), key=lambda x: (-x[1]['score'], x[1]['move']))[0][0]


def main():
    n = int(input())
    game_log = [input() for _ in range(n)]
    print(find_winner(game_log))


if __name__ == '__main__':
    main()
