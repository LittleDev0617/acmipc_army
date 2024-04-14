n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visit = []


def dfs(d, b):
  if d == m:
    print(*visit)
    return
  for i in range(b, len(num)):
    visit.append(num[i])
    dfs(d + 1, i)
    visit.pop()


dfs(0, 0)
