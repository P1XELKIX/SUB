"""
God forbid i set myself an easy project :/
Basically the story is that of iron lung

"""

#IMPORTS
import time, random

def Print(words):
    letters = list(words)

    for letter in letters:
        print (letter, end="", flush=True)
        time.sleep(0.08)


def fastPrint(words):
    letters = list(words)

    for letter in letters:
        print (letter, end="", flush=True)
        time.sleep(0.015)

class Player:
    def __init__(
        self, location, direction, speed, objectives_scanned, hull_damage
    ):
        self.location = location
        self.direction = direction
        self.speed = speed
        self.objectives_scanned = objectives_scanned
        self.hull_damage = hull_damage


class Objective:

    def __init__(
            self, objective_num, location_bottom_left, location_top_right, 
            direction, image_description
            ):
        self.objective_num = objective_num
        self.location_bottom_left = location_bottom_left
        self.location_top_right = location_top_right
        self.direction = direction
        self.image_description = image_description
    
    def scanned(self):
        fastPrint(
                  f"The screen loads slowly, and in black and white it "
                  f"displays {self.image_description} "
                  )


player = Player((150,90), 0, 0, 0)

possible_moves = ["Help", "Move", "Turn", "Scan", "Compass", "Map", "Fix"]

dev = input("")

if dev == "dev":
    intro = False
else:
    intro = True


first_objective = Objective(1, (325, 185), (000, 000), "SE", "a fish with 2 eyes")

Objective.scanned(first_objective)


if intro:
    Print("Welcome To SUSTAINED PRESSURE")

    fastPrint(
    '\n\nIn a future where humanity has colonized space, an event known as '
    '"The Quiet Rapture" causes all stars and habitable planets in the '
    'universe to inexplicably disappear, leaving only individuals aboard '
    'space stations or starships alive.'
    )

    fastPrint(
    '\n\nTo secure the survival of humanity, an expedition is launched an '
    'expedition to AT-5, a desolate moon that has recently formed an '
    'expansive ocean of human blood, believed to hold vital resources '
    'desperately required to sustain human life'
    )

    fastPrint(
    '\n\nYou are a convict sent to navigate the trenches of the blood ocean '
    'in a small submarine known officially as XDDCC, nicknamed the '
    '"STEEL Lung", to verify the existence of the resources'
    )

    fastPrint(
    '\n\nDue to the pressure and depth of the ocean, the main hatch is '
    'welded shut, the forward viewport has been encased in metal, and '
    'communications are lost shortly after submerging'
    )

    fastPrint(
    '\n\nYou are promised freedom your upon your return to the surface, but '
    'a note left by a previous occupant of the submarine warns you otherwise.'
    )

    Print("\n\nWould you like a tutorial? [Y/n]")

    ans = input("\n").strip().lower()

    if  ans == "n":
        tutorial = False

    elif ans == "y":
        tutorial = True

    else:
        Print("err: assuming you want tutorial")
        tutorial = True

    if tutorial:
        Print("\n||Tutorial||")
        fastPrint(
            "\n\nYou spawn in at coordinates 150,90 facing north and have to "
            "scan various objectives to complete the game."
            )
        fastPrint(
            "\nThe game is played via various inputs you type in if you input "
            "'help' it will display all the avaliable inputs that can be made."
            )
        fastPrint("\nfor example if you input 'scan':")
        Print("\nscan location")
        fastPrint("\nyou scan your current location on the submarine terminal")
        fastPrint(f"\n\nLOCATION: {player.location}")