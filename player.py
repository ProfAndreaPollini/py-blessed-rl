from dataclasses import dataclass


@dataclass
class Player:
  x: int
  y: int
  glyph: str = "@"
  health: int = 100
