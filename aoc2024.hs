import Data.List (transpose, sort, foldl')

processFileTextAsInts :: String -> [[Int]]
processFileTextAsInts c = map (map read . words) $ lines c

{-  ============================================================
    DAY 1
============================================================  -}

day1solve1 :: [Int] -> [Int] -> Int
day1solve1 lefts rights = sum (zipWith (\x y -> abs (x - y)) (sort lefts) (sort rights))

day1solve2 :: [Int] -> [Int] -> Int
day1solve2 lefts rights = sum $ map (\x -> x * length (filter (x==) rights)) lefts

day1 :: IO ()
day1 = do
    fileContents <- readFile "day01input.txt"
    let lines = processFileTextAsInts fileContents
    let [lefts, rights] = transpose lines
    let answer1 = day1solve1 lefts rights
    let answer2 = day1solve2 lefts rights
    print $ "Day 1, Part 1 solution: " ++ show answer1
    print $ "Day 1, Part 2 solution: " ++ show answer2

{-  ============================================================
    DAY 2
============================================================  -}

day2solve1_isSafe :: [Int] -> Bool
day2solve1_isSafe l = case l of
    []        ->   True
    [x]       ->   True
    (x:xs)    ->   (isDecreasing || isIncreasing) && isNotSteep where
        isDecreasing = all (< 0) deltas
        isIncreasing = all (> 0) deltas
        isNotSteep   = all (\x -> abs x > 0 && abs x <= 3) deltas
        deltas       = zipWith (-) xs l

day2solve2_isDampSafe :: [Int] -> Bool
day2solve2_isDampSafe l
    | day2solve1_isSafe l                       = True
    | any day2solve1_isSafe (allRemovalsOf1 l)  = True
    | otherwise                                 = False
    where
        allRemovalsOf1 l = map (removeNth l) [0..length l - 1]
        removeNth (x:xs) n
            | n == 0        = xs
            | otherwise     = x : removeNth xs (n-1)

day2 :: IO ()
day2 = do
    fileContents <- readFile "day02input.txt"
    let lines = processFileTextAsInts fileContents
    let answer1 = length . filter id . map day2solve1_isSafe $ lines
    let answer2 = length . filter id . map day2solve2_isDampSafe $ lines
    print $ "Day 2, Part 1 solution: " ++ show answer1
    print $ "Day 2, Part 2 solution: " ++ show answer2

{-  ============================================================
    DO ALL SOLUTIONS
============================================================  -}

main :: IO ()
main = do
    day1
    day2