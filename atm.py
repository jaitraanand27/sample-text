import calc as ca
USER_DATA = {
    "username" : "priya",
    "Acc no"   : 123456789,
    "pin"      : 1234,
    "total_bal" : 10000
            }

def user_info():
    if USER_DATA and USER_DATA["username"]:
        return f"Hi welcome user {USER_DATA['username']} your acc.no is {USER_DATA['Acc no']}"
    else:
        return False

def withdraw(withdrawal_amount):
    if withdrawal_amount > USER_DATA["total_bal"]:
        return False
    else:
        amount = ca.withdraw_calc(USER_DATA["total_bal"],withdrawal_amount)
        USER_DATA["total_bal"] = amount
        return amount

def deposit(deposit_amount):
    if deposit_amount:
        amount = ca.deposit_calc(USER_DATA["total_bal"],deposit_amount)
        USER_DATA["total_bal"] = amount
        return amount
    else:
        return False

def check_balance():
    return USER_DATA["total_bal"]

def main():
    print("Welcome To TP ATM......")
    print("="*20)
    pin = int(input("Enter your pin no to proceed:"))
    if pin == USER_DATA["pin"]:
        print(user_info())
        while True:
            choice = int(input("1.withdraw\n 2.deposit\n 3.check balance\n 4. exit\n Enter your choice:"))
            match choice:
                case 1:
                    amount = int(input("Enter the amount to withdraw:"))
                    withdraw_resp = withdraw(amount)
                    if withdraw_resp:
                        print(f"Withdrawal successful,your total balance is: {withdraw_resp}")
                    else:
                        print("insufficient balance")
                case 2:
                    amount = int(input("Enter the amount to deposit:"))
                    print(f"Deposit successful, your total balance is: {deposit(amount)}")
                case 3:
                    print(f"your total balance is: {check_balance()}")
                case 4:
                    print("Thanks for using TP ATM")
                    break
                case _:
                    print("invalid choice, please choose between 1 to 4")
    else:
        print("invalid pin no,please try again")
        return

if __name__ == "__main__":
    main()