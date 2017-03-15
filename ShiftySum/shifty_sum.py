def shifty_sum(N, k):
  shifted_numbers = [N]

  for i in range(k):
    shifted_numbers.append(shifted_numbers[i] * 10)

  print(sum(shifted_numbers))

shifty_sum(int(input()), int(input()))