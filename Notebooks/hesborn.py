def ATMCHECK(pin):
    acountbal = 50000
    choice = input("Please enter 'b' to check balance or 'w' to withdraw or 'd' to deposit: ")
    while choice != 'q':
        if choice.lower() in ('w','b','d'):
            if choice.lower() == 'b':
                print("Your balance is: %d" % acountbal)
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw or q to quit: ")
                print(choice.lower())
            elif choice.lower() == 'd':
                deposit = float(input('please enter the amount you want to deposit: '))
                acountbal = acountbal + deposit
                print(choice.lower())
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw or q to quit: ")
                print(choice.lower())
            else:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw <= acountbal:
                    print("here is your: %.2f" % withdraw)
                    acountbal = acountbal - withdraw
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw or q to quit: ")
                    #choice = 'q'
                else:
                    print("You have insufficient funds: %.2f" % acountbal)
        else:
            print('wrong choice')
            choice = input("Please enter 'b' to check balance or 'w' to withdraw: ")
            return acountbal

ATMCHECK(7878)