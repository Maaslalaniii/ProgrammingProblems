def sum_game(K, swifts, semaphores):
  swifts_sum = 0
  semaphores_sum = 0
  games_equal = 0

  for i in range(K):
    swifts_sum += swifts[i]
    semaphores_sum += semaphores[i]
    if swifts_sum == semaphores_sum:
      games_equal = i + 1

  print(games_equal)

K = int(input())
swifts = [int(x) for x in input().split()]
semaphores = [int(x) for x in input().split()]

sum_game(K, swifts, semaphores)