from .base import Character

class Mage(Character):
    def use_skill(self, other):
        damage = self.attack + 10
        other.damage(damage)
        self.add_xp(20)
