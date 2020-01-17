# 6.2 조건부 확률
import random

def random_kid():
  return random.choice(["boy","girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
  younger = random_kid()
  older = random_kid()
  if older == "girl":
    older_girl += 1
  if older == "girl" and younger == "girl":
    both_girls += 1
  if older == "girl" or younger == "girl":
    either_girl += 1

# 첫째가 딸일 경우, 둘 다 딸일 확률
print("P( both | older ) : ", both_girls/older_girl)

# older: girl
# younger : girl or boy -> 1/2

# 최소 한 명이 딸일 경우, 둘 다 딸일 확률
print("P( both | either ) : ", both_girls/either_girl)

# P(b|g) = P(b,g)/P(g) = P(b)/P(g)
# = (1/4) / (3/4)
# = 1/3

# P( both | older ) :  0.5007089325501317 -> 1/2
# P( both | either ) :  0.3311897106109325 -> 1/3
