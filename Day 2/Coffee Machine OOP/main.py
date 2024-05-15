import coffeeMachine
import moneyMachine
import menu

coffee_maker_instance = coffeeMachine.CoffeeMaker()
money_machine_instance = moneyMachine.MoneyMachine()
menu_instance = menu.Menu()
machine_on = True
bill = 0

while machine_on:
    menu_items = menu_instance.get_items()
    print(f"Esse é o nosso cardápio do dia: {menu_items}")
    while True:
        try:
            order = input("Qual será o seu pedido?: ").lower()
            break
        except ValueError:
            print("Por favor, insira um pedido válido.")

    if order == "report":
        coffee_maker_instance.report()
        money_machine_instance.report()
    elif order == "off":
        machine_on = False
    else:
        beverage = menu_instance.find_drink(order)
        if (coffee_maker_instance.is_resource_sufficient(beverage) and
                money_machine_instance.make_payment(beverage.cost)):
            coffee_maker_instance.make_coffee(beverage)
