# Combining Riceballs

### Problem Description

Alphonse has _N_ rice balls of various sizes in a row. He wants to form the largest rice ball possible for his friend to eat. Alphonse can perform the following operations:

* If two *adjacent* rice balls have the same size, Alphonse can combine them to make a new rice ball. The new rice ball’s size is the sum of the two old rice balls’ sizes. It occupies the position in the row previously occupied by the two old rice balls.

* If two rice balls have the same size, and there is *exactly one rice ball between them*, Alphonse can combine all three rice balls to make a new rice ball. (The middle rice ball does not need to have the same size as the other two.) The new rice ball’s size is the sum of the three old rice balls’ sizes. It occupies the position in the row previously occupied by the three old rice balls. Alphonse can perform each operation as many times as he wants. Determine the size of the largest rice ball in the row after performing 0 or more operations.

Alphonse can perform each operation as many times as he wants.

Determine the size of the largest rice ball in the row after performing 0 or more operations.

### Input Specification

The first line will contain the integer, _N_ (1 < _N_ < 400).

The next line will contain _N_ space seperated integers representing the sizes of the riceball, order from left to right. Each integer is at least 1 and at most 1 000 000.

* For 1 of the 15 available marks, _N_ = 4.
* For an additional 2 of the 15 available marks, _N_ < 10.
* For an additional 5 of the 15 available marks, _N_ < 50.

### Output specification

Output the size of the largest riceball Alphonse can form.