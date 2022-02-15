# Dhruv Patel, Haran M.
# Dec 31, 2021
# Menu

from dealership import Dealership
from car import Car

class Menu:

    def __init__(self, userInfo, carInfo, carsList, usersList, dealership, admin):

        self.__userInfo = userInfo
        self.__carInfo = carInfo
        self.__carsList = carsList
        self.__userList = usersList
        self.__dealership = dealership
        self.__customer = None
        self.__tempCarList = []
        self.__admin = admin

    #getters and setters
    def getUserInfo(self):
        return self.__userInfo

    def getCarInfo(self):
        return self.__carInfo

    def getCarsList(self):
        return self.__carsList

    def getUserList(self):
        return self.__userList

    def getDealership(self):
        return self.__dealership

    def getCustomer(self):
        return self.__customer

    def getTempCarList(self):
        return self.__tempCarList

    def getAdmin(self):
        return self.__admin

    def setUserInfo(self, newFile):
        self.__userInfo = newFile

    def setCarInfo(self, newFile):
        self.__carInfo = newFile

    def setCarsList(self, newList):
        self.__carInfo = newList

    def setUserList(self, newList):
        self.__userList = newList

    def setDealership(self, newDealership):
        self.__dealership = newDealership

    def setCustomer(self, customer):

        self.__customer = customer

    def setTempCarList(self, newList):
        self.__tempCarList = newList

    def setAdmin(self, newAdmin):
        self.__admin = newAdmin

    def displayMenu(self):

        return """
    Select an option to continue:
    1. View All Cars 
    2. View Cars By Car Type 
    3. View Cars by Body Type 
    4. Sort Cars by Price 
    5. Sort Cars by Horsepower 
    6. Add/Remove Funds to your account
    7. Edit previous car ratings
    8. Executive Member Draw
    9. Exit"""

    def displayCars(self):
        # cars list.
        carsList = []

        # for every car in the cars list, we are appending it to the cars list.
        for car in self.__carsList:

            carsList.append(car)

        return carsList

    def displayCarsByCarType(self):

        repeat = True
        # a list of car types.
        types = ['Sports Car', 'Family Car', 'Super Car']



        while repeat == True:
            print("""The following types of cars are availible: 
            1. Sports Car 
            2. Family Car
            3. Super Car""")
            # user inputs what kind of car they want to search by.
            carType = input('Select the body type that you want to view: ').title().strip()

            # if its not in the dealership, we would tell the user to search for a different type.
            if carType not in types:

                print("We don't carry that specificiation. Ensure you have spelt the type correctly, or email dhruv@haransautos.com to get it in stock!")

            else:
                # if it is, we would use the dealership method to create that cars list.
                carsList = self.__dealership.createCarsListByCarType(carType)
                break

        # setting a temporary list as that list.
        self.__tempCarList = carsList

        # returning the cars list.
        return carsList

    def rateCar(self):

        # creating a copy of the carsList from the previous method.
        if len(self.__tempCarList) == 0:
            ratingList = self.__carsList
            print(self.__carsList[0].getName())

        else:
            ratingList = self.__tempCarList.copy()

        # clearing the temporary list.
        self.__tempCarList.clear()
        nameList = []

        # getting a list of car names, for data validation.
        for car in ratingList:

            name = car.getName().title().strip()
            nameList.append(name)


        repeat = True
        while repeat == True:

            # user selects what car they would like to rate.
            vehicle = input("Which vehicle would you like to rate: ").strip().title()

            ratedBefore = self.checkIfRatedBefore(vehicle)

            if ratedBefore == True:
                print("You have already rated that car before! Please edit the rating instead. ")
                break


            # implement a system that tells the user if the car doesn't exist.
            for car in ratingList:
                name = car.getName().title().strip()
                # if the vehicle entered exists in the list of cars, then the dealership method of rating the car is invoked.
                if vehicle == name:
                    self.__dealership.rateCar(car, self.__customer)
                    break

                else: continue

            # if the vehicle the user entered doesn't exist, it tells the user to re-enter.
            if vehicle not in nameList:

                print("We don't carry that car in the dealership. Please re-enter which car you would like to rate. ")
                repeat = True

            else:
                break

    def viewRatings(self):

        # method that allows the user to view ratings.
        repeat = True
        carNames = []
        for car in self.__carsList:
            carNames.append(car.getName())

        # data validation.
        while repeat == True:
            vehicle = input("Which vehicle would you like to view the ratings for: ").title().strip()

            if vehicle not in carNames:

                print("That car doesn't exist in the dealership, please enter another one. ")

            else:
                break

        # getting the all the ratings of the car from the dealership object.
        allInfo = self.__dealership.viewRatings(vehicle)

        # making two separate lists for the numerical ratings and the written ratings.
        ratings = allInfo[0]
        numericalRatings = allInfo[1]

        #printing it.
        if len(ratings) > 0:
            for rating in ratings:
                print("""
                    Car: {}
                    Username: {}
                    Numerical Rating: {}
                    Written Rating: {}""".format(rating[0], rating[1], rating[2], rating[3]))

        total = 0
        counter = 0
        # calculating the average numerical rating.
        for num in numericalRatings:
            num = int(num)
            total += num
            counter += 1

        if counter > 0:

            averageRating = total / counter
            print("""The average numerical rating is {:.1f}""".format(averageRating))
            return averageRating

        else:
            print("This car doesn't have any ratings.")
            return 0



    def displayCarsByBodyType(self):
        # method that displays the cars by body type.
        repeat = True
        types = ['Sedan', 'Suv', 'Coupe']

        # printing the options, and data validation.
        while repeat == True:
            print("""The following types of cars are availible: 
                    1. Sedan 
                    2. Suv
                    3. Coupe""")


            carType = input('Select the body type that you want to view: ').title().strip()

            if carType not in types:

                print("We don't carry that specificiation. Ensure you have spelt the type correctly, or email dhruv@haransautos.com to get it in stock!")
            # creating a cars list by body type.
            else:
                carsList = self.__dealership.createCarsListByBodyType(carType)
                break
        # setting a temporary cars list as the cars list.
        self.__tempCarList = carsList

        # returning the cars list and the car type.
        return carsList, carType



    def displayCarsByHorsepower(self):
        # displaying the cars by horsepower.
        horsepowers = []
        cars = []

        for car in self.__carsList:

            # getting the horsepower and name for each car in the Cars List.
            # and appending it to two separate lists.
            horsepower = car.getHorsepower()
            horsepowers.append(horsepower)

            cars.append(car)

        # zipping the list to create a dictionary.
        # the key is the car
        # the item is the horsepower.

        zippedList = zip(cars,horsepowers)
        carDict = dict(zippedList)

        # sorting the horsepowers using a merge sorting algorithm.
        sortedHorsepowers = self.__dealership.mergeSorting(horsepowers)


        # iterating through the horsepower list to get the specific car that is associated with that horsepower.
        # get the key that is associated with the specific value in the dictionary.
        sortedCarsList = []

        for horsepower in sortedHorsepowers:

            for key, value in carDict.items():

                if horsepower == value:

                    sortedCarsList.append(key)

                else: continue

        # returning a list of sorted cars.
        return sortedCarsList



    def displayCarsByPrice(self):
        # displaying the cars by price.
        prices = []
        cars = []
        # getting the price of each car.
        for car in self.__carsList:

            price = car.getPrice()
            prices.append(int(price))

            cars.append(car)

        # zipping the cars and their prices to a dictionary.
        zippedList = zip(cars,prices)

        carDict = dict(zippedList)
        # using the merge sorting algorithm, to sort the prices.
        sortedPrices = self.__dealership.mergeSorting(prices)

        sortedCarsList = []
        # iterating through the sorted prices.
        for price in sortedPrices:
            # finding the car that matches the price.
            for key, value in carDict.items():

                if price == value:
                    # appending the car to the sorted cars list.
                    sortedCarsList.append(key)

                else:
                    continue
        # returning the sorted cars list.

        return sortedCarsList

    def editPreviousRatings(self, c):
        # method that allows the user to edit or delete previous ratings.
        f = open("ratings.txt", 'r')

        lines = [line.rstrip('\n') for line in f]
        f.close()

        username = c.getUsername()
        ratings = []

        for i in range(len(lines)):

            line = lines[i]

            if line == username:

                ratings.append([lines[i - 1], lines[i], lines[i + 1], lines[i + 2]])

        # if the user has no ratings
        if len(ratings) == 0:
            return "You do not have any ratings. "

        # printing out the ratings.
        for i in range(len(ratings)):

            print("""
                Rating Number: {}
                Car: {}
                Username: {}
                Numerical Rating: {}
                Written Rating: {}""".format(i+1,ratings[i][0], ratings[i][1], ratings[i][2], ratings[i][3]))

        # user input
        number = int(input("Enter the number of the rating you would like to change: "))
        choice = int(input("Would you like to edit this rating (1) or delete it (2): "))

        if choice == 1:

            # validating the input
            repeat = True
            while repeat == True:
                numericalRating = (input("Enter the new numerical rating: "))
                num = int(numericalRating)

                if num < 1 or num > 5:
                    print("Enter a value between 1 and 5: ")
                    continue

                else:
                    break

            writtenRating = input("Enter your new written rating: ")

            # changing the rating
            ratings[number - 1][2] = numericalRating
            ratings[number - 1][3] = writtenRating

            # flattening the 2-d list into a 1-d list.
            flattenedRatings = [j for sub in ratings for j in sub]

            # rewriting the text file with the new list.
            f = open('ratings.txt', 'w')
            f.truncate(0)
            f.close()

            g = open('ratings.txt', 'a')

            for line in flattenedRatings:
                g.write(line)
                g.write('\n')

            return 'Done!'

        # if the user wants to delete their rating instead.
        elif choice == 1:
            # deletes the sublist that contained that specific rating.
            del ratings[number-1]

            # rewriting the text file with the updated ratings.
            f = open('ratings.txt', 'w')
            f.truncate(0)

            flattenedRatings = [j for sub in ratings for j in sub]

            for line in flattenedRatings:

                f.write(line)
                f.write('\n')

            return 'Done!'



    def checkIfRatedBefore(self, carName):
        # method that checks if the user rated a car before.
        # getting the username of the customer.
        username = self.__customer.getName()
        f = open('ratings.txt', 'r+')

        lines = [line.rstrip('\n') for line in f]

        # iterating through all the ratings
        for i in range(len(lines)):

            line = lines[i]
            rater = lines[i+1]
            # if the user has rated that car before, return true, else false.
            if line == carName and rater == username:

                return True

            else:
                return False

    def purchaseCarMenu(self, c):

        dealership = self.__dealership
        # getting the information from the purchase car method.
        rate, downPaymentPercentage, vehicle, discountAmount = dealership.purchaseCar(c)
        # calculating the price, and the discount amount.
        discountAmount /= 100
        price = float(vehicle.getPrice()) * (1 - discountAmount)
        amountDown = (downPaymentPercentage / 100) * price

        if rate == 0:
            # in case teh user wants to purchase cash.
            print("Your total will be ${}.".format(amountDown))


        else:
            # user finances the car.
            print("You have to put ${:.2f} down and finance the rest at a rate of {:.2f}%".format(amountDown, rate))

        choice = int(input("Do you want to continue (1) Yes or (2) No: "))
        if choice == 1:
            # getting account balance.
            accountBalance = c.getAccountBalance()

            if accountBalance < amountDown:
                # in case the user doesn't have enough money to pay.
                print("You do not have enough money. Please add more funds and try again. ")

            else:
                # paying the amount due.
                c.reduceFunds(amountDown)
                print(
                    "Congratulations, you have purchased this car. It will be delivered to your house in 24 hours!")
                # getting horsepower for prediction algorith,
                horsepower = vehicle.getHorsepower()
                # increasing num sales and updating the dealership statistics.
                self.__dealership.increaseNumSales()
                self.updateDealershipStatistics()
                similarCars = dealership.createSimilarCarsList(horsepower, vehicle)

                # printing similar cars (prediction algorithm)
                print("Cars you may also like: ")
                for car in similarCars:
                    print(car.toString())

    def updateDealershipStatistics(self):

        # getting information from the dealership and admin objects.
        numCustomers = str(self.__admin.getNumCustomers())
        numExecs = str(self.__admin.getNumExecutives())
        numCars = str(self.__dealership.getNumCars())
        numSales = str(self.__dealership.getNumSales())

        # appending these values to a list.
        stats = [numCustomers,numCars, numSales, numExecs]

        f = open("dealershipStatistics.txt", 'r')
        info = [line.rstrip('\n') for line in f]
        f.close()

        for i in range(4):
            # getting the values in the text file.
            stat = stats[i]

            # if the text file value is different from the current value, it is updated.
            if stat != info[i]:
                info[i] = stat

        # rewriting the text file.
        f = open("dealershipStatistics.txt", 'w')
        f.truncate(0)

        for line in info:
            f.write(line)
            f.write('\n')

        f.close()

    def actionMenu(self):
        # action menu that allows for user options.
        ratingRepeat = True

        # code that allows the user to rate, view the ratings, or purchase the car.
        while ratingRepeat == True:
            nextStep = int(input(
                "Would you like to rate a car (1), view the ratings for a car (2), purchase a car (3) or exit (4): "))

            if nextStep == 1:
                # rating the car.
                self.rateCar()
                break

            elif nextStep == 2:
                # viewing ratings.
                averageRating = self.viewRatings()
                break

            elif nextStep == 3:
                # purchasing a car.
                self.purchaseCarMenu(self.__customer)
                break

            elif nextStep == 4:
                # exit.
                break

            else:
                # data validation.
                print("That wasn't a valid option. Please try again. ")
                continue
