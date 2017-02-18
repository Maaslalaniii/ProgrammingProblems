def tandem(Q, N, D, P):

  # Lists of the pairs on each tandem bicycle
  bicycles = []

  for i in range(0, N):
    
    # Depending on the question, pair the fastest speed from Dmojistan
    # with the fastest or slowest speed from Pegland.
    d = max(D)
    p = min(P) if Q == 1 else max(P)

    # Remove the two from the unpaired lists, to avoid reselection.
    D.remove(d)
    P.remove(p)

    # Add the pair to a tandem bicycle.
    bicycles.append([d, p])

  # Finds total speed by adding the speeds of all the bicycles. 
  total_speed = 0
  for bicycle in bicycles:
    total_speed = total_speed + max(bicycle)

  return total_speed