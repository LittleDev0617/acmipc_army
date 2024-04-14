n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visit = []


def dfs(d):
  if d == m:
    print(*[num[i] for i in visit])
    return

  tmp = []
  for i in range(len(num)):
    if num[i] in tmp or i in visit:
      continue
    visit.append(i)
    tmp.append(num[i])
    dfs(d + 1)
    visit.pop()


dfs(0)
