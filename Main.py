import random

enemy_ac = int(input("Enter enemy AC to roll attack:"))

atk = random.randrange(0, 20)

if atk == 0:
    print("Critical fail!")

else:
    atk = int(input("Enter attack modifier:")) + atk

    if atk > enemy_ac:
        winning = True
        print("You strike your enemy!")
        while winning:
            num_dice = input("How many dice?:")
            max_side = int(input("How many sides?:"))
            atk_mod = int(input("Attack modifier?:"))
            die_roll = 0

            for num_dice in num_dice: #Won't iterate!
                dmg = die_roll + random.randrange(1, max_side)
                print(die_roll)
                dmg + dmg
            dmg = die_roll + atk_mod

            print("You attacked for", dmg, "damage.")

    else:
        print("Your attack fails to penetrate your enemies defenses!")
