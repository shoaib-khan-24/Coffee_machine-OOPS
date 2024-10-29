from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()                                           #menu object (checks items and find drinks)
coffee_maker_obj = CoffeeMaker()                            #coffee maker object to make coffee & check resource
money_machine_obj = MoneyMachine()                          #take payment & show report

should_continue = True

while should_continue:
    drink_name = input(f"Which would you like to have? ({menu_obj.get_items()}): ").lower()
    if drink_name == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    elif drink_name == "off":
        should_continue = False
    else:
        your_drink = menu_obj.find_drink(drink_name)
        if your_drink:
            if coffee_maker_obj.is_resource_sufficient(your_drink):
                if money_machine_obj.make_payment(your_drink.cost):
                    coffee_maker_obj.make_coffee(your_drink)



