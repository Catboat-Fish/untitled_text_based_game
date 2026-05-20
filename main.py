import random
import math

random.seed()
game_running = True

class Player:
    def __init__(self,attack, defense, max_hp):
        self.attack = attack
        self.defense = defense
        self.max_hp = max_hp
        self.hp = max_hp
        self.level = 0
        self.xp = 0
        self.coins = 0
    
    def take_damage(self, damage):
        true_damage = max(1, int(damage * ((100 - self.defense) / 100)))
        self.hp = max(0, self.hp - true_damage)
    
    def heal(self):
        if self.level == 0:
            self.hp = min(self.max_hp, self.hp + 1)
        elif (self.level * 5) + self.hp >= self.max_hp:
            self.hp = self.max_hp
        else:
            heal_amount = self.level * 5
            self.hp = min(self.max_hp, self.hp + heal_amount)
    
    def fullheal(self):
        self.hp = self.max_hp
    
    def statcheck(self): # prints current stats (useful for debug)
        print(f'Attack: {self.attack}\nDefense: {self.defense}\nMax HP: {self.max_hp}\n HP: {self.hp}')
    
    def level_up_check(self): # levels up one level at a time
        while self.xp >= 1000:
            self.xp -= 1000
            self.level += 1
            self.hp = self.max_hp
            print(f'You are now level {self.level}. Which stat do you want to level up?')
            if self.defense < 50:
                print('1. Attack\n2. Defense\n3. Max HP')
                improve = input()
                if improve == '1':
                    self.attack += 2
                elif improve == '2':
                    self.defense = max(50, self.defense + 2)
                elif improve == '3':
                    self.max_hp += 10
                    self.hp += 10
                else:
                    self.xp += 1000
                    continue
            else:
                print('1. Attack\n2. Max HP')
                improve = input()
                if improve == '1':
                    self.attack += 2
                elif improve == '2':
                    self.max_hp += 10
                    self.hp += 10
                else:
                    self.xp += 1000
                    continue

class Enemy:
    def __init__(self, name, attack, defense, max_hp, reward):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_hp = max_hp
        self.hp = max_hp
        self.xp = reward
        # coins are 1/10 t0 1/5 of reward
        self.coins = random.randint(math.ceil(self.xp * 0.10), math.floor(self.xp * 0.20))
    
    def take_damage(self, damage):
        true_damage = max(1, int(damage * ((100 - self.defense) / 100)))
        self.hp = max(0, self.hp - true_damage)

enemies = { # xp reward for now = (hp * def%[1+{defense/100}]) + (attack * 5)
    'Goblin': (20, 0, 150, 250),
    'Bandit': (30, 0, 100, 250),
    'Orc': (60, 20, 300, 660),
    'Demon': (100, 10, 500, 800),
    'Dragon': (200, 25, 1000, 2250)
}

# game loop
if __name__ == "__main__"
while game_running:
    game_state = 'menu'
    pass
