import datetime

today = datetime.date.today()
time = datetime.datetime.now()

with open("Journel_2026.txt","w") as file:
    print(f"Date: {today.strftime("%d-%m-%Y")}")
    print(f"Time: {time.strftime("%H-%M-%S")}")

    Data = input("Describe How is the day ?\n")
    file.write(f"Date: {today.strftime("%d-%m-%Y")}")
    file.write(f"\n\nWhat I have Experienced ?\n")
    file.write(f"{Data}")
    file.write("\n------------------------------------------------\n\n")
    print("Thank You.")