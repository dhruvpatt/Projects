# Dhruv Patel, Haran M.
# Dec 17th, 2021
# Admin Class

from customer import Customer
from executiveMember import ExecutiveCustomer
from car import Car


class Admin:

    def __init__(self, userInfoFile, carInfoFile, numCustomers, dealership):

        self.__userInfoFile = userInfoFile
        self.__carInfoFile = carInfoFile
        self.__numCustomers = numCustomers
        self.__userInfoLists = []
        self.__passwordsList = []
        self.__usernameList = []
        self.__securityAnswersList = []
        self.__customers = []
        self.__dealership = dealership



    # Getters and Setters

    def getUserInfoFile(self):
        return self.__userInfoFile

    def getCarInfoFile(self):
        return self.__carInfoFile

    def getNumCustomers(self):
        return self.__numCustomers

    def getUserInfoLists(self):
        return self.__userInfoLists

    def getPasswordsList(self):
        return self.__passwordsList

    def getUserNameList(self):
        return self.__usernameList

    def getSecurityAnswersList(self):
        return self.__securityAnswersList

    def getCustomers(self):
        return self.__customers

    def getDealership(self):
        return self.__dealership

    def setUserInfoFile(self, newFile):
        self.__userInfoFile = newFile

    def setCarInfoFile(self, newFile):
        self.__carInfoFile = newFile

    def setNumCustomers(self, int):
        self.__numCustomers = int

    def setUserInfoLists(self, list):
        self.__userInfoLists = list

    def setPasswordsList(self, list):
        self.__passwordsList = list

    def setUsernameList(self, list):
        self.__usernameList = list

    def setSecurityAnswersList(self, list):
        self.__securityAnswersList = list

    def setCustomers(self, list):
        self.__customers = list

    def setDealership(self, dealership):
        self.__dealership = dealership

    def getNumExecutives(self):
        counter = 0
        for customer in self.__customers:

            if customer.getMembershipType() == "Executive Member":

                counter += 1

        return counter



    def createUserInfoLists(self):
        # creating the lists of the user info that will be used to create the customers.
        f = open('userInfo.txt', 'r+')
        # getting the information from the text file into a list.
        userInfo = [line.rstrip('\n') for line in f]
        userInfoLists = []
        # all the properties of each user get appended to a sublist, which then get appended to a main 2-d list.
        namesList = userInfo[0::9]
        userInfoLists.append(namesList)

        emailList = userInfo[1::9]
        userInfoLists.append(emailList)

        userNameList = userInfo[2::9]
        self.__usernameList = userNameList
        userInfoLists.append(userNameList)

        passwordList = userInfo[3::9]
        self.__passwordsList = passwordList
        userInfoLists.append(passwordList)

        membershipType = userInfo[4::9]
        userInfoLists.append(membershipType)

        creditScoreList = userInfo[5::9]
        creditScoreList = [int(i) for i in creditScoreList]
        userInfoLists.append((creditScoreList))

        securityQuestionAnswerList = userInfo[6::9]
        self.__securityAnswersList = securityQuestionAnswerList
        userInfoLists.append(securityQuestionAnswerList)

        discountAmountList = userInfo[7::9]
        discountAmountList = [float(i) for i in discountAmountList]
        userInfoLists.append(discountAmountList)

        accountBalanceList = userInfo[8::9]
        accountBalanceList = [float(i) for i in accountBalanceList]
        userInfoLists.append(accountBalanceList)

        # setting this list of info to the data field of the admin object.
        self.__userInfoLists = userInfoLists

        return userInfoLists

        f.close()

    def createCustomersList(self):

        # method that creates the customers.
        userInfoLists = self.__userInfoLists
        customerList = []
        for i in range(self.__numCustomers):
            # for the number of customers in the list, it takes all the properties of one customer and creates a customer object.
            name = userInfoLists[0][i]
            email = userInfoLists[1][i]
            userName = userInfoLists[2][i]
            password = userInfoLists[3][i]
            membershipType = userInfoLists[4][i]
            creditScore = userInfoLists[5][i]
            securityQuestion = userInfoLists[6][i]
            discountAmount = userInfoLists[7][i]
            accountBalance = userInfoLists[8][i]

            # once the customer object is created, it is appended to a customer list.
            c = Customer(name, email, userName, password, membershipType, creditScore, securityQuestion, discountAmount, accountBalance)
            customerList.append(c)

            if membershipType == "Executive Member":
                # in the case that a customer is an executive member, it deletes the customer from the list
                # an executive customer object is created using that customer object, and appended to the list.
                customerList.remove(c)
                execCustomer = ExecutiveCustomer(c)
                customerList.append(execCustomer)

        # setting the data field as the customer list.
        self.__customers = customerList
        return customerList


    def login(self):
        # login method that allows the user to log in.
        # setting variables as the different data fields.
        usernames = self.__usernameList
        passwords = self.__passwordsList
        answers = self.__securityAnswersList

        # creating a dictionary using the username and password lists.
        logins = dict(zip(usernames, passwords))
        # creating a dictionary using the usernames and answers lists.
        securityQuestions = dict(zip(usernames, answers))
        # boolean variables for loop repition.
        repeat = True
        # counter for the number of incorrect attempts before being asked a security question.
        counter = 0
        # counter for after being asked a security question.
        secondCounter = 0
        securityRepeat = True
        loggedIn = False


        while repeat == True:
            # if the first counter is equal to 3, and the user hasn't logged in yet, then they must answer a security question.
            if counter == 3 and loggedIn != True:
                print('Locked out')
                print('You must answer a security question to continue')
                # asking the security question.
                while securityRepeat == True:
                    userAnswer = input("What was your first car?: ").strip().lower()
                    # if they answer it correctly, then they can try to log in again.
                    if securityName in securityQuestions:

                        answer = securityQuestions.get(username)

                        if userAnswer == answer:
                            loggedIn = True
                            print("Correct!")
                            securityRepeat == False
                            break

                        elif secondCounter == 3:
                            # if they answer the security question wrong too many times, then they are locked out.
                            break

                        else:
                            secondCounter += 1
                            counter += 1

            # if the user fails to provide the correct password 3 more times, (6 in total) then the program ends.
            if counter == 6:
                print("Too many unsuccesful attempts, try again later!")
                sucessfulUsername = None
                break

            # user input for logging in.
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            # if the username is in the logins dictionary.
            if username in logins:
                # getting the password from the login dictionary.
                realPassword = logins.get(username)
                # if password entered matches the password from the dictionary, then the user is logged in.
                if password == realPassword:

                    sucessfulUsername = username
                    repeat = False
                    break

                else:
                    # else prints successful, and adds 1 to the counter.
                    print("Unsuccesful")
                    counter += 1

            else:

                print("Incorrect username or password")

            securityName = username
        # succesfull username is returned.
        return sucessfulUsername

    def createNewCustomer(self):
        # method that creates a new customer.
        f = open('userInfo.txt', 'a')

        userInfo = []
        # getting all the user info.
        name = input("What is your name?: ")
        userInfo.append(name)
        email = input("What is your email?: ")
        userInfo.append(email)

        # validating data to ensure that the username entered doesn't already exist.
        repeat = True
        while repeat == True:

            username = input("Enter a username: ")

            if username in self.__usernameList:

                print("Username already exists try again!")
                repeat = True

            else:
                repeat = False
                userInfo.append(username)

        # getting other user data.
        password = input("Enter your password: ")
        userInfo.append(password)
        membershipType = "Basic Member"
        userInfo.append(membershipType)
        creditScore = input("Enter your credit score: ")
        userInfo.append(creditScore)

        # getting the answer for the security question.
        print("Answer this Security Question: ")
        answer = input("What was your first car: ").strip().lower()
        userInfo.append(answer)

        # automatically set to zero, if user upgrades their membership, then the discount amount is raised.
        discountAmount = str(0)
        userInfo.append(discountAmount)
        # getting how much they want to deposity.
        accountBalance = input("How much money would you like to deposit into this account: $")
        userInfo.append(accountBalance)

        # writing to this text file the new user.
        for lines in userInfo:

            f.write(lines)
            f.write('\n')

        f.close()
        # creating the new customer object and updating the number of customers.
        c = Customer(name, email, username, password, membershipType, creditScore, answer, discountAmount, accountBalance)
        self.__numCustomers += 1
        return c

    def adminMenu(self):
        # method for the admin menu.
        return """
        1. View All Customers 
        2. View All Cars 
        3. Add a Car 
        4. Remove a Car
        5. Upgrade a Member 
        6. Remove a Member 
        7. View Statistics
        8. Exit """


    def addCar(self):
        # method that allows the user to add a car.
        f = open('cars.txt', 'r')
        lines = [line.rstrip('\n') for line in f]
        f.close()

        # while loop ensures that the admin doesn't add a car that already exists in the dealership.
        repeat = True
        while repeat == True:
            name = input("Enter the name of the car: ").title().strip()

            if name in lines:

                print("That car already exists, please enter another car, or press 2 to exit.")


            elif name == '2':

                return None
                break

            else:
                # getting the information about the car.
                price = input("Enter the price of the car: ")
                horsepower = input("Enter the horsepower of the car: ")
                engineType = input("Enter the engine type: ").upper()
                bodyType = input("Enter the body type (Suv, Sedan, Coupe) : ").strip().title()
                carType = input("Enter the car type(Super Car, Sports Car, Family Car) : ").strip().title()

                carInfo = []
                # extending the list with all the new information.
                lines.extend((name, price, horsepower, engineType, bodyType, carType))
                print("The car will be delivered to the dealership soon. ")
                # increasing the number of cars.
                self.__dealership.increaseNumCars()

                # writing this information to the text file.
                f = open("cars.txt", 'w')
                f.truncate(0)

                for info in lines:
                    f.write(info)
                    f.write('\n')
                break




    def removeCar(self):

        # opening file
        f = open("cars.txt", 'r+')
        # getting the name of the car that will be removed.
        lines = [line.rstrip('\n') for line in f]
        f.close()

        # validating that the car entered exists in the dealership
        repeat = True
        while repeat == True:
            name = input("Enter the name of car you would like to remove or press 3 to exit: ")

            # Honda Civic cannot be removed as it is the default car for the prediction algorithm.
            if name == "Honda Civic":
                print("That car cannot be removed. It is the owners favourite. ")
                repeat = True


            elif name in lines:
                break

            elif name == '3':
                break

            else:
                print("That car isn't in the dealership, please try again. ")
                repeat = True

        # for loop that deletes the car from the car list.
        for i in range(len(lines)):

            line = lines[i]

            if line == name:

                del lines[i:i+6]
                break

        # deleting the text file and rewriting it without the car that wants to be removed.
        f = open('cars.txt', 'w')

        f.truncate(0)

        for line in lines:

            f.write(line)
            f.write('\n')

        # reducing the number of cars in the dealership.
        self.__dealership.reduceNumCars()



    def removeMember(self):
        # method that deletes a member.
        f = open('userInfo.txt', 'r')
        lines = [line.rstrip('\n') for line in f]
        f.close()

        # data validation
        repeat = True
        while repeat == True:

            name = input("Enter the username of member you would like to remove: ")

            if name in lines:
                break
            else:
                print("That username doesn't exist, please try again")
                repeat = True

        # deleting the lines that are associated with a specific customer.
        for i in range(len(lines)):
            line = lines[i]

            if line == name:

                del lines[i-2:i+7]
                break

        print("Deleted. This members funds will be automatically deposited into thier bank account. ")
        # deleting the text file.
        f = open('userInfo.txt' , 'w')
        f.truncate(0)
        # reducing the number of customers.
        self.__numCustomers -= 1

        #re-writing the text file, without that specific customer.
        for line in lines:

            f.write(line)
            f.write('\n')


    def displayStatistics(self):

        # printing the dealership statistics using a separate text file.
        f = open('dealershipStatistics.txt', 'r')
        lines = [line.rstrip('\n') for line in f]

        # getting the info from the text file list.
        numCustomers = lines[0]
        numCars = lines[1]
        numSales = lines[2]
        numExecutiveCustomers = lines[3]

        return """
        Total Customers: {}
        Total Cars: {}
        Total Sales: {}
        Total Executive Members: {}""".format(numCustomers, numCars, numSales, numExecutiveCustomers)


    def upgradeMember(self):

        # this method changes the status of the member in the text file.
        f = open("userInfo.txt" , "r")
        lines = [line.rstrip('\n') for line in f]
        f.close()

        # data validation.
        repeat = True
        while repeat == True:
            userName = input("Enter the username of the customer you would like to upgrade or press (1) to exit: ")

            if userName not in lines and userName != '1':

                print("That username doesn't exist, please enter a valid one. ")

            elif userName == '1':
                break

            else:
                break

        # finding the index of the username in the text file, and updating the membership status to executive member.
        # also changes the discount amount to 5, which is the preset discount amount for executives.
        for i in range(len(lines)):

            line = lines[i]

            if line == userName:

                lines[i+2] = "Executive Member"
                lines[i+5] = '5'


        f = open("userInfo.txt" , 'w')
        f.truncate(0)

        # re-writing the text file.
        for line in lines:

            f.write(line)
            f.write('\n')
