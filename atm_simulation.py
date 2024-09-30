def ATM():
    attempts = 3
    while attempts > 0:
        print("Enter password:", end=" ")
        user_password = input()
        if user_password == password[i]:
            print("\nLogin successful\n")
            menu()
            break
        else:
            attempts -= 1
            print("Incorrect password, " + str(attempts) + " attempts left")
            if attempts == 0:
                print("Account Blocked, please contact customer care for more assistance")


def menu():
    print("1. Withdraw      \t2. Deposit")
    print("3. Check balance \t4. Change password")
    print("Enter your choice:", end=" ")
    choice = int(input())
    
    while choice not in [1, 2, 3, 4]:
        print("Invalid choice. Re-enter your choice.")
        choice = int(input())
    
    if choice == 1:
        withdraw()
    elif choice == 2:
        deposit()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        change_password()


def account_type():
    print("\nSelect Account type:")
    print("1. Savings\t 2. Current")
    print("3. Overdraft\t 4. Cash credit")
    print("\nEnter your choice:", end=" ")
    acc = int(input())
    return acc


def withdraw():
    account_type()
    amount = int(input("Enter the amount you want to withdraw: "))
    print("Enter the PIN:", end=" ")
    
    if pin_check():
        print("")
    else:
        if amount <= bal[i]:
            print("Collect your cash\nThanks for visiting")
            bal[i] -= amount
            print("Available Balance:", bal[i])
        else:
            print("Insufficient Balance")
            print("Press 1 to check the balance")
            print("Press 2 to exit")
            cb = int(input())
            if cb == 1:
                check_balance()
            else:
                print("End")


def deposit():
    account_type()
    amount = int(input("Enter the amount you want to deposit: "))
    print("Enter the PIN:", end=" ")
    
    if pin_check():
        print("")
    else:
        print("Amount deposited successfully")
        bal[i] += amount
        print("Total Balance:", bal[i])


def pin_check():
    try:
        pin_code = int(input())
        if pin_code not in pin:
            print("Invalid PIN")
            return True
        return False
    except ValueError:
        print("INVALID PIN")
        return True


def check_balance():
    print("Enter the PIN to check balance:", end=" ")
    
    if pin_check():
        print("")
    else:
        print("Available Balance:", bal[i])


def change_password():
    print("Enter the current password:", end=" ")
    current_password = input()
    
    if current_password != password[i]:
        print("Invalid Password")
    else:
        new_password = input("Enter the new password: ")
        confirm_password = input("Confirm the new password: ")
        
        if new_password == confirm_password:
            password[i] = new_password
            print("Password changed successfully")
        else:
            print("Passwords do not match")


# User and account details
user = ['mohan', 'vinay', 'vishnu', 'diwakar', 'naresh']
password = ['m11', 'v05', 'v06', 'd00', 'n06']
pin = [1121, 1122, 1221, 1201, 1111]
bal = [10000, 12112, 212122, 200000, 200000]

print("Welcome to ATM")
us = input("Enter the Username: ")

if us not in user:
    print("Invalid username\nThanks for visiting")
else:
    i = user.index(us)
    ATM()
