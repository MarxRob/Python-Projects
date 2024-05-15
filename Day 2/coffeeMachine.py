from prettytable import *

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO: Create a loop that'll keep asking user what do they want(espresso, latte, cappuccino)
# 1. I'll need a while loop so that it keeps asking the user
# 2. I'll also insert the 'resource' option so that a worker can check the machine's resource
menu_table = PrettyTable()
menu_table.add_column("Produto", ["Espresso (E)", "Latte (L)", "Capuccino (C)"])
menu_table.add_column("Preço (R$)", [MENU['espresso']['cost'], MENU['latte']['cost'],
                                     MENU['cappuccino']['cost']])

bill = 0
user_money = 0
can_brew = True
print(f"Bem-vindo(a)! Esse é o nosso cardápio: \n{menu_table}")
while True:
    user_choice = input("Qual será o pedido?: ").lower()

    if user_choice == "r":
        print(resources)
    elif user_choice == "e":
        if (resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] >=
                MENU['espresso']['ingredients']['coffee']):
            bill += MENU['espresso']['cost']
            resources['water'] -= 50
            resources['coffee'] -= 18
            print(f"O valor do espresso é R${MENU['espresso']['cost']:.2f}")
            wants_more = input("Deseja mais alguma coisa(S/N)?: ").lower()
            if wants_more == "s":
                continue
            else:
                print(f"O valor total é de R${bill:.2f}")
                break
        elif (resources['water'] < MENU['espresso']['ingredients']['water'] or resources['coffee'] <
                MENU['espresso']['ingredients']['coffee']):
            print("Não há recursos o suficiente. Por favor, chame um funcionário.")
            can_brew = False
            break
    elif user_choice == "l":
        if (resources['water'] >= MENU['latte']['ingredients']['water'] and resources['coffee'] >=
                MENU['latte']['ingredients']['coffee'] and resources['milk'] >=
                MENU['latte']['ingredients']['milk']):
            bill += MENU['espresso']['cost']
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
            print(f"O valor do latte é R${MENU['latte']['cost']:.2f}")
            wants_more = input("Deseja mais alguma coisa(S/N)?: ").lower()
            if wants_more == "s":
                continue
            else:
                print(f"O valor total é de R${bill:.2f}")
                break
        elif (resources['water'] < MENU['latte']['ingredients']['water'] or resources['coffee'] <
                MENU['latte']['ingredients']['coffee'] or resources['milk'] >=
                MENU['latte']['ingredients']['milk']):
            print("Não há recursos o suficiente. Por favor, chame um funcionário.")
            can_brew = False
            break
    elif user_choice == "c":
        if (resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['coffee'] >=
                MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] >=
                MENU['cappuccino']['ingredients']['milk']):
            bill += MENU['espresso']['cost']
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
            print(f"O valor do cappuccino é R${MENU['cappuccino']['cost']:.2f}")
            wants_more = input("Deseja mais alguma coisa(S/N)?: ").lower()
            if wants_more == "s":
                continue
            else:
                print(f"O valor total é de R${bill:.2f}")
                break
        elif (resources['water'] < MENU['cappuccino']['ingredients']['water'] or resources['coffee'] <
                MENU['cappuccino']['ingredients']['coffee'] or resources['milk'] >=
                MENU['cappuccino']['ingredients']['milk']):
            print("Não há recursos o suficiente. Por favor, chame um funcionário.")
            can_brew = False
            break


# TODO: Check resource availability
# Done, just not in the most effective way. But that'll be tackled later on.

# TODO: Show client final price and ask for payment
if can_brew:
    quarters = int(input("Quantas moedas de 25 cents serão inseridas?: "))
    dimes = int(input("Quantas moedas de 10 cents serão inseridas?: "))
    nickles = int(input("Quantas moedas de 5 cents serão inseridas?: "))
    pennies = int(input("Quantas moedas de 1 cent serão inseridas?: "))

    user_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    # TODO: Do payment process
    if user_money < bill:
        user_money = 0
        print("Sinto muito, este valor não é o suficiente. Você será estornado.")
    elif user_money > bill:
        change = user_money - bill
        print(f"Aqui esté seu troco de R${change:.2f} "
              f"Muito obrigado pela compra! Aproveite seu pedido e volte sempre :)")
    else:
        print("Muito obrigado pela compra! Aproveite seu pedido e volte sempre :)")



