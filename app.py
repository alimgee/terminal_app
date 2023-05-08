
import sys
from time import sleep

class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item

class Game:
    def __init__(self):
        self.rooms = [
            Room("Living Room", "The living room is dark and eerie.", "flashlight"),
            Room("Kitchen", "The kitchen smells of rotten food.", "knife"),
            Room("Bedroom", "The bedroom is cold and empty.", "key"),
            Room("Bathroom", "The bathroom is damp and moldy.", "towel"),
            Room("Basement", "The basement is dark and full of cobwebs.", "crowbar")
        ]
        self.current_room = 0
        self.inventory = []

    def print_slow(self, str, color=None):
        if color:
            if color == "red":
                str = f"\033[31m{str}\033[0m"
            elif color == "green":
                str = f"\033[32m{str}\033[0m"
            elif color == "yellow":
                str = f"\033[33m{str}\033[0m"
            elif color == "blue":
                str = f"\033[34m{str}\033[0m"
            elif color == "magenta":
                str = f"\033[35m{str}\033[0m"
            elif color == "cyan":
                str = f"\033[36m{str}\033[0m"
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.1)

    def play(self):
        self.print_slow("Welcome to the scary adventure game!\n", "green")
        self.print_slow("You are in a house with 5 rooms.\n", "green")

        while True:
            room = self.rooms[self.current_room]
            self.print_slow(f"You are in the {room.name}. {room.description}\n", "green")
            self.print_slow(f"There is a {room.item} here.\n", "green")
            self.print_slow("What would you like to do?\n","green")
            self.print_slow("1. Go to the next room\n", "cyan")
            self.print_slow("2. Go to the previous room\n", "cyan")
            self.print_slow("3. Look around\n", "cyan")
            self.print_slow("4. Pick up item\n", "cyan")
            self.print_slow("5. Use item\n", "cyan")
            self.print_slow("6. Check inventory\n", "cyan")
            self.print_slow("7. Exit the game\n", "red")

            choice = input()

            if choice == "1":
                self.current_room += 1
                if self.current_room > 4:
                    self.current_room = 0
            elif choice == "2":
                self.current_room -= 1
                if self.current_room < 0:
                    self.current_room = 4
            elif choice == "3":
                if room.name == "Living Room":
                    self.print_slow("You see a dusty old couch and a broken TV.\n")
                elif room.name == "Kitchen":
                    self.print_slow("You see dirty dishes piled up in the sink and a fridge that's been left open.\n")
                elif room.name == "Bedroom":
                    self.print_slow("You see an unmade bed and clothes scattered on the floor.\n")
                elif room.name == "Bathroom":
                    self.print_slow("You see a dirty bathtub and a toilet that hasn't been flushed.\n")
                elif room.name == "Basement":
                    self.print_slow("You see old boxes and broken furniture. It's hard to see in the darkness.\n")
            elif choice == "4":
                if room.item in self.inventory:
                    self.print_slow(f"You already have the {room.item}.\n")
                else:
                    self.inventory.append(room.item)
                    self.print_slow(f"You picked up the {room.item}.\n")
            elif choice == "5":
                if len(self.inventory) == 0:
                    self.print_slow("You don't have any items in your inventory.\n")
                else:
                    for i, item in enumerate(self.inventory):
                        self.print_slow(f"{i + 1}. {item}\n")

                    item_choice = int(input()) - 1
                    item = self.inventory[item_choice]

                    if item == "flashlight" and room.name == "Basement":
                        self.print_slow("You use the flashlight to see better in the darkness. You find a hidden door!\n")
                    else:
                        self.print_slow(f"You use the {item} but nothing happens.\n")
            elif choice == "6":
                if len(self.inventory) == 0:
                    self.print_slow("Your inventory is empty.\n")
                else:
                    for item in self.inventory:
                        self.print_slow(f"{item}\n")
            elif choice == "7":
                self.print_slow("Goodbye!\n")
                break
            else:
                self.print_slow("Invalid choice. Please try again.\n")

game = Game()
game.play()
