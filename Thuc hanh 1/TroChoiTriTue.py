def solve_game(N, M, K, teams):
    dp = [-1] * M

    def can_win(C):
        if C >= M:
            return 0
        if dp[C] != -1:
            return dp[C]

        for x in range(1, K + 1):
            if C + x >= M or can_win(C + x) == 0:
                dp[C] = 1
                return 1
        dp[C] = 0
        return 0

    result = []
    for start in range(N):
        dp = [-1] * M
        if can_win(0):
            result.append(str(teams[start]))
        else:
            result.append(str(1 - teams[start]))
    return "".join(result)


N, M, K = map(int, input().split())
teams = list(map(int, input().split()))

print(solve_game(N, M, K, teams))
