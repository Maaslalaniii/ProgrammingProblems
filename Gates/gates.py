def gates(G, P, g):
  # Representation of gates.
  gates = [False for i in range(G)]
  # Number of planes landed.
  planes = 0

  for plane in g:
    stop = True
    # Place the plane in the highest gate number possible.
    for i in reversed(range(plane)):
      if not gates[i]:
        gates[i] = True
        planes += 1
        stop = False
        break
    # The plane could not find a valid gate in which to land.
    if stop:
      return planes



print(gates(4, 6, [2, 2, 3, 3, 4, 4]))
print(gates(4, 3, [4, 1, 1]))