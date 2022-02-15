# Dhruv Patel, Haran M.
# Dec 17th, 2021
# Main Class

from admin import Admin
from dealership import Dealership
from menu import Menu

# opening database files
userInfoFile = open('userInfo.txt', 'r+')
carInfoFile = open('cars.txt', 'r+')

# getting number of lines in the userInfoFile to count the number of customers.
line_count = 0
for line in userInfoFile:
    if line != "\n":
        line_count += 1

numCustomers = int(line_count/9)

line_count2 = 0
for line in carInfoFile:
    if line != '\n':
        line_count2 += 1

numCars = int(line_count2/6)

# creating dealership.
dealership = Dealership(userInfoFile, carInfoFile, numCars)
dealership.setNumSales()
# creating admin object.
admin1 = Admin(userInfoFile,carInfoFile,numCustomers,dealership)

# creating pre-existing customers.
userInfoLists = admin1.createUserInfoLists()
customers = admin1.createCustomersList()

repeat = True
print("""

 _       __     __                             __           __  __                      _          ___         __            
| |     / /__  / /________  ____ ___  ___     / /_____     / / / /___ __________ _____ ( )_____   /   | __  __/ /_____  _____
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \   / /_/ / __ `/ ___/ __ `/ __ \|// ___/  / /| |/ / / / __/ __ \/ ___/
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /  / __  / /_/ / /  / /_/ / / / / (__  )  / ___ / /_/ / /_/ /_/ (__  ) 
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/  /_/ /_/\__,_/_/   \__,_/_/ /_/ /____/  /_/  |_\__,_/\__/\____/____/  
                                                                                                                             
""")
# login loop.
loggedIn = False
adminLogin = False
while repeat == True:

    newOrOld = int(input("Press 1 if you are a new customer or 2 if your are returning or 3 to login as the admin: "))

    if newOrOld == 1:
        # method for creating a new customer.
        customer = admin1.createNewCustomer()
        c = customer
        userInfoLists = admin1.createUserInfoLists()
        customers = admin1.createCustomersList()
        loggedIn = True
        break


    elif newOrOld == 2:
        # logging in as a returning customer.
        # info returns a username, or none.
        # if none is returned, then we know that the user is locked out, so they will not be shown the car dealership.
        info = admin1.login()

        if info == None:
            loggedIn = False

        for customer in customers:
            # checks all the usernames in the customer list.
            username = customer.getUsername()
            # if the username matches, then user is logged in.
            if username == info:

                c = customer
                loggedIn = True
                print("Successful")
        break

    elif newOrOld == 3:
        # in the case that the admin is trying to log in.

        info = admin1.login()
        # checking for admin being locked out.
        if info == None:

            loggedIn = False
        # if the username matches, then the admin menu is run.
        elif info == 'admin1':
            # this boolean allows the program to run a separate admin menu.
            adminLogin = True
            loggedIn = False
            print("Successful")
            break

        else:
            # in the case that a user tries to log in through the admin page.
            print("That is a user login, please select returning customer on the login page. ")
        break




    else:
        print("Thats not a valid option. Try again. ")
        repeat = True

# once the customer has succesfully logged into the car dealership

# creating the cars.
carsInfoList = dealership.createCarsInfoList()
carsList = dealership.createCars()
# creating the menu.
menu = Menu(userInfoFile,carInfoFile,carsList,customers, dealership, admin1)
menu.updateDealershipStatistics()

try:
    # setting the customer in the menu.
    menu.setCustomer(c)

except:

    pass


menuRepeat = True

while menuRepeat == True and loggedIn == True:
    # customer menu.
    print(menu.displayMenu())
    # customer input.
    userInput = int(input("Select an option: "))


    if userInput == 1:
        # displaying cars method.
        cars = menu.displayCars()

        for car in cars:
            # printing all the cars.
            print(car.toString())

        menu.actionMenu()

    elif userInput == 2:
        # displaying the cars by car type.
        carListByType = menu.displayCarsByCarType()

        for car in carListByType:
            # printing the cars.
            print(car.toString())

        menu.actionMenu()

    elif userInput == 3:
        # method that allows the user to display the cars by body type.
        carListByBodyType, carType = menu.displayCarsByBodyType()

        for car in carListByBodyType:
            # printing.
            print(car.toString())

        menu.actionMenu()


    elif userInput == 4:
        # displaying the cars by price.
        carsList = menu.displayCarsByPrice()

        for car in carsList:

            print(car.toString())

        menu.actionMenu()

    elif userInput == 5:
        # displaying the cars by horsepower.
        carsList = menu.displayCarsByHorsepower()

        for car in carsList:

            print(car.toString())

        menu.actionMenu()

    elif userInput == 6:
        # method that allows the user to add funds to the account.
        c.addFunds()

    elif userInput == 7:
        # method that allows the user to edit previous ratings.
        print(menu.editPreviousRatings(c))

    elif userInput == 8:
        # method that allows an executive member to enter a draw.
        # runs if the membership type of the customer is an executive member.
        if c.getMembershipType() == "Executive Member":

            c.draw()

        else:

            print("You aren't an executive member. Please seek the admin to be upgraded!")

    elif userInput == 9:
        # exit.
        print("Have a good day!")
        break

# menu options for the admin.

adminRepeat = True

while adminRepeat == True and adminLogin == True:
    # admin menu.
    # only runs if the user logged in is an admin.

    print(admin1.adminMenu())
    choice = int(input("Select an option: "))


    if choice == 1:
        # prints out all the customers.
        # creates a list of customers again in the case that any customers were upgraded to executives.
        userInfoLists = admin1.createUserInfoLists()
        customers = admin1.createCustomersList()

        for customer in customers:

            print(customer.toString())


    elif choice == 2:
        # prints out all the cars in the dealership.
        dealership.createCarsInfoList()
        cars = dealership.createCars()

        for car in cars:

            print(car.toString())

    elif choice == 3:
        # method to add a car to the dealership.
        admin1.addCar()
        menu.updateDealershipStatistics()

    elif choice == 4:
        # method to remove a car from the dealership.
        admin1.removeCar()
        menu.updateDealershipStatistics()

    elif choice == 5:
        # method that upgrades a member.
        admin1.upgradeMember()
        menu.updateDealershipStatistics()

    elif choice == 6:
        # method to remove a member from the dealership.
        admin1.removeMember()

    elif choice == 7:
        # displaying dealership statistics.
        print(admin1.displayStatistics())

    elif choice == 8:
        # exit
        print("Have a good day! ")
        break

