# Tandem Bicycle

### Problem Description
Since time immemorial, the citizens of Dmojistan and Pegland have been at war. Now, they have finally signed a truce. They have decided to participate in a tandem bicycle ride to celebrate the truce. There are _N_ citizens from each country. They must be assigned to pairs so that each pair contains one person from Dmojistan and one person from Pegland.

Each citizen has a cycling speed. In a pair, the fastest person will always operate the tandem while the slower person simply enjoys the ride. In other words, if the members of a pair have speeds _a_ and _b_, then the _bike speed_ of the pair is _max(a, b)_. The _total speed_ is the sum of the _N_ individual _bike speeds_.


For this problem, in each test case, you will be asked to answer one of the two questions:

 * Question 1: what is the _minimum_ total speed, out of all possible assignments into pairs?
 * Question 2: what is the _maximum_ total speed, out of all possible assignments into pairs?

### Input Specification
The first parameter will contain the type of question you are to solve, which is either 1 or 2.

The second parameter contains _N_.

The third parameter contains an array of length _N_: the speeds of the citizens of Dmojistan.

The fourth parameter contains an array of length _N_: the speeds of the citizens of Pegland.

### Output Specification
Output the maximum or minimum total speed that answers the question asked.