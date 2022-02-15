# Name: Dhruv Patel, Haran M.
# Date: Dec 16th, 2021
# Car Dealership

from car import Car
from admin import Admin
class Dealership:

    def __init__(self, userInfoFile, carsFile, numCars):

        self.__userInfoFile = userInfoFile
        self.__carsFile = carsFile
        self.__carInfoList = []
        self.__numCars = numCars
        self.__carsList = []
        self.__numSales = None

    # getters and setters
    def getUserInfoFile(self):
        return self.__userInfoFile

    def getCarFile(self):
        return self.__carsFile

    def getCarInfoList(self):
        return self.__carInfoList

    def getNumCars(self):
        return self.__numCars

    def getCarsList(self):
        return self.__carsList

    def getNumSales(self):
        return self.__numSales

    def setUserInfoFile(self, newFile):
        self.__userInfoFile = newFile

    def setCarsFile(self, newFile):
        self.__carsFile = newFile

    def setCarInfoList(self, newList):
        self.__carInfoList = newList

    def setCarsList(self, newList):
        self.__carsList = newList

    def changeNumSales(self, int):
        self.__numSales = int

    def setNumSales(self):

        f = open('dealershipStatistics.txt', 'r')
        lines = [line.rstrip('\n') for line in f]

        self.__numSales = int(lines[2])

    def increaseNumSales(self):
        self.__numSales += 1

    def reduceNumCars(self):
        # method that reduces the number of cars in the dealership by 1.
        self.__numCars -= 1

    def increaseNumCars(self):

        self.__numCars += 1

    def createCarsInfoList(self):
        # opening the textfile.
        f = open('cars.txt', 'r')

        carInfo = [line.rstrip('\n') for line in f]

        carInfoLists = []
        # appending all the information about each car to sublists, which get appended to a list of all the information about the cars.
        names = carInfo[0::6]
        carInfoLists.append(names)

        prices = carInfo[1::6]
        carInfoLists.append(prices)

        horsepowers = carInfo[2::6]
        carInfoLists.append(horsepowers)

        engineTypes = carInfo[3::6]
        carInfoLists.append(engineTypes)

        bodyTypes = carInfo[4::6]
        carInfoLists.append(bodyTypes)

        carTypes = carInfo[5::6]
        carInfoLists.append(carTypes)

        self.__carInfoList = carInfoLists

        return carInfoLists


    def createCars(self):
        # method that cretes the cars.
        carInfoLists = self.__carInfoList
        carsLists = []
        # loop that runs the amount of cars there are.
        for i in range(self.__numCars):
            # taking the values from each sublist.
            name = carInfoLists[0][i]
            price = carInfoLists[1][i]
            horsepower = carInfoLists[2][i]
            engineType = carInfoLists[3][i]
            bodyType = carInfoLists[4][i]
            carType = carInfoLists[5][i]
            # creating a car object using those vales.
            c = Car(name, price,horsepower, engineType, bodyType, carType )
            # appending the car to a list of cars.
            carsLists.append(c)

        self.__carsList = carsLists
        return carsLists


    def createCarsListByCarType(self, type):

        carsLists = self.__carsList
        carListByCarType = []
        # for each car in the car list, we get the car type.
        for car in carsLists:

            carType = car.getCarType()

            if carType == type:
                # if the type is the type that the user inputted, then the car is appended to a separate list containing these cars.
                carListByCarType.append(car)


        return carListByCarType

    def createCarsListByBodyType(self, type):
        # creating a car list by body type.
        carsLists = self.__carsList
        carsListByBodyType = []

        for car in carsLists:
            # getting the body type for each car in the car list.
            bodyType = car.getBodyType()

            if bodyType == type:
                # appending the car to a separate list if the body type matches.
                carsListByBodyType.append(car)

        return carsListByBodyType


    def createSimilarCarsList(self, horsepower, carPurchased):

        upperBound = horsepower + 50
        lowerBound = horsepower - 50
        otherCar = carPurchased.getName()
        similarCarList = []
        defaultCar = []

        for car in self.__carsList:

            if car.getName() == 'Honda Civic':

                defaultCar.append(car)
                break


        for car in self.__carsList:

            hp = car.getHorsepower()

            if hp >= lowerBound and hp < upperBound:

                if car.getName() != otherCar:
                    similarCarList.append(car)



        if len(similarCarList) == 0:

            return defaultCar

        else:

            return similarCarList


    def mergeSorting(self, arr):
    # soring algorithm
        def mergeSort(arr):
            # the algo should only do something if the length of the array is greater than 1:

            if len(arr) > 1:
                # defining the two parts of the array.
                # left arr is the start to middle
                # right arr goes from middle to end.
                leftArr = arr[:len(arr) // 2]
                rightArr = arr[len(arr) // 2:]

                # calling merge sort recursively
                mergeSort(leftArr)
                mergeSort(rightArr)

                # implementing the merge step:

                # using i to keep track of the left most element of the left array
                # using j to keep track of the left most element in the right array.
                # using k to keep track of the index in the merged array.
                i = 0
                j = 0
                k = 0
                while i < len(leftArr) and j < len(rightArr):

                    if leftArr[i] < rightArr[j]:
                        # whenever the value of left arr at index i is less than the right arr, the value will be saved in
                        # the regular arr at index k.
                        arr[k] = leftArr[i]
                        i += 1

                    else:
                        # if right arr is smaller than the current arr.
                        arr[k] = rightArr[j]
                        j += 1
                    # incrementing k by one.
                    k += 1

                # transferring every element from the left arr without considering right arr.
                while i < len(leftArr):
                    arr[k] = leftArr[i]
                    i += 1
                    k += 1

                # transferring every element from the right arr without considering left arr.
                while j < len(rightArr):
                    arr[k] = rightArr[j]
                    j += 1
                    k += 1


        mergeSort(arr)

        return arr

    def rateCar(self, car, account):

        f = open('ratings.txt', 'a')
        # getting all the information for the rating.
        rating = []
        name = car.getName().title()
        username = account.getUsername()
        numericalRating = input("Rate the car from 1 to 5 stars: ")
        writtenRating = input("Enter your thoughts about the car: ")

        # getting the rating into a list.
        rating.extend([name, username, numericalRating, writtenRating])

        for lines in rating:
            # appending the rating to the ratings text file.
            f.write(lines)
            f.write('\n')


        f.close()


    def viewRatings(self, name):

        f = open('ratings.txt', 'r')
        ratingList = []
        numericalRatingList = []
        allInfo = []
        i = 0
        lines = [line.rstrip('\n') for line in f]
        # for all the lines in the ratings list, we search for the line that matches the name we are searching for.
        for line in lines:
            i += 1

            if name == line:
                # if the name of the car matches, we take the values from one left of i, to 3 right of i.
                ratingList.append(lines[i - 1:i + 3])
                # we also take the numerical rating in a separate list.
                numericalRatingList.append(lines[i+1])

        # appeding these lists to another list called all info, which is used in the main file to print out the ratings.
        allInfo.append(ratingList)
        allInfo.append(numericalRatingList)

        return allInfo



    def purchaseCar(self, customer):

        # base rate is lowest rate that the dealership would charge.
        # based on factors, there would be a multiplier that would increased the final interest rate
        # these factors would be length of loan, credit score, and downpayment size.
        # these factors would be defined in a dictionary.
        # the keys would be the factors and the values would be the multipliers

        carRepeat = True
        carNames = []
        discountAmount = customer.getDiscountAmmount()
        for car in self.__carsList:
            carNames.append(car.getName())

        # data validation.
        while carRepeat == True:

            carName = input("Which car would you like to purchase: ").strip()

            if carName not in carNames:

                print("That car doesn't exist, please try again. ")
                carRepeat = True

            else:
                index = carNames.index(carName)
                break

        baseRate = 0.99
        loanLength = {12: 1.25, 24: 1.25, 36: 1.5, 48: 1.5, 60: 1.75}
        creditScores = {400: 3, 500: 2.5, 600: 1.5, 700: 1.25, 750: 1}
        downpayment = {10: 1.8, 20: 1.5, 30: 1.3, 40: 1.2, 50: 1}

        creditScore = customer.getCreditScore()
        # data validation
        repeat = True
        while repeat == True:

            purchaseCash = int(input("Would you like to purchase this car cash (1) , or finance (2): "))

            if purchaseCash == 1:
                break

            elif purchaseCash == 2 and creditScore > 400:
                break

            elif purchaseCash == 2 and creditScore < 400:

                print("Your credit score is too low to finance, you must purchase cash.")
                purchaseCash = 1
                break

            else:
                print("That isn't a valid input, please try again. ")
                repeat = True


        # if user wants to purchase cash, then an interest rate will not be calculated.
        if purchaseCash == 1:

            financing = False
            rate = 0
            downpaymentPercentage = 100
            vehicle = self.__carsList[index]

            return rate, downpaymentPercentage, vehicle, discountAmount

        else:
            financing = True

        # calculating the interest rate.
        loanTermRepeat = True

        while financing == True and creditScore >= 400:

            while loanTermRepeat == True:
                # second loop to ensure that the user selects an option that is in the dictionary
                print("""
    Select the loan length that you would like: 
    1. 12 Months 
    2. 24 Months 
    3. 36 Months 
    4. 48 Months 
    5. 60 Months""")

                loanLengthChoice = int(input("Enter the number of months: "))

                if loanLengthChoice in loanLength.keys():
                    # getting the multiplier from the dictionary and multiplying it to the base rate.
                    lengthMultipler = loanLength[loanLengthChoice]
                    baseRate *= lengthMultipler
                    break

                else:
                    print("That wasn't an option, please try again")


            scoreList = []
            for score in creditScores:
            # appending all the credit scores into a score list.
                scoreList.append(score)


            for i in range(1,len(scoreList)):
                # since credits scores arent a set number, an upper and lower bound is created.
                lowerScore = scoreList[i-1]
                higherScore = scoreList[i]

                # if the user's credit score is above 750, they get the best rate.
                if creditScore >= 750:
                    rateScore = 750

                # otherwise, they get the rate associated with the lower boundary.
                elif (creditScore >= lowerScore) and (creditScore < higherScore):
                    rateScore = lowerScore



            # getting the rate multiplier:
            creditMultiplier = creditScores[rateScore]
            # multiplying the base rate.
            baseRate *= creditMultiplier

            # calculating the downpayment multiplier
            # data validation
            downPaymentRepeat = True
            while downPaymentRepeat == True:
                downPaymentPercentage = float(input("How much would you like to put down (%): "))

                if downPaymentPercentage > 100 or downPaymentPercentage < 0:

                    print("That isn't valid, please try again! ")
                    downPaymentRepeat = True

                else:
                    break

            downpaymentList = []

            for amount in downpayment:
                # getting the downpayment amounts from the dictionary.
                downpaymentList.append(amount)

            for i in range(1, len(downpaymentList)):
                # creating upper and lower boundaries just like the credit score multiplier.
                lowerAmount = downpaymentList[i-1]
                higherAmount = downpaymentList[i]

                if downPaymentPercentage <= 10:
                    # if a user wants to put less than 10% down, they get the same rate as putting 10% down.
                    downPaymentAmount = 10

                elif downPaymentPercentage > lowerAmount and downPaymentPercentage <= higherAmount:
                    # otherwise they get the rate associated with the lower boundary.
                    downPaymentAmount = lowerAmount

            # multiplying the base rate.
            downPaymentMultiplier = downpayment[downPaymentAmount]
            baseRate *= downPaymentMultiplier

            break
        # getting the vehicle from the cars list using the index.
        vehicle = self.__carsList[index]

        # returning the interest rate, down payment percentage, vehicle, and the discount amount.
        print("Your interest rate is {:.2f}%".format(baseRate))
        return baseRate, downPaymentPercentage, vehicle, discountAmount

