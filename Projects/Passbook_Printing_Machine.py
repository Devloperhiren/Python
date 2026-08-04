import time
import os

if not os.path.exists("Transaction.txt"):
    with open("Transaction.txt","w",encoding="utf-8") as f:
        f.write("0\n")
        f.write(f"{"Date":<15} {"Particulars":<40} {"Debit":<10} {"Credit":<10} {"End Balance":<10}\n")

def get_balance():
    with open("Transaction.txt","r",encoding="utf-8") as f:
        for line in f:
            if(len(line)<15 and line[0]!="\n"):
                balanced=int(line)

        return balanced


Choice = int(input("Enter 1 for Transaction or 2 for printing\n"))

match Choice:

    case 1:
        with open("Transaction.txt","r",encoding="utf-8") as f:
            types = int(input("Enter 1 for Debit, 2 for Credit: "))

            balance = get_balance()

            print(f"Balance: {balance} type:{type(balance)}")

            match types:
                case 1:
                    a_no = int(input("Enter Account Number: "))

                    if(999999999999>a_no<99999999999):
                        print("Enter Valid Account Number")
                    else:
                        Amount = int(input("Enter Amount to Debit: "))
                        if(Amount>balance):
                            print("\nEntered Amount is more than Balance")
                        else:
                            balance -= Amount

                            with open("Transaction.txt","a+",encoding="utf-8") as f:
                                f.write(f"\n\n{time.strftime("%d.%m.%Y"):<15} {a_no:<40} {Amount:<10} {"":<10} {balance:<10}\n")
                                f.write(f"{"":<15} {"At 16041 LAMBE HANUMAN ROAD SURAT":<40} {"":<10} {"":<10} {"":<10}\n")
                                f.write(f"{balance}")

                case 2:
                    a_no = int(input("Enter Account Number: "))
                    if(999999999999>a_no<99999999999):
                        print("Enter Valid Account Number")
                    else:
                        Amount = int(input("Enter Amount: "))
                        if(Amount<0):
                            print("Not Valid Amount")
                        else:
                            balance+=Amount

                            with open("Transaction.txt","a+",encoding="utf-8") as f:
                                f.write(f"\n\n{time.strftime("%d.%m.%Y"):<15} {a_no:<40} {"":<10} {Amount:<10} {balance:<10}\n")
                                f.write(f"{"":<15} {"At 16041 LAMBE HANUMAN ROAD SURAT":<40} {"":<10} {"":<10} {"":<10}\n")
                                f.write(f"{balance}")

    


    case 2:
        balance = 0
        with open("Transaction.txt","r",encoding="utf-8") as f:
            for line in f:
                if(len(line)>15 and line[0]!="\n"):
                    print(line)
                elif(line[0]!="\n"):
                    balance = int(line)

            with open("Transaction.txt","w",encoding="utf-8") as f:
                f.write(f"{balance}\n")
                f.write(f"{"Date":<15} {"Particulars":<40} {"Debit":<10} {"Credit":<10} {"End Balance":<10}\n")
                