# advent-of-code-2024
My work on the [Advent of Code 2024](https://adventofcode.com/2024) challenge. In addition to doing them in my language of choice (usually Python, since I've been trying to practice it more), I've also done rewrites of a few of my solutions in Haskell, _q.v._ `aoc2024.hs`.

## Languages used for each day, number of stars earned, date completed, and personal comments
1. **Python** (⭐⭐) — Dec 22, 2024
    * Being Day 1, this puzzle was quite easy. I definitely could've done it more functionally if I had taken the time to... but the C programmer in me can't help but love procedural methods.
2. **Python** (⭐⭐) —  Dec 22, 2024
    * Quite straightfoward, little to no issue. I'm sure there's a cleverer way that I could've dealt with the `is_decreasing` and `is_increasing` at the same time... but there's hardly any harm in the way that I did it.
3. **Python** (⭐⭐) — Dec 22, 2024
    * As soon as I looked at this problem, I knew that regex would be my best friend. Thankfully, Python provides the nice `re` library for all my regex needs.
    * I also have found myself wanting to have an `sscanf` like in C... And apparently there are some in the same `re` library in the form of `re.search` and `re.parse`. I'll be sure to make judicious use of them going forward.
4. **Python** (⭐⭐) — Dec 22, 2024
    * The `numpy` library was king for this exercise. Not only could I easily flip and transpose the 2D array, but I could also use the methods:
      * `.argwhere` to find indices of all array elements equal to `'A'`
      * `.diag` to get all of the diagonals
    * This was the first day where I saw Part 2 and thought "Dang" since it wasn't as extendable from Part 1 as I'd hoped. Certainly a nice exercise in mini-optimizations like knowing that every X-MAS has `A` in the middle, and that `A`s around the edges can be ignored.
5. **Python** (⭐⭐) — Dec 23, 2024
    * Originally, I tried to solve this by creating a `dict` of all elements and recursively find all elements that could potentially follow them... but then I realized that I was wayyyy overthinking things, and I could just look up the rules in linear time (at least with this small number of rules) rather than overengineer a recursive solution.
    * Fortunately for me on Part 2, the way that I checked the ordering for a "page update" was extremely amenable to implementing BubbleSort by essentially changing just one line, letting me solve it very easily.
6. **Python** (⭐⭐) — Dec 23, 2024
    * The performance on Part 2 is lackluster, taking several minutes to complete. Nevertheless, it finds the right answer in a humanly-reasonable amount of time.
7. **Python** (⭐⭐) — Dec 23, 2024
    * I was actually quite surprised how well my Part 1 solution could be extended to accomodate Part 2--I merely had to add a third operator and what it did, and everything else worked the same!
8. **Python** (⭐⭐) — Dec 24, 2024
    * The fact that Python supports sets was wonderful for this problem. The only minor headache I encountered was having to convert between `numpy.ndarray`s and `tuple`s... but that's hardly a real issue.
    * I'm also not entirely convinced that I should've used a `dict` where I did in this problem... but it does work, so I ain't complaining.
