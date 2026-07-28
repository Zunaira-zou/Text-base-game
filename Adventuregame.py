#Simple Text-Based Adventure Game
import random
import time
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 50
        self.inventory = ["rusty sword"]
        self.location = "village"

    def status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Health : {self.health}")
        print(f"Gold   : {self.gold}")
        print(f"Items  : {', '.join(self.inventory)}")
        print(f"Place  : {self.location}")
        print("-" * 28)

    def is_alive(self):
        return self.health > 0

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def encounter_enemy(player):
    enemies = ["goblin", "wolf", "bandit", "skeleton"]
    enemy = random.choice(enemies)
    enemy_hp = random.randint(20, 45)
    print_slow(f"\nA wild {enemy} appears!")

    while enemy_hp > 0 and player.is_alive():
        print(f"\n{enemy.title()} HP: {enemy_hp} | Your HP: {player.health}")
        action = input("Fight (f) or Run (r)? ").lower().strip()

        if action == "f":
            damage = random.randint(8, 18)
            enemy_hp -= damage
            print(f"You hit the {enemy} for {damage} damage!")
            if enemy_hp <= 0:
                gold_found = random.randint(10, 30)
                player.gold += gold_found
                print_slow(f"You defeated the {enemy} and found {gold_found} gold!")
                break
            enemy_damage = random.randint(5, 15)
            player.health -= enemy_damage
            print(f"The {enemy} hits you for {enemy_damage} damage!")
        elif action == "r":
            if random.random() > 0.4:
                print("You escaped successfully!")
                break
            else:
                print("You failed to run!")
                enemy_damage = random.randint(5, 12)
                player.health -= enemy_damage
                print(f"The {enemy} hits you for {enemy_damage} damage!")
        else:
            print("Invalid choice.")

    if not player.is_alive():
        print_slow("\nYou have been defeated... Game Over.")
#and in here, the player can visit the shop to buy items that can help them in their adventure. The shop offers health potions.
def visit_shop(player):
    print_slow("\nWelcome to the Village Shop!")
    print("1. Health Potion (25 gold) - restore 40 HP")
    print("2. Steel Sword (60 gold) - better weapon")
    print("3. Leave shop")
#in this section, the player can choose to buy a health potion or a steel sword if they have enough gold. If they don't have enough gold, they are informed and can choose another option.
    choice = input("What would you like to buy? ").strip()
    if choice == "1":
        if player.gold >= 25:
            player.gold -= 25
            player.health = min(100, player.health + 40)
            print("You drank a health potion. Feeling better!")
        else:
            print("Not enough gold.")
    elif choice == "2":
        if player.gold >= 60:
            player.gold -= 60
            if "steel sword" not in player.inventory:
                player.inventory.append("steel sword")
                if "rusty sword" in player.inventory:
                    player.inventory.remove("rusty sword")
            print("You bought a shiny steel sword!")
        else:
            print("Not enough gold.")
    else:
        print("You leave the shop.")
#this function allows the player to explore different locations, encounter enemies, or find gold. The outcome is randomized to keep the game interesting.
def explore(player):
    places = {
        "forest": "You walk into a dark forest. Trees whisper around you.",
        "cave": "You enter a damp cave. Something glows in the distance.",
        "river": "You reach a sparkling river. Fish jump in the water."
    }
    location = random.choice(list(places.keys()))
    player.location = location
    print_slow(places[location])

    if random.random() < 0.6:
        encounter_enemy(player)
    else:
        found = random.randint(5, 20)
        player.gold += found
        print(f"You found {found} gold coins on the ground!")
# this function handles the main game loop, allowing the player to explore, visit the shop, rest, or quit. The game continues until the player dies or chooses to quit.
def main():
    print("=" * 40)
    print("   WELCOME TO PYTHON ADVENTURE")
    print("=" * 40)
    name = input("Enter your hero's name: ").strip() or "Adventurer"
    player = Player(name)
    print_slow(f"\nGreetings, {player.name}! Your journey begins...")

    while player.is_alive():
        player.status()
        print("\nWhat do you want to do?")
        print("1. Explore the wilderness")
        print("2. Visit the shop")
        print("3. Rest (recover some HP)")
        print("4. Quit game")

        choice = input("> ").strip()

        if choice == "1":
            explore(player)
        elif choice == "2":
            player.location = "village"
            visit_shop(player)
        elif choice == "3":
            heal = random.randint(10, 25)
            player.health = min(100, player.health + heal)
            print(f"You rest and recover {heal} health.")
        elif choice == "4":
            print_slow(f"\nFarewell, {player.name}. You leave with {player.gold} gold.")
            break
        else:
            print("Invalid option. Try again.")

        if not player.is_alive():
            break
#and the game ends when the player dies or chooses to quit
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
