import sys
import random
import time


# ============================================================
# Utility Functions
# ============================================================

def slow(text, delay=0.02):
    """Typewriter-style printing for better storytelling."""
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def prompt_choice(prompt, valid):
    """Ask user until they give a valid input."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid:
            return choice
        print("\n❌ Invalid choice. Try again.\n")


# ============================================================
# Player System
# ============================================================

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def damage(self, amount):
        """Decreases player health."""
        self.health -= amount
        if self.health < 0:
            self.health = 0
        slow(f"\n❤️ Health: {self.health}")

        if self.health <= 0:
            slow("\n💀 You have fallen in your adventure...")
            game_over()

    def heal(self, amount):
        """Increase health."""
        self.health += amount
        self.health = min(self.health, 100)
        slow(f"\n💚 You feel better. Health: {self.health}")

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            slow(f"🎒 Added to inventory: {item}")
        else:
            slow(f"🎒 You already have: {item}")


player = None  # Will be assigned when game starts


# ============================================================
# Game Scenes
# ============================================================

def start_game():
    global player

    print("\n✨ WELCOME TO THE ADVENTURE QUEST — ULTIMATE EDITION! ✨\n")
    name = input("What is your name, brave traveler? ").strip() or "Adventurer"
    player = Player(name)

    slow(f"\nWelcome, {player.name}! Your journey begins...\n")

    main_crossroad()


def main_crossroad():
    slow("\n🏞️ You arrive at a crossroads.")
    print("1) Enter the Dark Forest 🌲")
    print("2) Explore the Ancient Cave 🕳️")
    print("3) Visit the Abandoned Village 🏚️")
    print("4) Check Inventory 🎒")
    print("Q) Quit")

    choice = prompt_choice("\nYour choice: ", ["1", "2", "3", "4", "q"])

    if choice == "1":
        forest_path()
    elif choice == "2":
        cave_path()
    elif choice == "3":
        village_path()
    elif choice == "4":
        show_inventory()
        main_crossroad()
    elif choice == "q":
        slow("\nFarewell, explorer! 👋")
        sys.exit()


# ============================================================
# Forest Scene
# ============================================================

def forest_path():
    slow("\n🌲 You walk into the Dark Forest. The atmosphere is heavy.")

    print("\n1) Follow the river 🌊")
    print("2) Climb the ancient tree 🌳")
    print("B) Go back")

    choice = prompt_choice("\nYour move: ", ["1", "2", "b"])

    if choice == "1":
        forest_river()
    elif choice == "2":
        forest_tree()
    else:
        main_crossroad()


def forest_river():
    slow("\n🌊 You walk along the riverbank...")
    slow("You find something behind the waterfall!")

    player.add_item("Ancient Key")
    slow("🗝️ This key feels important...")

    main_crossroad()


def forest_tree():
    slow("\n🌳 You climb the giant tree to get a better view...")

    # 50% chance of falling
    if random.random() < 0.5:
        slow("\n❗ A branch snaps! You fall into thorns!")
        player.damage(35)
    else:
        slow("\n👀 From the top, you spot a hidden temple location!")
        player.add_item("Temple Map")

    main_crossroad()


# ============================================================
# Cave Scene
# ============================================================

def cave_path():
    slow("\n🕳️ You step into the Ancient Cave. It's cold and silent.")

    print("\n1) Light a torch 🔥")
    print("2) Walk in the dark 🌑")
    print("B) Go back")

    choice = prompt_choice("\nYour move: ", ["1", "2", "b"])

    if choice == "1":
        cave_torch()
    elif choice == "2":
        cave_dark()
    else:
        main_crossroad()


def cave_torch():
    slow("\n🔥 You light a torch and move carefully...")
    slow("You find a giant stone door with a keyhole.")

    if "Ancient Key" in player.inventory:
        slow("\n🗝️ You use the Ancient Key...")
        treasure_chamber()
    else:
        slow("\nIt seems locked. You need a key.")
        main_crossroad()


def cave_dark():
    slow("\n🌑 You walk blindly...")
    slow("Suddenly, you fall into a deep pit!")
    player.damage(100)  # instant death


# ============================================================
# Village Scene
# ============================================================

def village_path():
    slow("\n🏚️ The abandoned village is quiet… too quiet.")

    print("\n1) Enter the lonely house 🏠")
    print("2) Search the old well ⛓️")
    print("B) Go back")

    choice = prompt_choice("\nYour move: ", ["1", "2", "b"])

    if choice == "1":
        village_house()
    elif choice == "2":
        village_well()
    else:
        main_crossroad()


def village_house():
    slow("\n🏠 You enter the dusty house...")
    slow("A wild wolf jumps at you!")

    player.damage(30)

    slow("\nYou survive. Inside, you find a healing herb.")
    player.add_item("Healing Herb")

    main_crossroad()


def village_well():
    slow("\n⛓️ You peer into the well...")

    if random.random() < 0.6:
        slow("\nYou pull out a small chest!")
        player.add_item("Gold Coins")
    else:
        slow("\n🐍 A snake bites you!")
        player.damage(20)

    main_crossroad()


# ============================================================
# Final Treasure
# ============================================================

def treasure_chamber():
    slow("\n💎 The chamber opens...")
    slow("\n✨ The legendary treasure lies before you! ✨")
    slow("\n🎉 CONGRATULATIONS! You have completed the Adventure Quest! 🎉")

    restart_game()


# ============================================================
# Inventory
# ============================================================

def show_inventory():
    slow("\n🎒 Your Inventory:")
    if player.inventory:
        for item in player.inventory:
            print(" -", item)
    else:
        print(" (empty)")


# ============================================================
# Game Over / Restart
# ============================================================

def game_over():
    slow("\n💀 GAME OVER.")
    restart_game()


def restart_game():
    choice = prompt_choice("\nPlay again? (yes/no): ", ["yes", "no"])
    if choice == "yes":
        start_game()
    else:
        slow("\nGoodbye, traveler! 👋")
        sys.exit()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    start_game()
