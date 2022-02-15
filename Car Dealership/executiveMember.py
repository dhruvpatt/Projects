# Dhruv Patel, Haran M
# Dec 30th, 2021
# Executive Customer Class

from customer import Customer
from random import randint

class ExecutiveCustomer(Customer):

    def __init__(self, customer):

        super().__init__(customer.getName(), customer.getEmail(), customer.getUsername(), customer.getPassword(), customer.getMembershipType(), customer.getCreditScore(), customer.getSecurityQuestion(), customer.getDiscountAmmount(), customer.getAccountBalance())
        self.__discountAmount = 5

    def getDiscountAmount(self):
        return self.__discountAmount

    def setDiscountAmount(self, amount):
        self.__discountAmount = amount


    def draw(self):

        # executive members have the option to participate in draw that allows them to win a prize.

        # getting a random number between 0-10
        randomNum1 = randint(0,10)
        print("""
        Welcome to the executive member draw: 
        You will select a number between 0-10 and if you select the correct number you can win $5000! 
        Good Luck! """)
        repeat = True

        while repeat == True:
            # user selects a number.
            userChoice = int(input(("Enter a number between 0-10: ")))
            # if they select the correct number, they get 5000
            if userChoice == randomNum1:

                print('Congratulations you are a winner. $5000 have been deposited into your account.')
                self.addDrawFunds(5000)
                break

            elif userChoice != randomNum1 and (userChoice <= 10 and userChoice >= 0):
                # if they don't pick the right number, the program tells them what the right number was.
                print("Sorry, you didn't select the correct number, please try again later.")
                print("The correct number was: {}".format(randomNum1))
                break

            else:
                # data validation.
                print("That isn't a valid number. Please select a valid number")
                repeat = True


    def addDrawFunds(self, amount):
        # method for adding the funds to the customer if they win the draw.
        # adding the amount to the account balance.
        self.__accountBalance += amount

        f = open('userInfo.txt', 'r')
        lines = [line.rstrip('\n') for line in f]
        f.close()

        for i in range(len(lines)):
            # changing the value in the textfile.
            line = lines[i]

            if line == self.__userName:
                lines[i + 6] = str(self.__accountBalance)

        # rewriting the text file.
        f = open("userInfo.txt", 'w')
        f.truncate(0)

        for line in lines:
            f.write(line)
            f.write('\n')

        return self.__accountBalance

    def toString(self):
        # to string.
        return  """
        Name: {}
        Email: {}
        Username: {}
        Password: {}
        Membership Type: {}
        Credit Score: {}
        Security Question Answer: {}
        Account Balance: {}
        Discount Amount: {}
        """.format(self.getName(), self.getEmail(), self.getUsername(), self.getPassword(), self.getMembershipType(), self.getCreditScore(), self.getSecurityQuestion(), self.getAccountBalance(), self.__discountAmount)

    def toStringWithoutPassord(self):
        # to string without password.
        return """
           Name: {}
           Email: {}
           Username: {}
           Membership Type: {}
           Credit Score: {}
           Security Question Answer: {}
           Discount Amount: {}
           """.format(self.getName(), self.getEmail(), self.getUsername(),self.getMembershipType(), self.getCreditScore(), self.getSecurityQuestion(), self.getAccountBalance(), self.__discountAmount)





















