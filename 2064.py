n = int(input())
MASK = 0xFF_FF_FF_FF
NETWORK_IP = 0xFF_FF_FF_FF
TMP_NETWORK_IP = 0
XOR_NETWORK_IP = 0

for _ in range(n):
  _ip = input().split('.')
  ip = 0
  for j in reversed(range(4)):
    ip |= int(_ip[3 - j]) << (8 * j)
  NETWORK_IP &= ip
  XOR_NETWORK_IP ^= ip
  TMP_NETWORK_IP |= ip

# print(f'{NETWORK_IP:032b}')
# print(f'{TMP_NETWORK_IP:032b}')

for i in range(32):
  if f'{NETWORK_IP:032b}'[i] != f'{TMP_NETWORK_IP:032b}'[i]:
    MASK = int('1' * i + '0' * (32 - i), 2)
    break

NETWORK_IP &= MASK

S_NETWORK_IP = []
S_TMP_NETWORK_IP = []
S_MASK = []

for i in reversed(range(4)):
  S_NETWORK_IP.append(str((NETWORK_IP >> (8 * i)) & 0xFF))
  S_TMP_NETWORK_IP.append(str((TMP_NETWORK_IP >> (8 * i)) & 0xFF))
  S_MASK.append(str((MASK >> (8 * i)) & 0xFF))

print('.'.join(S_NETWORK_IP))
# print('.'.join(S_TMP_NETWORK_IP))
print('.'.join(S_MASK))
