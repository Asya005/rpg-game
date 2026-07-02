from .base import Character

class Enemy(Character):
    def use_skill(self, other):
        damage = self.attack + 3
        other.damage(damage)
        self.add_xp(12)
