import sys
balance = 5000
pin = int(sys.argv[1])
if pin == 1234:
    i = 2
    while i < len(sys.argv):
        action = sys.argv[i]
        if action == "balance":
            print("Balance =", balance)
            i = i + 1
        elif action == "deposit":
            amount = int(sys.argv[i + 1])
            balance = balance + amount
            print("Deposited. New balance =", balance)
            i = i + 2
        elif action == "withdraw":
            amount = int(sys.argv[i + 1])
            if amount > balance:
                print("Insufficient balance")
            else:
                balance = balance - amount
                print("Please collect cash. New balance =", balance)
            i = i + 2
        else:
            print("Invalid choice")
            i = i + 1
else:
    print("Wrong PIN")
