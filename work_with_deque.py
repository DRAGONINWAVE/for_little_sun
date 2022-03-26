from collections import deque
dp = deque(range(10),maxlen=10)
print(dp)
dp.rotate(3)
print(dp)
dp.appendleft(-1)
print(dp)
dp.extend([12,13,14])
print(dp)