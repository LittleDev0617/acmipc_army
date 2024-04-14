N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_shop = []


def house_chicken(h, cs):
  return abs(h[0] - cs[0]) + abs(h[1] - cs[1])


for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      house.append((i, j))
    elif city[i][j] == 2:
      chicken_shop.append((i, j))

dt = [[-1] * 13 for _ in range(len(house))]

for i, h in enumerate(house):
  for j, cs in enumerate(chicken_shop):
    dt[i][j] = house_chicken(h, cs)


def city_chicken(chicken_shop_index, limit):
  score = 0
  #print(chicken_shop_index)
  for i, h in enumerate(house):
    score += min(dt[i][j] for j in chicken_shop_index)
    if score >= limit:
      return 99999
  return score


visit_index = []
combinations = []
min_score = 99999


def dfs(depth, begin):
  global min_score
  if depth == M:
    combinations.append(visit_index)
    #print(visit_index)
    min_score = min(min_score, city_chicken(visit_index, min_score))
    return

  for i in range(begin, len(chicken_shop)):
    if i in visit_index:
      continue
    visit_index.append(i)
    dfs(depth + 1, i + 1)
    visit_index.pop()


dfs(0, 0)
print(min_score)
