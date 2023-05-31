from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print('2023 Porsche 911: $106,100, With a down payment amount of: ',amount)
# This function is an example of abstraction.I will pass in an argument, but I will not tell you how or what kind of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class carLoan(car):
# This is where I have defined how to implement the payment function from its parent Payment_Slip class.
    def payment(self, amount):
        print('{} will be your monthly payment for the next 60 months with an APR of 2.49%.'.format(amount))

obj = carLoan()
obj.paySlip('$30,000')
obj.payment('$1,299.91')
