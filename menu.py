from battle import Battle
from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.enemy import Enemy

"""Handles game menu and character selection."""

def create(choice):
    """Creates character based on user input."""
    if choice == "1":
        return Warrior("Warrior", 100, 20, 5)
    if choice == "2":
        return Mage("Mage", 80, 25, 3)
    if choice == "3":
        return Archer("Archer", 90, 18, 4)
    if choice == "4":
        return Enemy("Enemy", 120, 15, 2)
    return None


def menu():
    """Main game loop."""
    battle = Battle()

    while True:
        print("\n1 Warrior\n2 Mage\n3 Archer\n4 Enemy\n0 Exit")

        p1 = input("Player 1: ")
        if p1 == "0":
            break

        p2 = input("Player 2: ")

        player1 = create(p1)
        player2 = create(p2)

        if not player1 or not player2:
            print("Invalid choice")
            continue

        if type(player1) == type(player2):
            print("Choose different characters")
            continue

        battle.play(player1, player2)
