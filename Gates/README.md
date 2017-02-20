# Gates

### Problem Description
For your birthday, you were given an airport. The airport has _G_ gates, numbered from 1 to _G_. _P_ planes arrive at the airport, one after another. You are to assign the ith plane to permanently dock at any gate 1, . . . , _gi_ (1 ≤ _gi_ ≤ _G_), at which no previous plane has docked. As soon as a plane cannot dock at any gate, the airport is shut down and no future planes are allowed to arrive. In order to keep the person who gave you the airport happy, you would like to maximize the number of planes starting from the beginning that can all dock at different gates. 

### Input Specification
The first line of input contains _G_ (1 ≤ _G_ ≤ 105), the number of gates at the airport.
The second line of input contains _P_ (1 ≤ _P_ ≤ 105), the number of planes which will land.
The next _P_ lines contain one integer gi (1 ≤ _gi_ ≤ G), such that the _i_ th plane must dock at some
gate from 1 to _gi_, inclusive.
Note that for at least 40% of the marks for this question, _P_ ≤ 2000 and _G_ ≤ 2000.

### Output Specification
Output the maximum number of planes that can land starting from the beginning.
