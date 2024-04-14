import sys

sys.setrecursionlimit(10**6)
T = int(input())


def sol():
  n = int(input())
  students = [int(x) - 1 for x in input().split()]
  visit = [False] * n

  cnt = n
  tmp = []
  indexes = {}

  def dfs(start, s, index):
    nonlocal cnt
    #print(visit)
    if visit[s]:
      return

    if s == start:
      #print('**', tmp)
      cnt -= len(tmp)
      visit[s] = True
      return
    elif s in tmp:
      i = indexes[s] + 1
      cnt -= len(tmp) - i
      visit[s] = True
      #print(tmp, i)
      return

    tmp.append(s)
    indexes[s] = index
    dfs(start, students[s], index + 1)
    visit[s] = True

  for s in range(n):
    if not visit[s]:
      tmp.append(s)
      dfs(s, students[s], 0)
      visit[s] = True
      tmp = []
  return cnt


for _ in range(T):
  print(sol())
