# Level 3: Hard - Object-Oriented Programming (OOP)
# Focus: Data Abstraction (Classes), Encapsulation, and advanced game structure.

class Room:
    """
    Represents a location in the game. Each room object holds its own data
    (description, items) and knows about its possible exits.
    """
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        # Exits is a dictionary mapping direction strings to room names
        self.exits = exits
        # Items is a list of strings representing items currently in the room
        self.items = items if items is not None else []
        self.has_chest = False
        self.chest_unlocked = False

    def describe(self):
        """Prints the room's description and available visible elements."""
        print(f"\n--- {self.name.upper()} ---")
        print(self.description)
        
        # Show items in the room
        if self.items:
            print(f"You see: {', '.join(self.items)}.")
        
        # Show exits
        exit_list = ", ".join([f"{d.upper()} ({r})" for d, r in self.exits.items()])
        print(f"Exits available: {exit_list}.")
        
        # Special logic for the chest in the corridor
        if self.has_chest:
            if self.chest_unlocked:
                print("An old wooden CHEST sits open against the east wall.")
            else:
                print("An old wooden CHEST sits firmly locked against the east wall.")


class Game:
    """
    The main game engine, managing the map, player state, and game loop.
    """
    def __init__(self):
        self.map = self._setup_map()
        self.current_room = self.map["cell"]
        self.inventory = []
        self.game_status = "playing"
        print("--- THE DARK CELL ESCAPE (Level 3: Object-Oriented) ---")
        print("Your mission: Find the exit and escape the old prison.")

    def _setup_map(self):
        """Initializes all Room objects and links them together."""
        cell = Room(
            name="Cell", 
            description="A damp, cold cell. The main door is heavy and locked.", 
            exits={'north': 'corridor'}, 
            items=['loose stone'] # Note: key is hidden inside the stone
        )
        corridor = Room(
            name="Corridor", 
            description="You are in a long, dark corridor. The air is stale.", 
            exits={'south': 'cell'}
        )
        corridor.has_chest = True # Add a specific flag for the puzzle

        return {
            "cell": cell,
            "corridor": corridor
        }

    def play(self):
        """The main loop for the game."""
        while self.game_status == "playing":
            self.current_room.describe()
            
            action = input("\nWhat do you do? > ").lower().split()
            if not action:
                continue

            command = action[0]
            
            # 1. Navigation Commands (Check Room Exits)
            if command in self.current_room.exits:
                self._move(command)
            
            # 2. State & Inventory Commands
            elif command == "inventory":
                self._show_inventory()
            
            # 3. Puzzle & Interaction Commands
            elif command == "look" and "stone" in self.current_room.items and self.current_room.name == "Cell":
                self._pry_stone()
            
            elif command == "open" and action[-1] == "chest" and self.current_room.name == "Corridor":
                self._open_chest()

            elif command == "quit":
                self.game_status = "quit"
                print("You give up and accept your fate. Game Over.")
            
            else:
                print("I don't understand that command. Try a direction or an action like 'inventory'.")

        if self.game_status == "win":
            print("\n*** CONGRATULATIONS! YOU ESCAPED THE PRISON! ***")

    # --- Game Handler Methods (Behaviors) ---

    def _move(self, direction):
        """Updates the current room based on the direction command."""
        next_room_name = self.current_room.exits[direction]
        self.current_room = self.map[next_room_name]

    def _show_inventory(self):
        """Prints the player's inventory."""
        if self.inventory:
            print(f"Inventory: {', '.join(self.inventory)}")
        else:
            print("Your inventory is empty.")

    def _pry_stone(self):
        """Handles the 'look' action specifically in the cell to find the key."""
        if 'loose stone' in self.current_room.items:
            print("You successfully pry up the loose stone and find a small, brass key!")
            # Remove the stone, add the key
            self.current_room.items.remove('loose stone')
            self.inventory.append('brass key')
        else:
            print("You look around but find nothing new.")

    def _open_chest(self):
        """Handles the 'open chest' action in the corridor."""
        corridor = self.map["corridor"] # Access the specific Room object
        
        if corridor.chest_unlocked:
            print("The chest is already open. You see a glint of sunlight coming from a hole in the ceiling!")
            print("You climb up and escape!")
            self.game_status = "win"
            
        elif 'brass key' in self.inventory:
            print("You insert the brass key into the old lock. It clicks open!")
            corridor.chest_unlocked = True
        
        else:
            print("The chest is firmly locked. You need a key to open it.")

# --- Start the Game ---
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play()

