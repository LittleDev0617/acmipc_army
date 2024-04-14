tree = {}

n = int(input())
for _ in range(n):
  a, b, c = input().split()
  tree[a] = [b, c]

result = [[], [], []]


def dfs(node):
  left, right = tree[node]

  result[0].append(node)
  if left != '.':
    dfs(left)
  result[1].append(node)
  if right != '.':
    dfs(right)
  result[2].append(node)


dfs('A')
# print(result)
[print(''.join(res)) for res in result]
