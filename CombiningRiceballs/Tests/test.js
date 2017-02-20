// Import solution and testing library
const assert = require('assert')
const combiningRiceballs = require('../riceballs.js')

// Test 1: N = 4
assert.equal(combiningRiceballs(4, [2, 3, 2, 3]), 8)

// Test 2: N = 5
assert.equal(combiningRiceballs(5, [7, 4, 7, 18, 36]), 72)

// Test 3: N = 6
assert.equal(combiningRiceballs(6, [8, 4, 3, 4, 11, 8]), 38)

// Test 4: N = 7
assert.equal(combiningRiceballs(7, [47, 12, 12, 3, 9, 9, 3]), 48)

// Test 5: N = 8
assert.equal(combiningRiceballs(8, [5, 2, 3, 2, 3, 2, 5, 8]), 22)