def zero(N, a):

  # Current stack of numbers
  current_numbers = []  

  # Add all the numbers from the given array, while adjusting when a zero appears
  for i in range(N):
    # Zero! Remove the last number. 
    if a[i] == 0: current_numbers.pop()
    # Non-zero! Add the number to the stack.
    else: current_numbers.append(a[i])

  return sum(current_numbers)

