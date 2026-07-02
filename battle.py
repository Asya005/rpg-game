import random

"""Handles turn-based battle system."""

class Battle:
    def play(self, a, b):
        """Main fight loop."""

        while a.is_alive() and b.is_alive():
            print("\n")
            print(a)
            print(b)

            print("\n1 Attack")
            print("2 Skill")
            print("3 Show")

            choice = input("Choose: ")

            if choice == "1":
                a.basic_attack(b)

            elif choice == "2":
                a.use_skill(b)

            elif choice == "3":
                print(a)
                print(b)
                continue

            if b.is_alive():
                if random.choice([True, False]):
                    b.basic_attack(a)
                else:
                    b.use_skill(a)

        winner = a if a.is_alive() else b
        winner.add_xp(30)

        print("\nWinner:", winner.name)
