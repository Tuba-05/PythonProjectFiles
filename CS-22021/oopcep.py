""" BANKING SYSTEM """

from abc import ABC, abstractmethod  # importing module for abstract method.
import re  # importing module for search expressions when creating password.
import random  # importing module to create a unique account number.
from datetime import datetime  # importing module to save timing details of transaction history.
import time  # importing module to stop the upcoming execution for some seconds.


def generate_account_number():
    """Generates a random 9-digit account number."""

    account_number = random.randint(100000000, 9999999999)  # creating a unique account number.
    return str(account_number)


class Bank:
    def init(self):
        """BANK INFO"""
        self.bank_code = 'my_bank555$'
        self.bank_name = 'MY-BANK'

    def get_bank_info(self):
        """The function prints bank info"""
        print(f'{self.bank_code}\n{self.bank_name}')


class User:
    def login_(self):
        """ The function allows choices like login account and create account."""

        time.sleep(1.5)
        print(f'log in or create account\n press 1 for log in and 2 for create account')
        choice = int(input('Enter your choice:'))  # taking choice for user: admin/customer

        time.sleep(1.5)
        if choice == 1:  # user Login account
            print(f"are you a customer or an Administrator?\nPress 1 for Administrator "
                  f"and 2 for customer.")
            login_choice = int(input('enter here:'))

            time.sleep(1.5)
            if login_choice == 1:  # Login user is Admin.
                admin = Administrator()  # creating object of admin class.
                admin.login()  # calling function of admin class to log in admin account.

                time.sleep(0.5)
                print('Do you want to see all the bank records?\n press "Y" if yes.')
                admin_ch = input('Admin, enter your choice:').upper()

                if admin_ch == 'Y':
                   admin.get_records()  # calling the function to print all the bank records.
                else:
                    time.sleep(0.5)
                    print('EXIT.')

            elif login_choice == 2:  # Login user is Customer.
                time.sleep(1.5)
                acc_type = int(input('1.Checking Account\n2.Saving Account\n'
                                     '3.LOAN\n4.Delete account\nEnter your account type number:'))
                if acc_type == 1:  # if log in user has checking account.
                    ch = CheckingAccount()  # creating object of checking account.
                    file_name = 'CheckingAccountRecords.txt'
                    ch.login(file_name)  # calling function to log in.
                    ch.set_credit_limit(500)
                    ch.set_overdraft_fee(10)

                    time.sleep(1.5)
                    print('Enter your choice:')
                    print('1. Deposit money in account.\n2. Withdraw money from account.'
                          '\n3. Display your account information.')
                    chk_acc_choice = input('Enter your choice:')  # taking choice for withdraw/deposit.

                    if chk_acc_choice == '1':  # if "checking account" user wants to deposit money.
                        ch.deposit_amount()  # calling function to deposit money.
                        ch.get_account_balance()  # calling function to print checking account balance.
                        obj_ = ch.transaction_history_()  # creating object of transaction history function.
                        ch = FileSaver()  # creating object to save transaction history.
                        ch.transaction_history(obj_)  # calling function to save transaction records.

                    elif chk_acc_choice == '2':  # if checking account user wants to withdraw money.
                        ch.withdraw_amount()  # calling function to withdraw money.
                        ch.get_account_balance()  # calling function to print checking account balance.
                        obj_ = ch.transaction_history_()  # creating object of transaction history function.
                        ch = FileSaver()  # creating object to save transaction history.
                        ch.transaction_history(obj_)  # calling function to save transaction records.

                    else:  # for invalid choice.
                        time.sleep(0.5)
                        print('Invalid choice.')
                        exit()

                    time.sleep(1.5)
                    print('Do you want to see your info.\nIf yes press "Y".')
                    acc_ch = input('Enter your choice:').upper()  # if "checking account" user wants to see his info.
                    if acc_ch == 'Y':
                        ch.get_account_info()  # calling function to print the customer's record.
                    else:
                        time.sleep(0.5)
                        print("EXIT.")

                elif acc_type == 2:  # if log in user has saving account.
                    sv = SavingAccount()  # creating object of saving account.
                    file_name = 'SavingAccountRecords.txt'
                    sv.login(file_name)  # calling function to log in.

                    time.sleep(1.5)
                    print('Enter your choice:\n1.Deposit money.\n2.Withdraw money.'
                          '\n3. Display your account information.')
                    sv_acc_choice = input('Enter your choice:')  # taking choice for withdraw/deposit.

                    if sv_acc_choice == '1':  # if saving account user wants to deposit money.
                        sv.deposit_amount()  # calling function to deposit money.
                        sv.get_account_balance()  # calling function to print saving account balance.
                        obj_ = sv.transaction_history_()  # creating object of transaction history function.
                        sv = FileSaver()  # creating object to save transaction history.
                        sv.transaction_history(obj_)  # calling function to save transaction records.

                    elif sv_acc_choice == '2':  # if saving account user wants to withdraw money.
                        sv.apply_interest()
                        sv.withdraw_amount()  # calling function to withdraw money.
                        sv.get_account_balance()  # calling function to print saving account balance.
                        obj_ = sv.transaction_history_()  # creating object of transaction history function.
                        sv = FileSaver()  # creating object to save transaction history.
                        sv.transaction_history(obj_)  # calling function to save transaction records.

                    else:
                        time.sleep(0.5)
                        print('Invalid choice.')

                    time.sleep(1.5)
                    print('Do you want to see your info.\nIf yes press "Y".')
                    sav_ch = input('Enter your choice:').upper()  # if "saving account" user wants to see his info.
                    if sav_ch == 'Y':
                        sv.get_account_info()  # calling function to print the customer's info.
                    else:
                        time.sleep(0.5)
                        print("EXIT.")

                elif acc_type == 3:  # if log in user has loan account.
                    ln = Loan()  # creating object of loan account.
                    file_name = 'LoanRecords.txt'
                    ln.login(file_name)  # calling function to log in.
                    ln.set_loan_rate()  # setting values of instance variables.
                    ln.debit_monthly_interest()  # paying debt.
                    ln.get_account_balance()  # getting loan balance.
                    obj_ = ln.transaction_history_()  # creating object of transaction history function.
                    ln = FileSaver()  # creating object to save transaction history.
                    ln.transaction_history(obj_)  # calling function to save transaction records.

                    time.sleep(1.5)
                    print('Do you want to see your account info?\n press "Y" for yes.')
                    ln_choice = input('Enter your choice:').upper()  # if "loan account" user wants to see his info.
                    if ln_choice == 'Y':
                        ln.get_account_info()  # calling function to print the customer's info.
                    else:
                        time.sleep(0.5)
                        print('EXIT.')

                elif acc_type == 4:  # if log in customer wants to delete his account.
                    customer = Customer()  # creating object of customer class.
                    customer.delete_account()  # calling function to delete accounts.

                else:  # if login customer put invalid choice or wants to exit
                    time.sleep(0.5)
                    print('Your choice is invalid.\nEXIT.')

        elif choice == 2:  # if customer wants to create new account
            time.sleep(1.5)
            print('Account type:\n1.Checking Account\n2.Saving Account\n*OR*\n3.Apply for loan')
            account_type = input('Enter your account type:')  # taking choice of user for new account.

            if account_type == '1':  # if user wants to create checking account.
                ch1 = CheckingAccount()  # creating object of checking account.
                ch1.info()  # calling function to create new checking account.
                ch1.new_account_deposit_amount()  # depositing new account.
                ch1.get_account_balance()  # calling function to print checking account balance.
                obj_ = ch1.transaction_history_()  # creating object of transaction history function.
                ch1 = FileSaver()  # creating object to save checking records.
                ch1.checking_account_records()  # saving new checking account records.
                ch1.transaction_history(obj_)  # calling function to save transaction records.

            elif account_type == '2':  # if user wants to create saving account.
                sv = SavingAccount()  # creating object of saving account.
                sv.info() # calling function to create new checking account.
                sv.new_account_deposit_amount()  # depositing new account.
                sv.get_account_balance()  # calling function to print saving account balance.
                obj_ = sv.transaction_history_()  # creating object of transaction history function.
                sv = FileSaver()  # creating object to save saving records.
                sv.saving_account_records()  # saving new saving account records.
                sv.transaction_history(obj_)  # calling function to save transaction records.

            elif account_type == '3':  # if user is applying for loan.
                ln = Loan()  # creating object of loan account.
                ln.info()  # calling function to create new checking account.
                ln.set_loan_info()  # setting values of instance variables.
                ln.set_loan_rate()  # taking loan details from user.
                ln.get_account_balance()  # calling function to print loan account balance.
                obj_ = ln.transaction_history_()  # creating object of transaction history function.
                ln = FileSaver()  # creating object to save loan records.
                ln.loan_records()  # saving new loan account records.
                ln.transaction_history(obj_)  # calling function to save transaction records.

            else:  # if user does not want to create account.
                time.sleep(0.5)
                print('Invalid Choice.\nEXIT.')

        else:  # if user choice is invalid
            time.sleep(0.5)
            print('Your choice is invalid.\n EXIT.')


class Customer:  # if user is customer.
    Customer_account_no = ''  # creating class variable.
    records = []  # creating class list.

    def info(self):
        """ The takes information about user customer who is creating new account."""

        time.sleep(1.5)
        # taking customer's: user_id, account_no and user_name.
        self.__customer_user_name = input('Enter yor name in letters:').lower()
        while not ('a' <= self.__customer_user_name <= 'z'):
            time.sleep(0.5)
            print("You entered an int instead of str.")
        else:
            Customer.records.append(self.__customer_user_name)

        time.sleep(1.5)
        m = 0  # taking customer's: password.
        while m == 0:
            self.__password = input("Enter password for your account:")
            if len(self.__password) >= 7 and re.match("^(?=.([a-z-A-Z])(?=.\d)(?=.*[@#$%^&+=]))", self.__password):
                time.sleep(0.5)
                print("INVALID")
            else:
                m += 1
                time.sleep(1.5)
                print("Password has been created")
                Customer.records.append(self.__password)
                break

        time.sleep(1.5)
        while True:  # taking customer's: email_id.
            self.__customer_email_id = input('Enter your gmail id :')

            if '@gmail.com' in self.__customer_email_id:
                Customer.records.append(self.__customer_email_id)
                break
            else:
                time.sleep(0.5)
                print('The e-mail id you entered is invalid.')

        time.sleep(1.5)
        while True:  # taking customer's: country code.
            try:
                self.__country_code = int(input('enter your country code in numbers:'))
                assert len(str(self.__country_code)) != 0 and 1 <= len(str(self.__country_code)) <= 3
            except ValueError:
                time.sleep(0.5)
                print("You country code should be in numbers 'xx' or 'x'.")
            except AssertionError:
                time.sleep(0.5)
                print("Your code length should in between 1 to 3.")
            else:
                Customer.records.append('+' + str(self.__country_code))
                break

        time.sleep(1.5)
        while True:  # taking customer's: phone number.
            try:
                self.phone_no = int(input('Enter your phone number:'))
                self.__customer_phone_no = str(self.__country_code) + str(self.phone_no)
                Customer.records.append(self.__customer_phone_no)
                break
            except ValueError:
                time.sleep(0.5)
                print("The value you have entered is not a number.")

        time.sleep(1.5)
        # taking customer's: address(area, city and country).
        print('Enter your correct address.\nIt must contain your area,city and country')
        while True:
            self.__country = input('enter your country name:').lower()
            if self.__country != (0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9) \
                    and (('a' <= self.__country <= 'z') or ('A' <= self.__country <= 'Z')):
                Customer.records.append(self.__country)
                break
            else:
                time.sleep(0.5)
                print("kindly enter your country.")

        time.sleep(1.5)
        city = input('Enter your city name:').lower()
        area = input('Enter your area name:').lower()

        while not ('a' <= city <= 'z') and not('a' <= area <= 'z'):
            time.sleep(0.5)
            print('Kindly enter your correct city and area.')
        else:
            self.__customer_address = self.__country + ',' + city + ',' + area
            Customer.records.append(self.__customer_address)

        time.sleep(1.5)
        while True:  # taking customer's: gender.
            print('choose Male or Female.')
            self.__gender = input("enter your gender: ").lower()
            if self.__gender == 'male' or self.__gender == 'female':
                Customer.records.append(self.__gender)
                break
            else:
                time.sleep(0.5)
                print('Kindly give appropriate answer.')

        class Error(Exception):  # taking customer's: age.
            pass

        try:
            time.sleep(1.5)
            age = float(input('enter your age:'))
            if age < 18:
                raise Error
            else:
                self.__customer_age = str(age) + ' yrs'
                Customer.records.append(self.__customer_age)
        except Error:
            time.sleep(0.5)
            print("You are under aged or minor.\nSo we can not open an account for you.")
            exit()
        except ValueError:
            time.sleep(0.5)
            print("The value you have entered is not an age.")
        Error()

        time.sleep(1.75)
        # if user succeed in creating account.
        print('You have successfully created an account.')
        self.__customer_account_no = generate_account_number()  # calling function for an account number.
        Customer.records.append(self.__customer_account_no)
        time.sleep(0.5)
        print('Your account number is', self.__customer_account_no)

    def login(self, file):
        """ The function works when user is loging his account,"""

        time.sleep(1.5)
        self.__customer_account_no = input('enter your account number:')
        self.bank_records_file = open(file, 'r+')
        self.file = self.bank_records_file.read()
        self.bank_records_file.seek(0)

        # searching customer's: user_id, account_no and password
        for records in self.bank_records_file:  # range = no. of lines
            for data in eval(records):
                if (eval(records)[-2]) == self.__customer_account_no:
                    time.sleep(1.75)
                    print('Successfully login.\n', records)
                    Customer.records = eval(records)
                    Customer.Customer_account_no = self.__customer_account_no
                    break  # to break the otherwise it will print records on the basis of no. of index of list

            # if these statements would inside in nested loop it will print multiple times
            if self.__customer_account_no not in self.file:  # if user enter invalid user id
                time.sleep(0.5)
                print('Invalid account number.')
                exit()

    def delete_account(self):
        """Delete the account and its records"""

        time.sleep(1.5)
        self.__customer_account_no = input('Enter your account number:')

        # Call the delete_customer_records method of FileSaver class
        file_saver = FileSaver()  # creating object of file saver class.
        file_saver.delete_customer_records(self.__customer_account_no)
        time.sleep(1.5)
        print('Your account and records have been deleted.')


class Administrator:  # if user is admin
    def login(self):
        """ The function takes about admin who is loging his account."""

        time.sleep(1.5)
        self.__administrator_user_id = input('Enter your id:')
        self.__administrator_user_name = input('Enter your name:')
        self.__administrator_password = input('Enter your account password:')

        # searching admin info.
        self.admin_file = open('Admin.txt', 'r+')
        a = self.admin_file.readline()
        b = self.admin_file.readline()
        self.admin_file.seek(0)

        # loging admin account.
        for records in self.admin_file:  # loop iterates 2 times.
            for item in eval(records):  # nested loop iterates 3 times.
                if (eval(records)[2]) == self.__administrator_password and \
                        (eval(records)[1]) == self.__administrator_user_name and \
                        (eval(records)[0]) == self.__administrator_user_id:
                    time.sleep(1.75)
                    print('Successfully login.')
                    break  # to break 3 times

                else:
                    print(end='')

            # if user enters something wrong.
            if (self.__administrator_user_id in b) and (self.__administrator_user_name in a):
                time.sleep(0.5)
                print('OOPs.\nYou entered something wrong plz try again.')
                exit()
            if (self.__administrator_user_id in a) and (self.__administrator_user_name in b):
                time.sleep(0.5)
                print('OOPs.\nYou entered something wrong plz try again.')
                exit()

    def get_records(self):
        """ The function prints all bank records."""

        self.bank_records_file1 = open('CheckingAccountRecords.txt', 'r').read()
        self.bank_records_file2 = open('SavingAccountRecords.txt', 'r').read()
        self.bank_records_file3 = open('LoanRecords.txt', 'r').read()
        self.bank_records_file4 = open('TransactionHistory.txt', 'r').read()

        time.sleep(1.5)
        print('Checking Account Records.')  # printing checking account records.
        for items in self.bank_records_file1:
            print(items, end='')
        print('')

        time.sleep(1.5)
        print('Saving Account Records.')  # printing saving account records.
        for items in self.bank_records_file2:
            print(items, end='')
        print('')

        time.sleep(1.5)
        print('Loan Records')
        for items in self.bank_records_file3:  # printing loan account records.
            print(items, end='')
        print('')

        time.sleep(1.5)
        print('Transaction History')
        for items in self.bank_records_file4:  # printing transaction records.
            print(items, end='')
        print('')


class Account(ABC):  # if user is admin.
    bank_balance = 0  # creating class variable bank balance.

    def info(self):
        """ The function will take info about customer."""

        c = Customer()  # association, creating object of customer class.
        c.info()  # calling function for log in.

    def new_account_deposit_amount(self):
        """The function takes money as input to save in account only when user customer is creating new account."""

        while True:
            try:
                time.sleep(1.5)
                self.t = datetime.today()
                self.__new_amount_deposit = int(input('enter the amount you want put in your  account:'))
                Account.bank_balance = self.__new_amount_deposit
                Customer.records.append(str(Account.bank_balance))
                self.transaction_amount = self.__new_amount_deposit
                self.transaction_history = f'Deposit amount:{self.transaction_amount}, Time:{self.t},' \
                                           f'Total balance:{Account.bank_balance}'
                break
            except ValueError:
                time.sleep(0.5)
                print("The amount of money you have entered is invalid.")

    def withdraw_amount(self):
        """The function works when a customer wants to withdraw money from his account."""
        pass

    def deposit_amount(self):
        """The function works when a customer wants to withdraw money from his account."""
        pass

    def get_account_info(self):
        """The function returns info of a customer."""

        print(Customer.records)

    @abstractmethod
    def get_account_balance(self):
        return Account.bank_balance

    def transaction_history_(self):
        """The function has transaction history of an account"""

        return self.transaction_history


# if user wants to take loan
class Loan(Account):
    def info(self):
        """The function takes information about the loan from the user."""

        super().info()

    def set_loan_rate(self):
        """The function has fixed values of some variables."""

        self.__principal_amount = 0
        self.interest_rate = 8.6
        self.__loan_duration = 12
        self.__loan_balance = 0

    def login(self, file):
        """ The function works when user is loging his account,"""

        l_ = Customer()
        l_.login(file)

    def set_loan_info(self):
        """The function sets the loan details entered by the user."""

        while True:
            try:
                time.sleep(1.5)
                self.t = datetime.today()
                self.__principal_amount = int(input('Enter the principal amount: '))
                self.__loan_duration = int(input('Enter the loan duration (in months): '))
                break
            except ValueError:
                time.sleep(0.5)
                print('Invalid value.')

        self.__loan_balance = self.__principal_amount
        Customer.records.append(str(self.__loan_balance))
        self.transaction_amount = self.__loan_balance
        self.transaction_history = f'Loan duration:{self.__loan_duration}, Loan Balance left:' \
                                   f'{self.__principal_amount}, Time:{str(self.t)}'

    def debit_monthly_interest(self):
        """The function deducts the monthly interest from the loan balance."""

        self.initial_loan = int(Customer.records[-1])
        self.__loan_balance = int(Customer.records[-1])
        monthly_interest = (self.interest_rate / 100) * self.__loan_balance
        self.__loan_balance -= monthly_interest
        self.t = datetime.today()

        with open('LoanRecords.txt', 'r') as file:
            records = file.readlines()  # saving records of loan account in a variable.

        for i, record in enumerate(records):
            if eval(record) == Customer.records:
                Customer.records[-1] = str(self.__loan_balance)
                records[i] = str(Customer.records) + '\n'
                break

        with open('LoanRecords.txt', 'w') as file:  # writing records of loan account in file.
            file.writelines(records)  # writing records of loan account in file.

        self.transaction_amount = self.__loan_balance
        self.transaction_history = f'Loan duration:{self.__loan_duration},Initial Loan Balance:{self.initial_loan}, ' \
                                   f'Loan Balance left:{self.transaction_amount}, Time:{str(self.t)}'

    def get_account_balance(self):
        """The function prints the current loan balance."""

        Account.bank_balance = Customer.records[-1]
        time.sleep(0.75)
        print(f'Loan Balance: {Account.bank_balance}')

    def transaction_history_(self):
        """The function has transaction history of an account"""

        return self.transaction_history


class CheckingAccount(Account):
    def info(self):
        """The function takes information about user's checking account."""

        super().info()
        self.credit_limit = 0
        self.overdraft_fee = 0

    def login(self, file):
        """ The function works when user is loging his account,"""

        ch = Customer()
        ch.login(file)

    def set_credit_limit(self, limit):
        """The function sets the credit limit for the user's checking account"""

        self.credit_limit = limit

    def set_overdraft_fee(self, fee):
        """The function sets overdraft fee when user's balance goes to negative."""

        self.overdraft_fee = fee

    def withdraw_amount(self):
        """The function works when a customer wants to withdraw money from his checking account."""

        Account.bank_balance = int(Customer.records[-1])
        while True:
            try:
                time.sleep(1.5)
                self.t = datetime.today()
                self.__withdraw_amount = int(input('Enter the amount you want to withdraw from your current account:'))
                break
            except ValueError:
                time.sleep(0.5)
                print("Invalid value.")

        with open('CheckingAccountRecords.txt', 'r') as file:
            records = file.readlines()  # saving records of checking account in a variable.

        for i, record in enumerate(records):
            if eval(record) == Customer.records:
                # if withdrawal amount is less than or equal to account balance:
                if self.__withdraw_amount <= Account.bank_balance:
                    Account.bank_balance -= self.__withdraw_amount
                    Customer.records[-1] = Account.bank_balance
                    time.sleep(1.5)
                    print('Withdrawal successful.')
                    self.transaction_amount = self.__withdraw_amount
                    self.transaction_history = f'withdrawal amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                               f'Total Balance:{Account.bank_balance}'

                #  if withdrawal amount is greater than account balance
                elif self.__withdraw_amount <= Account.bank_balance + self.credit_limit:
                    time.sleep(0.75)
                    self.t = datetime.today()
                    overdraft_choice = input('Withdrawal amount exceeds account balance. '
                                             'Do you want to proceed with overdraft? (y/n):').lower()

                    if overdraft_choice == 'y':  # if customer wants to withdraw
                        self.__overdraft_amount = self.__withdraw_amount - Account.bank_balance
                        self.new_amount = Account.bank_balance - self.__withdraw_amount - self.overdraft_fee
                        Account.bank_balance = self.new_amount
                        Customer.records[-1] = Account.bank_balance
                        time.sleep(1.5)
                        print('Withdrawal successful. Overdraft amount:', self.__overdraft_amount)
                        self.transaction_history = f'Overdraft amount:{self.transaction_amount}, ' \
                                                   f'Time:{str(self.t)},Total Balance:{Account.bank_balance}'
                    else:
                        time.sleep(0.5)
                        print('Withdrawal canceled.')
                else:
                    time.sleep(0.5)
                    print('Insufficient funds.')

                Customer.records[-1] = str(Account.bank_balance)
                records[i] = str(Customer.records) + '\n'
                break

        with open('CheckingAccountRecords.txt', 'w') as file:
            file.writelines(records)   # writing records of checking account in file.

    def deposit_amount(self):
        """The function works when a customer wants to withdraw money from his account."""

        Account.bank_balance = int(Customer.records[-1])
        while True:
            try:
                time.sleep(1.5)
                self.t = datetime.today()
                self.__deposit_amount = int(input('Enter the amount you want to deposit:'))
                break
            except ValueError:
                time.sleep(0.5)
                print('Invalid value.')

        with open('CheckingAccountRecords.txt', 'r') as file:
            records = file.readlines()  # saving records of checking account in a variable.

        for i, record in enumerate(records):
            if eval(record) == Customer.records:
                Account.bank_balance += self.__deposit_amount
                Customer.records[-1] = str(Account.bank_balance)
                records[i] = str(Customer.records) + '\n'
                break

        with open('CheckingAccountRecords.txt', 'w') as file:
            file.writelines(records)  # writing records of checking account in file.

        self.transaction_amount = self.__deposit_amount
        self.transaction_history = f'Deposit amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                   f'Total Balance:{Account.bank_balance}'
        time.sleep(1.5)
        print('Deposit successful.')

    def get_account_balance(self):
        """The function prints the current account balance."""

        time.sleep(0.75)
        print(f'Current Account Balance: {Account.bank_balance}')

    def transaction_history_(self):
        """The function has transaction history of an account"""

        return self.transaction_history


class SavingAccount(Account):
    def info(self):
        """The function takes information about user's saving account."""

        super().info()
        self.interest_rate = 0

    def login(self, file):
        """ The function works when user is loging his account,"""

        sv = Customer()
        sv.login(file)

    def deposit_amount(self):
        """The function works when a customer wants to withdraw money from his account."""

        Account.bank_balance = int(Customer.records[-1])
        while True:
            try:
                time.sleep(1.5)
                self.t = datetime.today()
                self.__deposit_amount = int(input('Enter the amount you want to deposit:'))
                break
            except ValueError:
                time.sleep(0.5)
                print('Invalid value.')

        with open('SavingAccountRecords.txt', 'r') as file:
            records = file.readlines()  # saving records of saving account in a variable.

        for i, record in enumerate(records):
            if eval(record) == Customer.records:
                Account.bank_balance += self.__deposit_amount
                Customer.records[-1] = str(Account.bank_balance)
                records[i] = str(Customer.records) + '\n'
                time.sleep(1.5)
                print('Deposit successful.')
                break

        with open('SavingAccountRecords.txt', 'w') as file:
            file.writelines(records)  # writing records of saving accounts in file.

        self.transaction_amount = self.__deposit_amount
        self.transaction_history = f'Deposit amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                   f'Total Balance:{Account.bank_balance}'

    def apply_interest(self):
        """The function updates the account balance according to the bank's applied interest rate."""

        self.interest_rate = 0.05  # Assuming interest rate is 5%
        Account.bank_balance = int(Customer.records[-1])
        self.new_amount = int(Account.bank_balance * self.interest_rate)
        self.new_amount += Account.bank_balance

    def withdraw_amount(self):
        """The function works when a customer wants to withdraw money from their savings account."""

        while True:
            try:
                time.sleep(1.5)
                self.t = datetime.today()
                self.__withdraw_amount = int(input('Enter the amount you want to withdraw from your saving account:'))
                break
            except ValueError:
                time.sleep(0.5)
                print('Invalid value.')

        with open('SavingAccountRecords.txt', 'r') as file:
            records = file.readlines()  # saving records of saving account in a variable.

        for i, record in enumerate(records):
            if eval(record) == Customer.records:
                if self.__withdraw_amount <= Account.bank_balance:
                    self.new_amount -= self.__withdraw_amount
                    time.sleep(1.5)
                    print('Withdrawal successful.')
                    Account.bank_balance = self.new_amount
                    Customer.records[-1] = str(Account.bank_balance)
                    records[i] = str(Customer.records) + '\n'
                    break
            else:
                time.sleep(0.5)
                print("Insufficient funds in your savings account.")

        with open('SavingAccountRecords.txt', 'w') as file:
            file.writelines(records)  # writing the records of saving accounts in file.

        self.transaction_amount = self.__withdraw_amount
        self.transaction_history = f'Withdrawal amount:{self.transaction_amount}, Time:{str(self.t)},' \
                                   f'Total Balance:{Account.bank_balance}'

    def get_account_balance(self):
        """The function prints the saving account balance."""

        time.sleep(0.75)
        print(f'Saving Account Balance: {Account.bank_balance}')

    def transaction_history_(self):
        """The function has transaction history of a saving account"""

        return self.transaction_history


# Saving all bank records in a file
class FileSaver(SavingAccount, CheckingAccount, Loan, Customer):
    def saving_account_records(self):
        """ The function saves all info related customers of saving account."""

        self.bank_records_file = open('SavingAccountRecords.txt', 'a+')
        self.bank_records_file.write(str(Customer.records) + '\n')  # saving records of saving account.
        self.acc_no = f'Account number:{Customer.Customer_account_no}'  # account number of saving account user.

    def checking_account_records(self):
        """ The function saves all info related customers of checking account."""

        self.bank_records_file = open('CheckingAccountRecords.txt', 'a+')
        self.bank_records_file.write(str(Customer.records) + '\n')  # saving records of checking account.
        self.acc_no = f'Account number:{Customer.Customer_account_no}'  # account number of checking account user.

    def loan_records(self):
        """ The function saves all info related customers who take loan."""

        self.bank_records_file = open('LoanRecords.txt', 'a+')
        self.bank_records_file.write(str(Customer.records) + '\n')  # saving records of loan account.
        self.acc_no = f'Account number:{Customer.Customer_account_no}'  # account number of loan account user.

    def transaction_history(self, obj_):
        """The function keeps all records of transaction history."""

        self.bank_records_file = open('TransactionHistory.txt', 'a+')
        self.acc_no = f'Account number:{Customer.Customer_account_no}'  # account number of any account user.
        self.transaction = obj_  # calling function of transaction history belongs to any subclass.
        self.bank_records_file.write(str(self.acc_no) + '=>' +
                                     str(self.transaction) + '\n')  # records of transaction history.

    def delete_customer_records(self, customer_account_no):
        """Delete the records of a particular customer from the file"""

        file_list = ['CheckingAccountRecords.txt', 'SavingAccountRecords.txt', 'LoanRecords.txt']
        for files in file_list:
            # Open the file in read mode and read all lines
            with open(files, 'r') as file:
                lines = file.readlines()

            # Open the file in write mode and write all lines except the one to be deleted
            with open(files, 'w') as file:
                for line in lines:
                    if customer_account_no not in line:
                        file.write(line)

        time.sleep(0.75)
        print(f"Records of customer with account number {customer_account_no} deleted.")


u = User()  # creating the object of main class to start the execution of program
u.login_()  # calling the function of main class to start the program
