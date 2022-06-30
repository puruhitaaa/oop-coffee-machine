from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Penny = 1 cent ($0.01)
# Dime = 10 cents ($0.10)
# Nickel = 5 cents ($0.05)
# Quarter = 25 cents ($0.25)

espresso = MenuItem('Espresso', 100, 0, 24, 5)
latte = MenuItem('Latte', 200, 100, 18, 10)
cappucino = MenuItem('Cappucino', 200, 50, 14, 7.5)
item_dict = {'espresso': espresso, 'latte': latte, 'cappucino': cappucino}

items = Menu()
items_str = items.get_items()
should_continue = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print('Welcome to StarboxCoffee!')
while should_continue:
  initial_input = input("Type 'menu' to get the menu items or 'exit' to cancel. ")

  if initial_input == 'exit':
    should_continue = False
  elif initial_input == 'report':
    coffee_maker.report()
  elif initial_input == 'menu':
    print(f"Items available: {items_str}")
    picked_item = input('What do you want to order today? ')

    if not coffee_maker.is_resource_sufficient(item_dict[picked_item]):
      print(f"We are sorry. The resources are not sufficient to make {picked_item}.")
      next_prompt = input("Type 'refill' to refill the resources or 'exit' to stop the machine: ")

      if next_prompt == 'stop':
        should_continue = False
      elif next_prompt == 'refill':
        coffee_maker.__init__()
        print('Refilled resources!')
      else:
        print('Invalid command, please try again')
    else:
      print(f"That would be ${item_dict[picked_item].cost}")
      is_payment_accepted = money_machine.make_payment(item_dict[picked_item].cost)

      if not is_payment_accepted:
        total_money = money_machine.process_coins()
        print(f'Not enough money, inserted: ${total_money} required: ${item_dict[picked_item].cost}')
      else:
        coffee_maker.make_coffee(item_dict[picked_item])
  else:
    print('Invalid input, please try again.')
    should_continue = False