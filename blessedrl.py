from player import Player
from blessed import Terminal
import os

cmd = 'mode 50,80'
os.system(cmd)


term = Terminal()


running = True

player = Player(term.width // 2, term.height // 2)

with term.cbreak(), term.hidden_cursor():

    inp = None
    while running:

      # draw player
      print(term.move_xy(player.x, player.y) +
            f"{term.gold}{player.glyph}{term.normal}")

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
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)
          case 'd':
            player.x += 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)
          case 's':
            player.y += 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)
          case 'w':
            player.y -= 1
            # print(term.move_down(2) + 'You pressed ' + term.bold("a"))
            print(term.home + term.clear)

print(f"{term.width=} {term.height=}")
