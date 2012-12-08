case class Coordinate(x: Int, y: Int) {
  def isInBound(size: Int): Boolean = {
    ((x >= 0) && (x < size) && (y >= 0) && (y < size))
  }
}

case class State(state: Boolean=true)

case class Grid(width: Int, height: Int) {
  
  var cells = Array.ofDim[State](2, 2)
  for (i <- 0 to (cells.length-1))
    for (j <- 0 to (cells(i).length-1))
      cells(i)(j) = State()

  def getAliveNeighbourNumber(i: Int, j: Int): Int = {
    getNeighbours(i, j).count(x => x.isInBound(width))
  }

  def getNeighbours(i: Int, j: Int): List[Coordinate] = {
    var result: List[Coordinate] = List()

    for (y <- j-1 to j+1)
      result = Coordinate(i-1, y) :: result

    for (y <- j-1 to j+1)
      result = Coordinate(i+1, y) :: result
    
    result = Coordinate(i,j-1) :: result
    result = Coordinate(i, j+1) :: result

    result
  }

}

def main() = {
  println("hello retreat") 
  val g = Grid(3, 3)
  val coord = Coordinate(0, -1)
  println(coord.isInBound(2)) 
}


