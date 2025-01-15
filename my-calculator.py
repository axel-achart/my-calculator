# BONUS : Fonctionnalité historique à votre calculatrice
# Possibilité d'effacer et réinitialiser l'historique
# (Pas de base de donnée)


# Function to Choose operation
def choose_operation():
    while True:
        try:
            print ("""Available operations :
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Exponentiation (Power of a number)
    6 - Quotient
    7 - Remainder
    8 - Exit""")

            operation = int(input("\nEnter your choice : "))

            if 1 <= operation <= 7:
                return operation        # Save type operation
            elif operation == 8:
                print("Leaving the calculator...")
                print()
                exit()      # To exit the program
            else:
                print("\nPlease enter a number between 1-7")

        except ValueError:
                print("\nPlease enter a number")


# Function to ask 2 numbers
def ask_numbers():
    while True:
        try:
            first_number = float(input("\nEnter the first number : "))
            second_number = float(input("Enter the second number : "))
            numbers = first_number, second_number
            return numbers

        except ValueError:
            print("Please enter a valid number")


# Calculation functions
def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

def exponentiation(first_number, second_number):
    return first_number ** second_number

def quotient(first_number, second_number):
    return first_number // second_number

def remainder(first_number, second_number):
    return first_number % second_number


# Function History
def settings_hist(hist, result):
    # Increment and Show
    hist.append(result)
    show_hist = str(input("\nDo you want to show history ? (y/n) : "))
    if show_hist == 'y' or show_hist == 'yes':
        print("History :", hist)
    # Delete an Element
        remove = str(input("\nDo you want to remove an element from history ? (y/n) : "))
        if remove == 'y' or remove == 'yes':
            while True:
                try:
                    delete = int(input(f"History contain {len(hist)} element(s), Enter the index of your choice (between 0 - {len(hist)-1}) : "))
                    del hist[delete]
                    print("History update : ", hist)
                    break
                except ValueError:
                    print("\nPlease enter a valid number")
                except IndexError:
                    print("\nPlease enter a valid index")
        elif remove == 'n' or remove == 'no':
            print("\nNo items deleted")

    # Total Clear
        ask_clear = str(input("\nDo you want to clear history ? (y/n) : "))
        if ask_clear == 'y' or ask_clear == 'yes':
            hist = []
            print()
            print(f"History update : {hist}")
        elif ask_clear == 'n' or ask_clear == 'no':
            print("\nHistory not clear")

    return hist



# Menu 
def main(operation, numbers):

    hist = []

    while True:

        first_number, second_number  = numbers

        if first_number == int(first_number):       # verification if 1st numb is int
            first_number = int(first_number)

            if second_number == int(second_number):     # verification if 2nd numb is int
                second_number =  int(second_number)
            elif second_number == float(second_number):     # verification if 2nd numb is float
                second_number = float(second_number)

        elif first_number == float(first_number):       # verification if 1st numb is float
            first_number = float(first_number)

            if second_number == int(second_number):     # verification if 2nd numb is int
                second_number =  int(second_number)
            elif second_number == float(second_number):     # verification if 2nd numb is float
                second_number = float(second_number)
    

        operation = int(operation)      # operation --> int
        if operation == 1:
            print()
            result = addition(first_number, second_number)
            print(first_number, '+', second_number, '=', result)
            settings_hist(hist, result)
            break

        elif operation == 2:
            print()
            result = subtraction(first_number, second_number)
            print(first_number, '-', second_number, '=', result)
            settings_hist(hist, result)
            break
        
        elif operation == 3:
            print()
            result = multiplication(first_number, second_number)
            print(first_number, '*', second_number, '=', result)
            settings_hist(hist, result)
            break
        
        elif operation == 4:
            print()
            while second_number != 0:
                result = division(first_number, second_number)
                print(first_number, '/', second_number, '=', result)
                settings_hist(hist, result)
                break
            if second_number == 0:
                print("Impossible division with divider = 0, retry")
                break
        
        elif operation == 5:
            print()
            result = exponentiation(first_number, second_number)
            print(first_number, '**', second_number, '=', result)
            settings_hist(hist, result)
            break
        
        elif operation == 6:
            print()
            while second_number != 0:
                result = quotient(first_number, second_number)
                print(first_number, '//', second_number, '=', result)
                settings_hist(hist, result)
                break
            if second_number == 0:
                    print("Impossible division with divider = 0, retry")
                    break
        
        elif operation == 7:
            print()
            while second_number != 0:
                result = remainder(first_number, second_number)
                print(first_number, '%', second_number, '=', result)
                settings_hist(hist, result)
                break
            if second_number == 0:
                    print("Impossible division with divider = 0, retry")
                    break


# Function to show the menu and execute the program
def menu():
    while True:
        print("\n--- MENU ---")
        main(choose_operation(), ask_numbers())


# Program execute only by myself
if __name__ == "__main__":
    print("\nLaunching the calculator...")
    menu()