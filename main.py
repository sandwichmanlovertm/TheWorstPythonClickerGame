# imports
from time import sleep
import pickle
from os.path import exists
# saveable vars
class main_variables:
    coins = 0
    multiplier = 1
    coins_per_click = 1

    multiplier_price = 250
    coins_per_click_price = 50

# not saveable vars
ingame = True
inshop = False

def save_game():
    jjff = {
        "coins": main_variables.coins,
        "multiplier": main_variables.multiplier,
        "coins_per_click": main_variables.coins_per_click,
        "CPCP": main_variables.coins_per_click_price,
        "MPP": main_variables.multiplier_price
    }
    outfile = open("safedata",'wb')
    pickle.dump(jjff, outfile)
    outfile.close()


infile = open("safedata",'rb')
new_dict = pickle.load(infile)
infile.close()

file_exists = exists("safedata")

if file_exists == True:
    infile = open("safedata",'rb')
    new_dict = pickle.load(infile)
    infile.close()
    print("welcome back")
    
    main_variables.coins = new_dict["coins"]
    main_variables.multiplier = new_dict["multiplier"]
    main_variables.coins_per_click = new_dict["coins_per_click"]

    main_variables.multiplier_price = new_dict["CPCP"]
    main_variables.coins_per_click_price = new_dict["MPP"]


def shop_store():
    global ingame, inshop
    while inshop == True:
        print(f"welcome to the shop: you currently have {main_variables.coins}")
        print(f"1. 1 extra coin, price {main_variables.coins_per_click_price}, currently you have {main_variables.coins_per_click} click")
        print(f"2. 1 extra multiplier of coins, price {main_variables.multiplier_price}, currently you have {main_variables.multiplier}")
        print(f"3. exit")
        dfktot = input("what would you choose?: ")
        if dfktot == "1":
            if main_variables.coins > main_variables.coins_per_click_price:
                print("you have purchased extra coins")
                main_variables.coins = main_variables.coins - main_variables.coins_per_click_price
                main_variables.coins_per_click_price = main_variables.coins_per_click_price * 2
                main_variables.coins_per_click = main_variables.coins_per_click + 1
            else: 
                print("you do not have enough money :\\")
        elif dfktot == "2":
            if main_variables.coins > main_variables.multiplier_price:
                print("you have purchased a multiplier")
                main_variables.coins = main_variables.coins - main_variables.multiplier_price
                main_variables.multiplier_price = main_variables.multiplier_price * 2
                main_variables.multiplier = main_variables.multiplier + 1
            else:
                print("you don't have enough coins")
        elif dfktot == "3":
            print("bye! see ya")
            inshop = False

def clicker_game():
    global ingame, inshop
    while ingame == True:
        foff = input("nothing = coins, 1 = shop, 2 = save & quit: ")
        if foff == "1":
            inshop = True
            shop_store()
        elif foff == "2":
            print("goodbye")
            sleep(1)
            ingame = False
            save_game()
        else:
            print("you got " + str(main_variables.coins + main_variables.coins_per_click))
            main_variables.coins = main_variables.coins + main_variables.coins_per_click * main_variables.multiplier

    clicker_game()


# Sorry for bad coding... gonna fix it someday :TrollFace:

# 100 LINES OF CODE... NUUUUUUUUUUUUUUUUUUUUUUUUUUUUUu