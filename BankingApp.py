count = 0
attempts = 4
transactions = []

print('Welcome to the bank. Please log in.')
print(f'You have {attempts} attempts.')

while count < attempts:
    username = input('\nEnter your username: ')
    password = input('Enter your password: ')

    STORED_USERNAME = 'user123'
    STORED_PASSWORD = 'pass123'

    if STORED_USERNAME == username and STORED_PASSWORD == password:
        print('\nLog in successful.')
        balance = 0
        while True:
            try:
                options = int(input('\nHow can we help you? \n*Choose your option by writing the number of the action: \n1. Deposit money \n2. Withdraw money \n3. Check the balance \n4. Show transaction history \n5. Log out: '))
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 5.')
                continue

            if options == 1:
                while True:
                    user_input = input('\nPlease enter the amount you want to deposit in €: ')
                    try:
                        user_input = float(user_input)
                        if user_input <= 0:
                            print('Deposit amount must be positive.')
                            continue
                    except:
                        print('\nWrong input. Please enter amount in €: ')
                        continue
                    else:
                        deposit_amount = balance + user_input
                        transactions.append(f'Deposited was {user_input} €')
                        balance = deposit_amount
                        break

            elif options == 2:
                while True:
                    user_input2 = input('\nPlease enter the amount you want to withdraw in €: ')
                    try:
                        user_input2 = float(user_input2)
                        if user_input2 < 0:
                            print('Withdrawal amount must be positive.')
                            continue
                    except:
                        print('Wrong input. Please enter amount in €: ')
                        continue
                    else:
                        if user_input2 <= balance:
                            withdraw_amount = balance - user_input2
                            transactions.append(f'Withdrawned was {user_input2} €')
                            balance = withdraw_amount
                            break
                        else:
                            print('The balance can not be negative. Withdrawal is not possible.')
                            continue

            elif options == 3:
                print(f'\nYour current balance is {balance} €')
            elif options == 4:
                if transactions:
                    print('\nTransaction history: ')
                    for transaction in transactions:
                        print(transaction)
                else:
                    print('\nThere are no transactions yet.')
            elif options == 5:
                print('\nYou logged out of the bank.')
                break
            else:
                print('Invalid input. Please choose an action from the list (1-5): ')

        if options == 5:
            break
    else:
        count = count + 1
        if count < attempts:
            print('\nIncorrect username or password. Please try again.')
            attempts_left = attempts - count
            print(f'You have {attempts_left} attempts left')
        else:
            print('\nYou dont have acces to this account.')
            break