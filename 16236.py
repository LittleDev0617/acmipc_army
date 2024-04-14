from collections import deque

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]


class Shark:

  def __init__(self, n: int, pos: tuple, bg):
    self.x = pos[0]
    self.y = pos[1]
    self.n = n
    self.bg = bg
    self.size = 2
    self.exp = 0

  def __str__(self) -> str:
    return '\n'.join([' '.join(map(str, row)) for row in self.bg])

  def eat_prey(self, pos: tuple):
    size = self.bg[pos[1]][pos[0]]
    if self.size <= size: return -1

    self.exp += 1
    if self.exp == self.size:
      self.size += 1
      self.exp = 0
    # print(f'{self.size=} : {self.x=}, {self.y=} -> ', end='')
    self.bg[self.y][self.x] = 0
    self.x = pos[0]
    self.y = pos[1]
    self.bg[self.y][self.x] = 0
    # print(f'{self.x=}, {self.y=}')
    return (self.x, self.y)

  def find_prey(self) -> tuple:
    q = deque()
    visit = [[False] * self.n for _ in range(self.n)]
    visit[self.y][self.x] = True

    q.append([(self.x, self.y), 0])
    preys = []
    prev = 0
    while q:
      p, distance = q.popleft()

      if prev != distance:
        if len(preys) != 0:
          preys.sort(key=lambda v: (v[1], v[0]))
          # print(preys)
          return self.eat_prey(preys[0]), distance
        else:
          prev = distance

      for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        nx, ny = dx + p[0], dy + p[1]
        if 0 <= nx < self.n and 0 <= ny < self.n and \
            not visit[ny][nx] and self.bg[ny][nx] <= self.size:
          if self.bg[ny][nx] != 0 and self.bg[ny][nx] < self.size:
            preys.append((nx, ny))
            #return self.eat_prey((nx, ny)), distance + 1

          q.append([(nx, ny), distance + 1])
          visit[ny][nx] = True

    return -1, 0


pos = ()
for i in range(N):
  for j in range(N):
    if M[i][j] == 9:
      pos = (j, i)
      break

# print()
shark = Shark(N, pos, M)
time = 0

while (res := shark.find_prey()) and res[0] != -1:
  # print(shark)
  time += res[1]
  # input()

print(time)
