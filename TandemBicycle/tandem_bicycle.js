function tandem(Q, N, D, P) {

  // Lists of the pairs on each tandem bicycle
  let bicycles = []

  for (let i = 0; i < N; i++) {

    // Depending on the question, pair the fastest speed from Dmojistan
    // with the fastest or slowest speed from Pegland.
    let d = Math.max(...D)
    let p = Q == 1 ? Math.max(...P) : Math.min(...P)

    // Remove the two from the unpaired lists, to avoid reselection
    D.splice(D.indexOf(d), 1)
    P.splice(P.indexOf(p), 1)

    // Add the pair to a tandem bicycle
    bicycles.push([d, p])

  }

  // Finds total speed by adding the speeds of all the bicycles. 
  return bicycles.reduce((sum, pair) => sum + Math.max(pair[0], pair[1]), 0)

}