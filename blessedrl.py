from typing import List
from random import randint

from player import Player
from blessed import Terminal
from wall import Wall
from potion import Potion,Orb


term = Terminal()


running = True

player = Player(term.width // 2, term.height // 2)
walls: List[Wall] = []
for _ in range(10):
    walls.append(Wall(randint(1, term.width - 1), randint(1, term.height-1)))

potions: List[Potion] = []
orbs: List[Orb] = []
for _ in range(10):
    orbs.append(Orb(randint(1, term.width - 1), randint(1, term.height-1),-5,"O"))


while len(potions) < 5:
    pos = randint(1, term.width - 1), randint(1, term.height-1)
    occupied = False
    for wall in walls:
        if wall.x == pos[0] and wall.y == pos[1]:
            occupied = True
            break
    if not occupied:
        health = randint(1, 10)
        potions.append(Potion(pos[0], pos[1], health,
                       "P"))



with term.cbreak(), term.hidden_cursor():

    inp = None
    while running:

        # draw player
        print(term.move_xy(player.x, player.y) +
              f"{term.gold}{player.glyph}{term.normal}")

        for wall in walls:
            print(term.move_xy(wall.x, wall.y) +
                  f"{term.green}{wall.glyph}{term.normal}")

        for potion in potions:
            print(term.move_xy(potion.x, potion.y) +
                  f"{term.orangered}{potion.glyph}{term.normal}")

        for orb in orbs:
            print(term.move_xy(orb.x, orb.y) +
                  f"{term.cyan}{orb.glyph}{term.normal}")

        print(term.move_xy(2, term.height - 2),
              f"{player.x=} {player.y} {player.health=} potions={len(potions)}")

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
        for i in range(len(potions)):
            potion = potions[i]
            if potion.x == player.x and potion.y == player.y:
                player.health += potion.health
                potions.remove(potion)
                break
        
        # update orbs
        for orb in orbs:
          dx = randint(-1, 1)
          dy = randint(-1, 1)
          x = max(min(orb.x + dx,term.width),0)
          y = max(min(orb.y + dy,term.height),0)
          orb.x = x
          orb.y = y
          if orb.x == player.x and orb.y == player.y:
            player.health += orb.health

print(f"{term.width=} {term.height=} ")
