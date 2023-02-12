
from dataclasses import dataclass


@dataclass
class Wall:
  x: int
  y: int
  glyph: str = "#"
  walkable: bool = False

  def __post_init__(self):
    self.walkable = False
    self.glyph = "#"
