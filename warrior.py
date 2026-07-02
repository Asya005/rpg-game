from .base import Character

class Warrior(Character):
    def use_skill(self, other):
        damage = self.attack * 2
        other.damage(damage)
        self.add_xp(20)
