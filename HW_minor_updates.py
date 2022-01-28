# == == == == == == == == == == == == == == == == == == == ==
# You have no items in your cart.
# == == == == == == == == == == == == == == == == == == == ==
# Total: $0.00
# Have a good day! Goodbye!








# ****** USED DEREK'S SHOPPING CART AND REPURPOSED FOR THIS PER OUR DISCUSSION IN CLASS ******* #

from random import random, uniform

class collection:
    def add_item(self, cart, item):          # will use a_list as self
       cart.append(item)

    def costs(self, cart, item):
        self.cost = f'${len(item) * .50} '
        self.tcost = f'${len("".join(cart)) * .50} '

    def savings(self, cart, item):
        self.saving = f'${len(item) * .50} '
        self.tsaving = f'${len("".join(cart)) * .50} '

    def gain(self, cart, item):
        current_gains = uniform(0, 10)
        self.gains = f'{len(item) * current_gains} lbs '
        self.tgains = f'{len("".join(cart)) * current_gains} '

    def loss(self, cart, item):
        current_loss = uniform(0, 10)
        self.losses = f'{len(item) * current_loss} lbs '
        self.tlosses = f'{len("".join(cart)) * current_loss} '


    def remove_item(self, cart, item):       # will use a_list as self
        cart.remove(item)

    def clear_items(self, cart):             # will use a_list as self
        cart.clear()

    def show_items(self):                    # will use a_list as self
        print('='*60)
        if self:
            for idx, val in enumerate(set(self)):
                print(f'{idx+1}: {val} [{self.count(val)}]')
        else:
            print('You have no items in your cart.')
        print('='*60)


    def show_instructions():
        print("""
    Type 'add' to add an item to the list.
    Type 'remove' to remove an item from the list.
    Type 'clear' to remove all items from your cart.
    Type 'quit' to exit program.""")
        print('='*60)

    def __init__(self):
        cart = []
        done = False
        while not done:
            # co()

            collection.show_items(cart)
            collection.show_instructions()

            decision = input('What would you like to do? ').lower()

            if decision == 'quit':
                done = True
            elif decision == 'add':
                item = input('What item would you like to add? ')
                collection.add_item(self, cart, item)
                collection.costs(self, cart, item)
                collection.gain(self, cart, item)
                print(f'You just spent {self.cost} !')
                print(f'Your total is {self.tcost} !')
                print(f'Your added item weighs {self.gains}lbs !')
                print(f'Your cart is now heavier and weighs {self.tgains}lbs !')
                if float(self.tgains) >= 100:
                    print('Your cart is sweaty, wheels are week, weight is heavy, there"s produce on the floor already, Derek"s spaghetti. ')
                    break
            elif decision == 'remove':
                item = input('What item would you like to remove? ')
                collection.remove_item(self, cart, item)
                collection.savings(self, cart, item)
                collection.loss(self, cart, item)
                print(f'You just saved {self.saving} !')
                print(f'Your total is {self.tsaving} !')
                print(f'Your removed item weighs {self.losses}lbs !')
                print(f'Your cart is now lighter and weighs {self.tlosses}lbs !')
                if float(self.tlosses) >= 100:
                    print('Your cart is sweaty, wheels are week, weight is heavy, there"s produce on the floor already, Derek"s spaghetti. ')
                    break
            elif decision == 'clear':
                confirmed = False
                while not confirmed:
                    confirmation = input(
                        'Are you sure you want to remove all items from your cart? This action cannot be undone. Y/N? ').lower()
                    if confirmation == 'y':
                        collection.clear_items(self, cart)
                        confirmed = True
                        input(
                            'All items have been removed from your cart. Press any key to continue.')
                    elif confirmation == 'n':
                        confirmed = True


cart = collection()
