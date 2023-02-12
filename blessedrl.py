from typing import List
from random import randint

from player import Player
from blessed import Terminal
from wall import Wall


term = Terminal()


running = True

player = Player(term.width // 2, term.height // 2)
walls: List[Wall] = []
for _ in range(10):
  walls.append(Wall(randint(1, term.width - 1), randint(1, term.height-1)))

with term.cbreak(), term.hidden_cursor():

    inp = None
    while running:

      # draw player
      print(term.move_xy(player.x, player.y) +
            f"{term.gold}{player.glyph}{term.normal}")

      for wall in walls:
        print(term.move_xy(wall.x, wall.y) +
              f"{term.green}{wall.glyph}{term.normal}")

      print(term.move_xy(2, term.height - 2), f"{player.x=} {player.y}")

      inp = term.inkey()
      if inp.is_sequence:
        keycode = inp.code
        match keycode:
          case term.KEY_ESCAPE:
            running = False
      else:
        match inp:
          case 'a':
            player.x -= 1
            if player.x < 0:
              player.x = 0

            for wall in walls:
              if wall.x == player.x and wall.y == player.y:
                player.x += 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)
          case 'd':
            player.x += 1
            if player.x >= term.width:
              player.x = term.width

            for wall in walls:
              if wall.x == player.x and wall.y == player.y:
                player.x -= 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)
          case 's':
            player.y += 1
            if player.y >= term.height:
              player.y = term.height
            for wall in walls:
              if wall.x == player.x and wall.y == player.y:
                player.y -= 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)
          case 'w':
            player.y -= 1
            if player.y <= 0:
              player.y = 0

            for wall in walls:
              if wall.x == player.x and wall.y == player.y:
                player.y += 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)

print(f"{term.width=} {term.height=}")
