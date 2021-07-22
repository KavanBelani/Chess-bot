class Board():
  def __init__(self):
    pieces = []
    for x in range(8):
      pieces.append(Pawn(x, 2))
    for x in range(8):
      pieces.append(Pawn(x, 6))
    
    self.pieces = pieces

class BasePiece():
  moves = []
  def __init__(self, x, y, team):
    self.x = x
    self.y = y
    self.team = team
  
class Pawn(BasePiece):
  moves = [(0, 1)]