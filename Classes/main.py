import random
class character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.defending = False
        
    def attack(self, other):
        damage = random.randint(1, self.strength)
        
        if other.defending:
            damage = damage // 2
            other.defending = False
            print(f"{other.name} defended the attack! Damage is halved to {damage}.")
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
    
    def defend(self):
        self.defending = True
        print(f"{self.name} is defending and will take half damage from the next attack.")
        
    def endTurn(self):
        self.defending = False
        
    def isAlive(self):
        return self.health > 0

hero = character("Hero", 100, 20)
enemy = character("Enemy", 80, 15)
turn = 0

while hero.isAlive() and enemy.isAlive():
    print(f"\n--- Turn {turn + 1} ---")
    if turn % 2 == 0:
        action = input("Choose action for Hero (attack/defend): ").lower()
        if action == "attack":
            hero.attack(enemy)
        elif action == "defend":
            hero.defend()
        else:
            print("Invalid action. Turn skipped.")
    else:
        if random.choice(["attack", "defend"]) == "defend":
            enemy.defend()
        else:
            enemy.attack(hero)
    hero.endTurn()
    enemy.endTurn()
    print(f"Hero Health: {hero.health}, Enemy Health: {enemy.health}")
    turn += 1

if hero.isAlive():
    print("\nHero wins!")
else:
    print("\nEnemy wins!")