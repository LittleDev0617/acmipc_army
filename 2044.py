H, W = map(int, input().split())
screenshot = [list(input()) for _ in range(H)]


class Vector2D:

  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  def __add__(self, vec):
    return self.__class__(self.x + vec.x, self.y + vec.y)

  def __radd__(self, vec):
    return self.__class__(self.x + vec.x, self.y + vec.y)

  def __sub__(self, vec):
    return self.__class__(self.x - vec.x, self.y - vec.y)

  def __rsub__(self, vec):
    return self.__class__(vec.x - self.x, vec.y - self.y)

  def __iter__(self):
    yield self.x
    yield self.y

  def __str__(self) -> str:
    return f'({self. x}, {self.y})'


class Screen:

  class Window:

    def __init__(self, title: str, top_left: Vector2D, size: Vector2D):
      self.width, self.height = size
      self.size = size
      self.x, self.y = top_left
      self.top_left = top_left
      self.title = title

    def move_to(self, pos: Vector2D):
      self.top_left = pos
      self.x, self.y = pos

    def __str__(self) -> str:
      return f'Window [{self.title}]: {self.width} x {self.height}, pos:{self.top_left}'

  def __init__(self, size: Vector2D, init_screen: list[list]):
    self.width, self.height = size
    self.screen = init_screen
    self.bg_char = '.'
    self.windows = self.find_windows()

  def find_windows(self) -> list[Window]:
    windows = []

    for y in range(self.height):
      for x in range(self.width):
        if self.screen[y][x] == '+':
          width = self.screen[y][x + 1:].index('+') + 2
          height = [row[x] for row in self.screen[y + 1:]].index('+') + 2
          title = ''.join(self.screen[y][x:x + width]).split('|')[1]

          top_left = Vector2D(x, y)
          size = Vector2D(width, height)

          windows.append(Screen.Window(title, top_left, size))
          # print(windows[-1])
          self.erase_window(windows[-1])
          # print(self)
    return windows

  def erase_rectangle(self, top_left: Vector2D, size: Vector2D):
    self.fill_rectangle(self.bg_char, top_left, size)

  def erase_window(self, window: Window):
    self.erase_rectangle(window.top_left, window.size)

  def fill_rectangle(self, c: str, top_left: Vector2D, size: Vector2D):
    c = c[0] if len(c) > 1 else c
    x, y = top_left
    w, h = size

    for i in range(h):
      for j in range(w):
        if 0 <= i + y < self.height and 0 <= j + x < self.width:
          self.screen[i + y][j + x] = c

  def draw_window(self, window: Window):
    x, y = window.top_left
    w, h = window.size

    tmp = w - 4 - len(window.title)
    top = '+' + '-' * (tmp // 2) + '|' + window.title + '|' + '-' * (
        tmp // 2 + tmp % 2) + '+'
    for i in range(1, h - 1):
      self.screen[y + i][x] = '|'
      self.screen[y + i][x + w - 1] = '|'
    btm = '+' + '-' * (w - 2) + '+'

    self.screen[y][x:x + w] = top
    self.screen[y + h - 1][x:x + w] = btm

    self.erase_rectangle(window.top_left + Vector2D(1, 1),
                         window.size - Vector2D(2, 2))

  def cascade_mode(self):
    self.erase_rectangle(Vector2D(0, 0), Vector2D(self.width, self.height))
    windows = sorted(self.windows, key=lambda w: w.title)

    for i, window in enumerate(windows):
      window.move_to(Vector2D(i, i))
      self.draw_window(window)

  def __str__(self) -> str:
    return '\n'.join(''.join(row) for row in self.screen)


screen = Screen(Vector2D(W, H), screenshot)
screen.cascade_mode()
print(screen)
