"""
God forbid i set myself an easy project :/
Basically the story is that of iron lung

"""

#IMPORTS
import time

class Objective:

    def __init__(self, objective_num, location, direction)


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


dev = input("")


if dev == "dev":
    intro = False
else:
    intro = True

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

    while tutorial:
        pass


