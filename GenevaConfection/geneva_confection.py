def sort_carts(c):
  mountain = c
  branch = []
  lake = []
  current = 1

  # For every cart decide whether it should go to the lake or the branch.
  for cart in reversed(mountain):
    mountain.pop()

    # Place the cart in the branch or lake
    if cart == current:
      lake.append(cart)
      current += 1
    else: branch.append(cart)

    # Check if the carts from the branch can go to the lake 
    for cart in reversed(branch):
      if cart == current:
        branch.pop()
        lake.append(cart)
        current += 1
      else: break

  # If the branch is empty we can complete the recipe.
  print('Y') if len(branch) == 0 else print('N')


def geneva(file):
  # Read the file input
  with open(file, 'r') as f:
    data = [int(i) for i in f.readline().split()]
    
  cases = []
  current = 1

  # Arrange the data in a 2 dimensional array
  for i in range(data[0]):
    cases.append([])
    current += 1
    for j in range(data[current - 1]):
      cases[i].append(data[current])
      current += 1
    # Solve the the problem for each test.
    sort_carts(cases[i])


# Test by calling geneva(file)
# Example: geneva('s3.5.in')