class BankAccount:
    # Constructorul
    def __init__(self, account_holder, iban):
        self.account_holder = account_holder
        self.iban = iban
        self.hip = 0
        self.active = False
        self.pin = 7777
        self.number_of_attempts = 0

    def balance_query(self):
            print(f'Holder {self.account_holder}')
            print(f'IBAN {self.iban}')
            print(f'Hip {self.hip}')
            print(f'Active {self.active}')
            print(f'Number of attempts {self.number_of_attempts}')
            print(f'-----------------------------------------------')

    def account_activation(self, user_pin):
                self.hello()
                if user_pin == self.pin:
                    print('The card has been activated')
                    self.active = True
                else:
                    print('Wrong PIN')
                    self.number_of_attempts = self.number_of_attempts + 1


    def feed_account(self, the_amount):
            self.hello()
            self.hip += the_amount
            print(f'You fed {the_amount}')
            print(f'You have in account {self.hip}')


    def card_payment(self, the_amount):
            self.hello()
            if the_amount <= self.hip:
                self.hip -= the_amount
                print(f'You spent {the_amount}')
                print(f'You have in account {self.hip}')
            else:
                print('Insufficient funds')


    def hello(self):
            print(f'Hello {self.account_holder}')
