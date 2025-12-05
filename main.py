"""
God forbid i set myself an easy project :/
Basically the story is that of iron lung


"""


#IMPORTS
import time, random, threading, math






class Player:
    def __init__(
        self, location, direction, speed, objectives_scanned, hull_integrity
    ):
        self.location = location
        self.direction = direction
        self.speed = speed
        self.objectives_scanned = objectives_scanned
        self.hull_integrity = hull_integrity
       
        self.move_player = False
        self.move_input = 0
        self.stop_moving = False
        self.next_objective = Objective(1, [325, 185], 135, "a fish with 2 eyes")




    def action_input(self):
        player_input = input("\n").lower().strip()


        if player_input == "help":
            normalPrint("\nAvaliable actions: ")


            for option in player_options.action:
                fastPrint("\n" + option)
            normalPrint("")


        elif player_input == "move":
            self.stop_moving = False
            normalPrint(
                "how many seconds do you want to move at 10 meters per second"
                )
            self.move_input = int(input("\n"))
            self.move_player = True




       
        elif player_input == "turn":
            normalPrint(
                "\nwould you like to turn clockwise or anti clockwise"
                )
            turn_input = input("\n").lower().strip()
            if turn_input == "clockwise":
                normalPrint("\nhow far would you like to turn in degrees:")


                turn_clockwise = int(input("\n"))


                player.direction += turn_clockwise


            elif turn_input == "anticlockwise":
                normalPrint("\nhow far would you like to turn in degrees:")


                turn_anticlockwise = int(input("\n"))


                player.direction -= turn_anticlockwise


            while player.direction > 360:
                player.direction -= 360
            while player.direction < 0:
                player.direction += 360




        elif player_input == "scan":
            normalPrint("\nWhat would you like to scan:")


            for option in player_options.scan:
                fastPrint("\n" + option)
            normalPrint("")


            scan_input = input("\n").lower().strip()


            if scan_input == "location":
               normalPrint(f"\nLOCATION: {player.location}")


            elif scan_input == "direction":
               normalPrint(f"\nDIRECTION: {player.direction}° clockwise from North")


            elif scan_input == "damage":
               normalPrint(f"\nHULL INTEGRITY: {player.hull_integrity}%")


            elif scan_input == "objective":
                self.next_objective.check_objective(self)
                if self.next_objective.location[0] - 10 < self.location[0] \
                    < self.next_objective.location[0] + 10 and \
                    self.next_objective.location[1] - 10 < self.location[1] \
                    < self.next_objective.location[1] + 10:
                   
                    Player.next_objective.scanned()


            elif scan_input == "nextobjective":
                normalPrint(f"\nLOCATION: {player.next_objective.location_x}")




#        self.scan = ["location", "direction", "damage", "objective", "next objective"]


        elif player_input == "fix":
            pass


        elif player_input == "clock":
            fastPrint("You check your watch:")
            normalPrint(f"\nyou only have {int(oxygen_time_left // 60)} minutes & {int(oxygen_time_left % 60)} seconds of oxygen remaining.")


        elif player_input == "stop":
            self.stop_moving = True




class Objective:


    def __init__(
            self, objective_num, location,
            direction, image_description
            ):
        self.objective_num = objective_num
        self.location = location
        self.direction = direction
        self.image_description = image_description
   
    def scanned(self):
        fastPrint(
                  f"The screen loads slowly, and in black and white it "
                  f"displays {self.image_description} "
                  )
       
    def check_objective(self, Player):


        if Player.objectives_scanned == 1:
            pass


        elif Player.objectives_scanned == 2:
            Player.next_objective = Objective(2, [385, 250], 45, "a wierd temple")


        elif Player.objectives_scanned == 3:
            Player.next_objective = Objective(3, [258, 416], 135, "half a statue of the moon")


        elif Player.objectives_scanned == 4:
            Player.next_objective = Objective(4, [525, 275], 315, "large white curved spikes")


        elif Player.objectives_scanned == 5:
            Player.next_objective = Objective(5, [658, 166], 265, "scraps of metal strewn around")


        elif Player.objectives_scanned == 6:
            Player.next_objective = Objective(6, [850, 300], 45, "scraps of metal strewn around")


        elif Player.objectives_scanned == 7:
            Player.next_objective = Objective(7, [633, 525], 90, "scraps of metal strewn around")


        elif Player.objectives_scanned == 8:
            Player.next_objective = Objective(8, [175, 575], 180, "scraps of metal strewn around")


        elif Player.objectives_scanned == 9:
            Player.next_objective = Objective(9, [316, 758], 0, "scraps of metal strewn around")


        elif Player.objectives_scanned == 10:
            Player.next_objective = Objective(10, [675, 833], 45, "a thin path probably too thin to fit the submarine")


        elif Player.objectives_scanned == 11:
            Player.next_objective = Objective(11, [942, 875], 90, "scraps of metal strewn around")


#Prints the direction you are facing as a angle clockwise from North


class Action:
    def __init__(self):
        self.action = {
            "help": "Prints all available action options",
            "move": "Moves your submarine for as many seconds as you want in the direction your facing at a speed of 10 meters per second",
            "turn": "Turns your submarine clockwise or anti-clockwise from your current direction for as many degrees as you want",
            "scan": "Allows you to inspect the current state of your submarine based on limited information",
            "fix": "Spends time to repair the hull of the submarine for damage",
            "clock": "Displays the time left until you run out of oxygen",
            "stop": "Stops any submarine movment immediately"
            }
        self.scan = ["location", "direction", "damage", "objective", "next objective"]


player = Player([150,90], 0, 10, 0, 100)
player_options = Action()




moving_avaliable = True
playing = True
oxygen_time_left = 600
time_passed = 0
clock_running = True
clock_active = False




def game_clock():
    global time_passed
    global oxygen_time_left
    while clock_running:
        if clock_active:
            time.sleep(0.1)   # 0.1 second per tick
            time_passed += 0.1  # update clock by 100 mili seconds
            oxygen_time_left -= 0.1
        else:
            time.sleep(0.1)


def moving():
    while moving_avaliable:
        if player.move_player:
            radians = math.radians(player.direction)
            x_axis_direction = math.cos(radians) * player.speed
            y_axis_direction = math.sin(radians) * player.speed


            for seconds in range(player.move_input):


                for number in range(10):
                    if not player.stop_moving:
                        player.location[0] += (x_axis_direction / 10)
                        player.location[1] += (y_axis_direction /  10)
                        normalPrint(player.location)
                        time.sleep(0.1)
        player.move_player = False
        time.sleep(0.1)




moving_thread = threading.Thread(target=moving, daemon=True)
clock_thread = threading.Thread(target=game_clock, daemon=True)


moving_thread.start()


clock_thread.start()


#CHANGE BACK BEFORE HAND IN
def normalPrint(words):
    letters = list(words)


    for letter in letters:
        print(letter, end="", flush=True)
        time.sleep(0.08)




def fastPrint(words):
    letters = list(words)


    for letter in letters:
        print(letter, end="", flush=True)
        time.sleep(0.015)












dev = input("")


if dev == "dev":
    intro = False
else:
    intro = True






if intro:
    normalPrint("Welcome To SUSTAINED PRESSURE")


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
    'communications are lost shortly after submerging.'
    )


    fastPrint(
    '\n\nYou are promised freedom your upon your return to the surface, but '
    'a note left by a previous occupant of the submarine warns you otherwise.'
    )


    normalPrint(
    '\n\nYou only have 10 minutes make them count.'
    )


    normalPrint("\n\nWould you like a tutorial? [Y/n]")


    ans = input("\n").strip().lower()


    if  ans == "n":
        tutorial = False


    elif ans == "y":
        tutorial = True


    else:
        normalPrint("err: assuming you want tutorial")
        tutorial = True


    if tutorial:
        normalPrint("\n||Tutorial||")
        fastPrint(
            "\n\nYou spawn in at coordinates 150,90 facing north and have to "
            "scan various objectives to complete the game."
            )
        fastPrint(
            "\n\nThe game is played via various inputs you type in if you input "
            "'help' it will display all the avaliable inputs that can be made."
            )
        fastPrint("\n\nfor example if you input 'scan':")
        normalPrint("\n\ninput: scan")
        normalPrint("\n\n>>> what would you like to scan?")
# .join(scan options) is taking the list of strings and putting them together seperated by spaces or ", " in this case as a single string
        fastPrint("\n>>> " + ", ".join(player_options.scan))
        normalPrint("\n\ninput: location")
        fastPrint("\n\n>>> you scan your current location on the submarine terminal")
        fastPrint(f"\n>>> LOCATION: {player.location}")
        fastPrint(
            '\n\nThats the tutroirla input "help" whenever your in open water '
            'to open iput options :)'
            )




Print(
    "\n\n\nYour submarine shudders as you reach the designated depth."
    "\nYou check your pocket watch you only have 10 minutes of oxygen it "
    "would be best to move quickly"
    )


clock_active = True


while playing:
    player.action_input()


