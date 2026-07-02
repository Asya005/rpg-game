"""Base class for all characters."""

class Character:
    total_characters = 0

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.xp = 0

        Character.total_characters += 1

    def is_alive(self):
        return self.health > 0

    def damage(self, damage):
        real_damage = max(0, damage - self.defense)
        self.health -= real_damage

    def add_xp(self, xp):
        self.xp += xp
        if self.xp >= 100:
            self.xp = 0
            self.level += 1
            self.attack += 5
            self.defense += 2
            self.health += 10

    def basic_attack(self, other):
        other.damage(self.attack)
        self.add_xp(10)

    def use_skill(self, other):
        """Override in child classes."""
        pass

    def __str__(self):
        return f"Name: {self.name} | Health: {self.health} | Attack: {self.attack} | Defense: {self.defense} | Level: {self.level} | XP: {self.xp}"
