from collections import deque

T = int(input())


def sol():
  h, w = (int(x) + 2 for x in input().split())
  MAP = [['.'] * w] + ([list('.' + input() + '.')
                        for _ in range(h - 2)]) + [['.'] * w]
  keys = input()
  keys = set() if keys == '0' else set(list(keys))
  keys.add('$')
  keys.add('.')

  #[print(''.join(row)) for row in MAP]
  #print(keys)

  def bfs(start):
    q = deque([start])
    visit = [[False] * w for _ in range(h)]
    visit[start[1]][start[0]] = True

    key_cnt = 0
    while q:
      p = q.popleft()

      for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
        nx, ny = dx + p[0], dy + p[1]
        if 0 <= nx < w and 0 <= ny < h and \
            (cell := MAP[ny][nx]) != '*' and not visit[ny][nx]:
          if cell == '$':
            key_cnt += 1

          if cell.islower():
            visit = [[False] * w for _ in range(h)]
            MAP[ny][nx] = '.'
            visit[ny][nx] = True
            keys.add(cell)

          if cell.lower() in keys:
            if cell.isupper() or cell == '$':
              #print(ny, nx, cell)
              #[print(''.join(row)) for row in MAP]
              MAP[ny][nx] = '.'
            visit[ny][nx] = True
            q.append((nx, ny))

    return key_cnt

  res = bfs((0, 0))
  print(res)


for _ in range(T):
  sol()
