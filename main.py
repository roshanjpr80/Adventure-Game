
# The player explores locations, makes choices, and attempts to find a legendary treasure.

import sys


def prompt_choice(prompt, valid_choices):
          """Prompt the player until they enter one of the valid_choices (list of strings)."""
          while True:
                    choice = input(prompt).strip().lower()
                    if choice in valid_choices:
                              return choice
                    print("\nInvalid choice. Please try again.\n")



def start_game():
          print("\n✨ Welcome to the Adventure Quest! ✨")
          print("\nYou are an explorer searching for the legendary treasure hidden in an ancient land.")
          player_name = input("\nWhat is your name, brave adventurer? ").strip() or "Adventurer"
          print(f"\nWelcome, {player_name}! Your journey begins now...\n")

          while True:
                    print("\nYou find yourself at a crossroads.")
                    print("\n1) Enter the dark forest 🌲")
                    print("\n2) Explore the mysterious cave 🕳️")
                    print("\nQ) Quit")

                    choice = prompt_choice("\nWhere would you like to go? (1/2/Q): ", ["1","2","q"])
                    if choice == "1":
                              forest_path(player_name)
                              break
                    elif choice == "2":
                              cave_path(player_name)
                              break
                    elif choice == "q":
                              print("\nFarewell! Thank you for trying the Adventure Quest.")
                              sys.exit()



def forest_path(player_name):
          print(f"\n{player_name}, you venture into the dark forest. The trees whisper secrets and the path is dim.")
          print("\nYou come across a flowing river and a tall, sturdy tree.")
          print("\n1) Follow the river 🌊")
          print("\n2) Climb the tree 🌳")
          print("\nB) Go back")

          choice = prompt_choice("\nWhat will you do? (1/2/B): ", ["1","2","b"])
          if choice == "1":
                    print("\nYou follow the river downstream and discover a hidden waterfall with a shining chest behind it!")
                    print("\nInside, you find the legendary treasure! 💎")
                    print("\n🎉 Congratulations, you have won the game! 🎉")
                    restart_game()
          elif choice == "2":
                    print("\nYou climb the tree to scout the area. From the top you see the cave's mouth far away.")
                    print("\nWhile climbing down, a brittle branch snaps and you fall into a thorny bush. You are injured and can't continue.")
                    print("\nGame Over — your adventure ends here.")
                    restart_game()
          elif choice == "b":
                    start_game()




def cave_path(player_name):
          print(f"\n{player_name}, you step into the mysterious cave. It's cold, damp, and the air smells ancient.")
          print("\nYou have two options to proceed:")
          print("\n1) Light a torch 🔥")
          print("\n2) Proceed in the dark 🌑")
          print("\nB) Go back")

          choice = prompt_choice("\nWhat will you do? (1/2/B): ", ["1","2","b"])
          if choice == "1":
                    print("\nWith the torch lit, you carefully move ahead and discover ancient symbols on the wall.")
                    print("\nBehind a large stone, you find the legendary treasure! 💎")
                    print("\n🎉 Congratulations, you have completed your quest successfully! 🎉")
                    restart_game()
          elif choice == "2":
                    print("\nYou walk blindly into the darkness and fall into a deep pit.")
                    print("\nGame Over — the treasure remains undiscovered.")
                    restart_game()
          elif choice == "b":
                    start_game()



def restart_game():
          print("\nWould you like to play again?")
          choice = prompt_choice("\nType 'yes' to restart or 'no' to quit: ", ["yes","no"])
          if choice == "yes":
                    start_game()
          else:
                    print("\nThank you for playing the Adventure Quest! Farewell, traveler! 👋")
                    sys.exit()




if __name__ == "__main__":
    start_game()