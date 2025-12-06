class Hero:
    def __init__(self, name, hp, attack_power=10):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other_hero):
        other_hero.hp -= self.attack_power
        print(
            f"{self.name} attacked {other_hero.name}! {other_hero.name}'s HP is now {other_hero.hp}"
        )

    def is_alive(self):
        return self.hp > 0


# # 1. 建立兩隻英雄
# p1 = Hero("Ben", 100)
# p2 = Hero("Boss", 500)

# # 2. 互毆
# p1.attack(p2)  # Ben 打 Boss
# p1.attack(p2)  # Ben 再打 Boss

# # 3. 檢查狀態
# print(f"Boss alive? {p2.is_alive()}")  # 預期 True
# print(f"Boss HP: {p2.hp}")  # 預期 480 (因為被打了兩下，扣 20)
