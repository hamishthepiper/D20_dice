import random

enemy_ac = int(input("Enter enemy AC to roll attack:"))

atk = random.randrange(0, 20)

if atk == 0:
    print("Critical fail!")

elif atk == 20:
    pwning = True
    print("Natty 20! You strike your enemy for critical damage.")
    while pwning:
        num_dice = int(input("How many dice?:")) * 2
        max_side = int(input("How many sides?:"))
        atk_mod = int(input("Attack modifier?:"))
        die_roll = 0
        i = 0
        dmg = 0

        while i < num_dice:
            die_roll = random.randrange(1, max_side)
            print("Dice #" + str(i + 1) + " rolled " + str(die_roll) + " damage.")
            dmg = dmg + die_roll
            i += 1
        dmg = dmg + atk_mod

        print("You attacked for", dmg, "damage.")
        pwning = False

else:
    atk = int(input("Enter attack modifier:")) + atk

    if atk >= enemy_ac < 20:
        winning = True
        print("Your attack succeeds.")
        while winning:
            num_dice = int(input("How many dice?:"))
            max_side = int(input("How many sides?:"))
            atk_mod = int(input("Attack modifier?:"))
            die_roll = 0
            i = 0
            dmg = 0

            while i < num_dice:
                die_roll = random.randrange(1, max_side)
                print("Dice #" + str(i + 1) + " rolled " + str(die_roll) + " damage.")
                dmg = dmg + die_roll
                i += 1
            dmg = dmg + atk_mod

            print("You attacked for", dmg, "damage.")
            winning = False

    else:
        print("Your attack fails to penetrate your enemies defenses!")
