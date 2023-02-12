from dataclasses import dataclass


@dataclass
class Potion:
  x: int
  y: int
  health: int
  glyph: str


@dataclass
class Orb:
  x: int
  y: int
  health: int
  glyph: str
