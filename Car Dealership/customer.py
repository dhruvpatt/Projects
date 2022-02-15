# Dhruv Patel
# Dec 17th, 2021
# Customer Class

class Customer:

    def __init__(self, name, email, userName, password, membershipType, creditScore, securityQuestion, discountAmount, accountBalance):

        self.__name = name
        self.__email = email
        self.__userName = userName
        self.__password = password
        self.__membershipType = membershipType
        self.__creditScore = int(creditScore)
        self.__securityQuestion = securityQuestion
        self.__discountAmount = float(discountAmount)
        self.__accountBalance = float(accountBalance)


    # getters

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getUsername(self):
        return self.__userName
    def getPassword(self):
        return self.__password

    def getSecurityQuestion(self):
        return self.__securityQuestion

    def getMembershipType(self):
        return self.__membershipType

    def getDiscountAmmount(self):
        return self.__discountAmount

    def getCreditScore(self):
        return self.__creditScore

    def getAccountBalance(self):
        return self.__accountBalance

    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email

    def setUsername(self,username):
        self.__userName = username

    def setPassword(self, password):
        self.__password = password

    def setSecurityQuestion(self, securityQuestion):
        self.__securityQuestion = securityQuestion

    def setMembershipType(self, membershipType):
        self.__membershipType = membershipType

    def setCreditScore(self, creditScore):
        self.__creditScore = creditScore

    def setAccountBalance(self, accountBalance):
        self.__accountBalance = accountBalance


    def addFunds(self):
        # method that allows the user to add funds.
        # getting input.
        print("You currently have ${} in your account.".format(self.__accountBalance))
        amount = float(input("How much would you like to add/remove to your account: $"))
        self.__accountBalance+= amount
        print("Your new account balance is ${:.2f}".format(self.__accountBalance))
        f = open('userInfo.txt', 'r')
        lines = [line.rstrip('\n') for line in f]
        f.close()

        # iterating through the textfile.
        for i in range(len(lines)):

            line = lines[i]
            # changing the accountbalance for the customer in the textfile.
            if line == self.__userName:
                lines[i + 6] = str(self.__accountBalance)

        # re-writing the textfile.
        f = open("userInfo.txt", 'w')
        f.truncate(0)

        for line in lines:
            f.write(line)
            f.write('\n')

        return self.__accountBalance

    def reduceFunds(self, amount):
        # method for reducing funds.
        # subtracting the amount from the account balance.
        self.__accountBalance -= amount

        f = open('userInfo.txt', 'r')
        lines = [line.rstrip('\n') for line in f]
        f.close()

        for i in range(len(lines)):
            # changing the value in the text file.
            line = lines[i]

            if line == self.__userName:

                lines[i+6] = str(self.__accountBalance)

        # rewriting the text file.
        f = open("userInfo.txt" , 'w')
        f.truncate(0)

        for line in lines:
            f.write(line)
            f.write('\n')

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
        """.format(self.__name, self.__email, self.__userName, self.__password, self.__membershipType, self.__creditScore, self.__securityQuestion, self.__accountBalance)

    def toStringWithoutPassord(self):
        # to string without password.
        return """
        Name: {}
        Email: {}
        Username: {}
        Membership Type: {}
        Credit Score: {}
        Security Question Answer: {}
        """.format(self.__name, self.__email, self.__userName, self.__membershipType, self.__creditScore, self.__securityQuestion)





