class CoffeeMachine:
    t_inv = {'water': 400, 'milk': 540, 'beans': 120, 'money': 550, 'cups': 9}

    # Function for 'dispensing coffee' after it checks to see if all inventory reqs are met.
    def buy(self):
        choice = input("""Enter the number of the drink you would like:
    1 for espresso, 2 for latte, 3 for cappuccino, or type 'back' to return to the main menu: """)
        if choice == 'back':
            main_screen()
        elif choice == '1':
            self.espresso_reqs()
        elif choice == '2':
            self.latte_reqs()
        elif choice == '3':
            self.capp_reqs()
            main_screen()

    # Function to determine if the machine has enough resources to make an espresso.
    # If no, informs the user.
    # If yes, subtracts resources from t_inv and "makes coffee".
    def espresso_reqs(self):
        if min(self.t_inv['water'] // 250, self.t_inv['beans'] // 16,
               self.t_inv['cups'] // 1) == 0:
            print('Sorry, not enough resources!')
            main_screen()
        else:
            self.t_inv['water'] -= 250
            self.t_inv['beans'] -= 16
            self.t_inv['money'] += 4
            self.t_inv['cups'] -= 1
            self.no_neg_inv()
            self.making_coffee_notice()

    # Function to determine if the machine has enough resources to make a latte.
    # If no, informs the user.
    # If yes, subtracts resources from t_inv and "makes coffee".
    def latte_reqs(self):
        if min(self.t_inv['water'] // 350, self.t_inv['milk'] // 75,
               self.t_inv['beans'] // 20,
               self.t_inv['cups'] // 1) == 0:
            print('Sorry, not enough resources!')
            main_screen()
        else:
            self.t_inv['water'] -= 350
            self.t_inv['beans'] -= 20
            self.t_inv['milk'] -= 75
            self.t_inv['money'] += 7
            self.t_inv['cups'] -= 1
            self.no_neg_inv()
            self.making_coffee_notice()

    # Function to determine if the machine has enough resources to make a cappuccino.
    # If no, informs the user.
    # If yes, subtracts resources from t_inv and "makes coffee".
    def capp_reqs(self):
        if min(self.t_inv['water'] // 200, self.t_inv['milk'] // 100,
               self.t_inv['beans'] // 12,
               self.t_inv['cups'] // 1) == 0:
            print('Sorry, not enough resources!')
            main_screen()
        else:
            # t_inv['water'] = 0 if t_inv['water'] - 200 < 0 else t_inv['water'] -= 200
            self.t_inv['water'] -= 200
            self.t_inv['beans'] -= 12
            self.t_inv['milk'] -= 100
            self.t_inv['money'] += 6
            self.t_inv['cups'] -= 1
            self.no_neg_inv()
            self.making_coffee_notice()

    # Function to display the current inventory of the machine.
    def display_stats(self):
        print(f"""The coffee machine has:
        {self.t_inv['water']} of water
        {self.t_inv['milk']} of milk
        {self.t_inv['beans']} of coffee beans
        {self.t_inv['cups']} of disposable cups
        {self.t_inv['money']} of money
        """)
        main_screen()

    def making_coffee_notice(self):
        print('''I have enough resources, making you a coffee!''')
        main_screen()

    # Function to ensure nothing in the inventory goes negative. Auto corrects to 0.
    def no_neg_inv(self):
        for (key, value) in self.t_inv.items():
            if value < 0:
                self.t_inv[key] = 0
            else:
                self.t_inv[key] = value

    # Function to set money value to 0 if user decides to 'take' all the money.
    def take(self):
        print(f"I gave you ${self.t_inv['money']}")
        self.t_inv['money'] = 0
        main_screen()

    # Function for user to resupply the coffee machine.
    def fill(self):
        self.t_inv['water'] += int(input('How many ml of water do you want to add?: '))
        self.t_inv['milk'] += int(input('How many ml of milk do you want to add?: '))
        self.t_inv['beans'] += int(input('How many grams of coffee beans do you want to add?: '))
        self.t_inv['cups'] += int(input('How many disposable cups do you want to add?: '))
        main_screen()


coffee_machine = CoffeeMachine()


def main_screen():
    options = input("Would you like to 'Buy', 'Fill', 'Take', 'Remaining', or 'Exit'?: ").lower()
    if options == 'buy':
        coffee_machine.buy()
    elif options == 'remaining':
        coffee_machine.display_stats()
    elif options == 'take':
        coffee_machine.take()
    elif options == 'fill':
        coffee_machine.fill()
    elif options == 'exit':
        quit()


main_screen()
