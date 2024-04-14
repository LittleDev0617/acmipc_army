N = int(input())
data = [input().split() for _ in range(N)]
dp = [[] for _ in range(N)]

dp[0] = [data[0][0]]

for i in range(1, N):
  for j in range(len(data[i])):
    if j == 0:
      dp[i] = [data[i][j] + dp[i - 1][0]]
      continue
    elif j == len(data[i]) - 1:
      dp[i].append(data[i][j] + dp[i - 1][-1])
      continue

    dp[i].append(max(dp[i - 1][j - 1], dp[i - 1][j]) + data[i][j])

  # print(dp[i])

print(max(dp[N - 1]))
