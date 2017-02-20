def ragaman(a, b):
  a = list(a)
  b = list(b)

  # Check each letter to find a match with the potential anagram
  for i in reversed(range(len(a))):
    for j in reversed(range(len(b))):
      if a[i] == b[j]:
        a.pop(i)
        b.pop(j)
        break

  # Account for asterisks
  for i in reversed(range(len(b))):
    if b[i] == '*':
      b.pop(i) # Take away that asterisk
      a.pop()  # Take away a random letter to match that asterisk

  # There should be no more duplicate letters nor asterisks left
  # If the two arrays are not empty that means they were not wildcard anagrams
  print('A') if len(a) == 0 and len(b) == 0 else print('N')
