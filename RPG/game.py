import random
import time

def print_stats(player, enemy):
    print(f"""\n📊 Player Stats:
Health: {player['health']} / {player['max_health']}
Potions: {player['potion']}
Power Attack: {player['power_attack']}
Inventory: {player['inventory']}

🐺 Enemy Stats:
Health: {enemy['health']}
Power Attack: {enemy['power_attack']}\n""")

def combat(player, enemy):
    print("\n⚔️ Битва начинается! Удачи тебе, рыцарь Альберт!")
    while player["health"] > 0 and enemy["health"] > 0:
        print_stats(player, enemy)
        choice = input("Выбери действие:\n1 - Атаковать\n2 - Использовать зелье\n3 - Сбежать\n> ")

        if choice == "1":
            damage = random.randint(player["power_attack"], player["power_attack"] + 5)
            if random.randint(1, 100) <= player["critical_chance"]:
                damage = round(damage * 1.5)
                print(f"💥 Критический удар! Урон: {damage}")
            else:
                print(f"🗡️ Ты нанёс {damage} урона врагу.")
            enemy["health"] -= damage

        elif choice == "2":
            if player["potion"] > 0:
                player["potion"] -= 1
                heal = player["potion_power"]
                player["health"] = min(player["health"] + heal, player["max_health"])
                print(f"🧪 Ты использовал зелье и восстановил {heal} здоровья.")
            else:
                print("❌ У тебя нет зелий!")

        elif choice == "3":
            print("🏃‍♂️ Пытаешься сбежать...")
            time.sleep(2)
            if player["speed"] >= enemy["speed"]:
                print("✅ Ты успешно сбежал!")
                return
            else:
                print("❌ Враг догнал тебя и атакует!")

        # Enemy counterattack
        if enemy["health"] > 0:
            enemy_damage = random.randint(enemy["power_attack"], enemy["power_attack"] + 5)
            player["health"] -= enemy_damage
            print(f"🐺 Враг атакует и наносит {enemy_damage} урона!")

    # Combat outcome
    if player["health"] <= 0:
        print("💀 Ты проиграл...")
    elif enemy["health"] <= 0:
        print("🏆 Ты победил врага!")
        player["money"] += enemy["money_drop"]
        print(f"💰 Ты получил {enemy['money_drop']} монет.")
        if "knife" in player["inventory"]:
            rr = input("🔪 Хочешь снять шкуру с врага? (yes/no): ").lower()
            if rr == "yes":
                player["inventory"].append("wolf skin")
                print("🧤 Ты снял шкуру. Она добавлена в инвентарь.")
            else:
                print("😕 Ты отказался от шкуры.")
    print("🌲 Твое приключение завершено.")

def main():
    while True:
        player = {
            "health": 100,
            "max_health": 100,
            "power_attack": 15,
            "money": 20,
            "potion": 2,
            "critical_chance": 30,
            "speed": 10,
            "potion_power": 30,
            "inventory": ["craft_book", "knife"]
        }

        print("👑 Привет, дорогой игрок! Ты играешь за рыцаря Альберта.")
        print("Твоя задача — спасти тролля от принцессы. Да, всё наоборот!")
        print("Ты начинаешь своё путешествие в замке твоего отца.")
        print("🎲 Удачи тебе!")

        choice = input("\nКуда ты пойдёшь сначала?\n1 - В лес\n2 - В деревню\n3 - К горной пещере\n> ")

        if choice == "1":
            print("\n🌳 Ты направляешься в лес. Там ты слышишь рычание... это волки!")
            action = input("Что будешь делать?\n1 - Убежать\n2 - Сражаться\n> ")
            if action == "1":
                print("😌 Ты продолжаешь путешествие, но ничего не получаешь.")
            elif action == "2":
                wolf = {
                    "power_attack": 10,
                    "speed": 5,
                    "health": 200,
                    "money_drop": 100
                }
                combat(player, wolf)

        elif choice == "2":
            print("\n🏘️ Ты идёшь в деревню. Люди боятся принцессы и просят твоей помощи.")
            print(" и вдруг внезапно старый человек подходит и говорит чтобы спасти жителей И троля от принцесса Тебе нужно метеорический меч который находится вы вершине горы Альберта ")

        elif choice == "3":
            print("\n⛰️ Ты приближаешься к горной пещере. Внутри слышны странные звуки...")
            print("🚧 Здесь скоро появится битва с магическим существом.")

        else:
            print("❓ Неверный выбор. Попробуй снова.")

        replay = input("\nХочешь сыграть снова? (yes/no): ").lower()
        if replay != "yes":
            print("👋 Спасибо за игру! До скорых встреч.")
            break
        
if __name__ == "__main__":
    main()