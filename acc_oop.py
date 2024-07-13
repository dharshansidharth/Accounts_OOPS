class noAccount(Exception):
    pass

from accounts import *


def bank():
    normal_acc_holders = []
    interest_acc_holders = []
    savings_acc_holders = []

    opt = int(input("Enter :\n 1.Normal Account\n2.Interest Account\n3.Savings Acccount\n0.Exit"))

    def normal_account():
        flag1 = 0 
        flag2 = 0
        print('\nYou chose a normal bank account!\n')
        while True:
            choice1 = int(input('Enter :\n1.Create Account\n2.Deposit\n3.Withdraw\n4.Transaction\n'))
            if choice1 == 1:
                user1 = str(input('\nEnter user name:'))
                dep1 = int(input('\nEnter Initial amount:'))
                acc1 = bankAccounts(user1 , dep1)
                normal_acc_holders.append(acc1)

            elif choice1 == 2:
                flag_ = 0
                g_name1 = str(input('Enter account name to deposit:'))
                for i in normal_acc_holders:
                    if i.get_name() == g_name1:
                        index = normal_acc_holders.index(i)
                        flag_ = 1
                        break
                    else:
                        flag_ = 0

                if flag_:
                    g_name1 = normal_acc_holders.pop(index)
                    amt1 = int(input('Enter amount to deposit:'))
                    g_name1.deposit(amt1)
                    normal_acc_holders.append(g_name1)
                else:
                    print('No such account exist!')

            elif choice1 == 3:
                w_name1 = str(input('Enter account name to withdraw:'))
                for i in normal_acc_holders:
                    if i.get_name() == w_name1:
                        flag = 1
                        w_name1 = normal_acc_holders.pop(normal_acc_holders.index(i))
                        amt2 = int(input('Enter amount to withdraw:'))
                        w_name1.withdraw(amt2)
                        normal_acc_holders.append(w_name1)
                        break
                    else:
                        flag = 0
                print('No such account exists') if flag == 0 else print()

            elif choice1 == 4:
                flag1 = 0 
                flag2 = 0
                src1 = str(input('Enter source account name:'))
                dest1 = str(input('Enter reciver account name:'))
                for i in normal_acc_holders:
                    if i.get_name() == src1:
                        flag1 = 1
                        src1 = normal_acc_holders.pop(normal_acc_holders.index(i))
                for j in normal_acc_holders:
                    if j.get_name() == dest1:
                        dest1 = normal_acc_holders.pop(normal_acc_holders.index(j))
                        flag2 = 1
                if flag1 & flag2:
                    amt3 = int(input(f'Enter amount to transfer from {src1.get_name()} to {dest1.get_name()}:'))
                    src1.transfer(amt3 , dest1)
                if choice1 == 0:
                    break
                else:
                    return normal_account()
                
            
    def interest_account():
        print("\nYou chose an Interest Account!\n")
        while True:
            choice2 = int(input('Enter :\n1.Create Account\n2.Deposit\n3.Withdraw\n4.Transaction\n0.Exit'))

            if choice2 == 1:
                user1 = str(input('\nEnter user name:'))
                dep1 = int(input('\nEnter Initial amount:'))
                acc1 = interestAccount(user1 , dep1)
                interest_acc_holders.append(acc1)


            elif choice2 == 2:
                flag_ = 0
                g_name1 = str(input('Enter account name to deposit:'))
                for i in interest_acc_holders:
                    if i.get_name() == g_name1:
                        index = interest_acc_holders.index(i)
                        flag_ = 1
                        break
                    else:
                        flag_ = 0

                if flag_:
                    g_name1 = interest_acc_holders.pop(index)
                    amt1 = int(input('Enter amount to deposit:'))
                    g_name1.deposit(amt1)
                    interest_acc_holders.append(g_name1)
                else:
                    print('No such account exist!')

            elif choice2 == 3:
                w_name1 = str(input('Enter account name to withdraw:'))
                for i in interest_acc_holders:
                    if i.get_name() == w_name1:
                        flag = 1
                        w_name1 = interest_acc_holders.pop(interest_acc_holders.index(i))
                        amt2 = int(input('Enter amount to withdraw:'))
                        w_name1.withdraw(amt2)
                        interest_acc_holders.append(w_name1)
                        break
                    else:
                        flag = 0
                print('No such account exists') if flag == 0 else print()


            elif choice2 == 4:
                src1 = str(input('Enter source account name:'))
                dest1 = str(input('Enter reciver account name:'))
                for i in interest_acc_holders:
                    if i.get_name() == src1:
                        flag1 = 1
                        src1 = interest_acc_holders.pop(interest_acc_holders.index(i))
                for j in interest_acc_holders:
                    if j.get_name() == dest1:
                        dest1 = interest_acc_holders.pop(interest_acc_holders.index(j))
                        flag2 = 1
                if flag1 & flag2:
                    amt3 = int(input(f'Enter amount to transfer from {src1.get_name()} to {dest1.get_name()}:'))
                    src1.transfer(amt3 , dest1)
            if choice2 == 0:
                break
            else:
                return interest_account()
        

    def savings_account():
        print("\nYou chose an Savings Account!\n")
        while True:
            choice3 = int(input('Enter :\n1.Create Account\n2.Deposit\n3.Withdraw\n4.Transaction\n0.Exit'))

            if choice3 == 1:
                user1 = str(input('\nEnter user name:'))
                dep1 = int(input('\nEnter Initial amount:'))
                acc1 = savingsAccount(user1 , dep1)
                savings_acc_holders.append(acc1)

            elif choice3 == 2:
                flag_ = 0
                g_name1 = str(input('Enter account name to deposit:'))
                for i in savings_acc_holders:
                    if i.get_name() == g_name1:
                        index = savings_acc_holders.index(i)
                        flag_ = 1
                        break
                    else:
                        flag_ = 0

                if flag_:
                    g_name1 = savings_acc_holders.pop(index)
                    amt1 = int(input('Enter amount to deposit:'))
                    g_name1.deposit(amt1)
                    savings_acc_holders.append(g_name1)
                else:
                    print('No such account exist!')

            elif choice3 == 3:
                w_name1 = str(input('Enter account name to withdraw:'))
                for i in savings_acc_holders:
                    if i.get_name() == w_name1:
                        flag = 1
                        w_name1 = savings_acc_holders.pop(savings_acc_holders.index(i))
                        amt2 = int(input('Enter amount to withdraw:'))
                        w_name1.withdraw(amt2)
                        savings_acc_holders.append(w_name1)
                        break
                    else:
                        flag = 0
                print('No such account exists') if flag == 0 else print()

                
            elif choice3 == 4:
                src1 = str(input('Enter source account name:'))
                dest1 = str(input('Enter reciver account name:'))
                for i in savings_acc_holders:
                    if i.get_name() == src1:
                        flag1 = 1
                        src1 = savings_acc_holders.pop(savings_acc_holders.index(i))
                for j in savings_acc_holders:
                    if j.get_name() == dest1:
                        dest1 = savings_acc_holders.pop(savings_acc_holders.index(j))
                        flag2 = 1
                if flag1 & flag2:
                    amt3 = int(input(f'Enter amount to transfer from {src1.get_name()} to {dest1.get_name()}:'))
                    src1.transfer(amt3 , dest1)
            if choice3 == 0:
                break
            else:
                return savings_account()
    if opt == 1:
        return normal_account
    elif opt == 2:
        return interest_account
    elif opt == 3:
        return savings_account
    else:
        return

while True:
    ans = bank()
    ans()