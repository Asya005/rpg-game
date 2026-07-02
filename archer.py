from .base import Character

class Archer(Character):
    def use_skill(self, other):
        damage = self.attack + 5
        other.damage(damage)
        self.add_xp(15)
