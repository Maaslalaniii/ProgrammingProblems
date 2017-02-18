function riceball(N, r) {

  let numberOfPossibleCombinations = getNumberOfPossibleCombinations(N, r)

  // Check for zero combination possibilities
  if (numberOfPossibleCombinations == 0) return r

  // Start combining riceballs.
  let riceballs = []

  for (let i = 0; i < numberOfPossibleCombinations; i++) {

    // Create a new possibility branch, for later comparison
    riceballs.push([])

    let combinations = 0
    let combined = false
    let skip = i

    for (let j = 0; j < N; j++) {
      
      // Check adjacent riceballs
      if (r[j] == r[j+1] && !combined) {
        if (++combinations > skip) {
          riceballs[i].push(r[j] + r[j++])
          combined = true
        } else riceballs[i].push(r[j])
      }

      // Check riceballs seperated by exactly one riceball
      else if (r[j] == r[j+2] && !combined) {
        if (++combinations > skip) {
          riceballs[i].push(r[j] + r[j+1] + r[j+2])
          combined = true
          j = j + 2
        } else riceballs[i].push(r[j])
      }

      // Riceball cannot combine on this iteration.
      else riceballs[i].push(r[j])
  
    }
  }

  // For each possibility, continue combining riceballs, in a tree-like manner.
  for (let i = 0; i < riceballs.length; i++) {
    riceballs[i] = riceball(riceballs[i].length, riceballs[i])
  }

  return riceballs

}


function getNumberOfPossibleCombinations(N, r) {
  let numberOfPossibleCombinations = 0

  // Check each riceball to see if it has an equal sized riceball zero or one riceballs away. 
  for (let i = 0; i < N; i++) {
    if (r[i] == r[i+1]) numberOfPossibleCombinations++
    if (r[i] == r[i+2]) numberOfPossibleCombinations++
  }
  
  return numberOfPossibleCombinations
  
}


function flatten(array) {
  return [].concat.apply([], array.map(element => Array.isArray(element) ? flatten(element) : element))
}


function findLargestRiceball(N, r) {
  return Math.max(...flatten(riceball(N, r)))
}

module.exports = findLargestRiceball