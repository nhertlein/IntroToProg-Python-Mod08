# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# NHertlein,03.08.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""  # Captures the user option selection


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NHertlein,03.08.2021,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        # No need to be private, but good practice?
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)

    # -- Properties --
    @property  # Allows access to private attributes
    def product_name(self):
        return str(self.__product_name).title()

    @property  # allows access to private attributes
    def product_price(self):
        return float(self.__product_price)

    # -- Setters --
    @product_name.setter
    def product_name(self, name: str):
        self.__product_name = name

    @product_price.setter
    def product_price(self, price: float):
        self.__product_price = price

    # -- Methods --
    def __str__(self):
        return "The product name is: " + self.product_name + " and the cost is: $" + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NHertlein,03.08.2021,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """Saves a list of product names and prices to a file

        :param file_name: (string) with name of file to save data to
        :param list_of_product_objects: (list) of data to save to file
        :return: (list) of product objects
        """
        with open(file_name, 'w') as file:  # Automatically close
            for row in list_of_product_objects:
                file.write(row.product_name + "," + str(row.product_price) + "\n")
            return list_of_product_objects

    @staticmethod
    def read_data_from_file(file_name):
        """Reads all lines of file data from a file

        :param file_name: (string) with name of file to read
        :return: (list) of product objects
        """
        list_of_product_objects = []  # Create list to save to
        with open(file_name, 'r') as file:  # Automatically closes
            for line in file:
                name, cost = line.split(",")
                row = Product(name, cost)  # Save as object
                list_of_product_objects.append(row)
            return list_of_product_objects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Class of Input/Output functions to be used in the script

    methods:
        user_menu: Prints menu of options

        input_user_choice: Gets user choice

        display_current_data(list_of_product_objects): Prints current list objects

        add_product_data: -> Object populated with user entered data

    changeLog: (When,Who,What)
        NHertlein,03.08.2021, New code for Assignment 8
    """

    @staticmethod
    def user_menu():
        """ Prints a menu of selectable options in a menu format """
        print("""
        Menu of Options:
        1) Show Product Data
        2) Add a New Product
        3) Save Data to File
        4) Exit Program
        """)

    # TODO: Add code to get user's choice
    @staticmethod
    def input_user_choice():
        """ Gets the menu choice from a user

        :return: (string) number choice
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def display_current_data(list_of_product_objects: list):
        """ Displays data in the list

        :param list_of_product_objects:
        """
        print("******** Product List: ********")
        for row in list_of_product_objects:
            print(row.product_name + ", $" + str(row.product_price))
        print("*******************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def add_product_data():
        """ Enters user data into
        :return: (Object) Product object with user input
        """
        print("New Product Information")
        while True:  # Loop until a alphanumeric value is entered
            try:
                name = str(input("New product name: "))
                if not name.isnumeric():  # alpha numeric allowed
                    break
                else:
                    raise Exception("\nProduct names cannot be numbers")
            except Exception as e:
                print(e)
                print("Try again!\n")

        while True:  # Loop until a alphanumeric value is entered
            try:
                price = float(input("New product cost: "))
                break
            except ValueError as e:
                print("\n" + str(e))
                print("Try again!\n")

        new_row = Product(product_name=name, product_price=price)
        return new_row


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
except FileNotFoundError as e:
    print("\nExisting list not found")
    print("Continuing.....\n")
except Exception as e:
    print("Something went wrong loading the file")
    print(e, e.__doc__)

while True:
    # Show user a menu of options
    IO.user_menu()

    # Get user's menu option choice
    strChoice = IO.input_user_choice()

    if strChoice.strip() == "1":
        # Show user current data in the list of product objects
        if lstOfProductObjects:  # Only display if list is not empty
            IO.display_current_data(lstOfProductObjects)
        else:
            print("File is Empty, Nothing to display")
    elif strChoice.strip() == "2":
        # Let user add data to the list of product objects
        new_product = IO.add_product_data()
        lstOfProductObjects.append(new_product)
    elif strChoice.strip() == "3":
        # let user save current data to file
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
    elif strChoice.strip() == "4":
        # exit program
        print("the program will now exit")
        break

# Main Body of Script  ---------------------------------------------------- #
