module Life where

type Cell = Bool

type Board = [[Cell]]

type Coord = (Int, Int)

empty_board:: Int -> Board
empty_board 0 = [[]]
empty_board dim = [[False | x <- [1..dim]] | x <- [1..dim]]


get_cell:: Board -> Coord -> Cell
get_cell board coord = (board !! (fst coord)) !! (snd coord)

neighbour_coordinates:: Board -> Coord -> [Coord]
neighbour_coordinates board (x, y) =
  let
    upper = [(x-1, j) | j <- [y-1..y+1]]
    lower = [(x+1, j) | j <- [y-1..y+1]]
    l_r = [(x, y-1), (x, y+1)]
    tot = upper ++ lower ++ l_r
  in filter_coordinates (length board) tot

count_active_neighbours:: Board -> Coord -> Int
count_active_neighbours board coord =
  count_active board (neighbour_coordinates board coord)

tick_cell:: Board -> Coord -> Cell
tick_cell board coord =
  let
    cell = get_cell board coord
    num_active = count_active_neighbours board coord
  in
   if (num_active == 2)
   then
     if (cell)
     then True
     else False
   else if (num_active == 3)
        then True
        else False
   else False


count_active:: Board -> [Coord] -> Int
count_active board coords =
  let
    cells = [(c, get_cell board c) | c <- coords]
    actives = filter (\x -> snd x) cells
  in
   length actives

is_valid_coord:: Int -> Coord -> Bool
is_valid_coord size (x, y) =
  (x >= 0) && (x < size) && (y >= 0) && (y < size)

filter_coordinates:: Int -> [Coord] -> [Coord]
filter_coordinates size coords = filter is_valid_on_size coords
  where
    is_valid_on_size:: Coord -> Bool
    is_valid_on_size = is_valid_coord size


main = do
  let board = empty_board 3
  print board
  let val = get_cell board (0, 0)
  -- assert (val == False)
  print val
  let coords = [(-1, 0), (1, 1)]
  let res = filter_coordinates 2 coords
  print res
  let neighs = neighbour_coordinates board (0, 0)
  print neighs
  let act = count_active board neighs
  print act
  let horrible_one = [[False, False, False], [True, False, False], [False, False, False]]
  let act2 = count_active horrible_one neighs
  print act2
  print $ count_active_neighbours horrible_one (0, 0)