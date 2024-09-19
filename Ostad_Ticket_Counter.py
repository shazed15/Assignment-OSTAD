print("Welcome to Ostad Cinema Hall. If you want to buy a ticket then enter your age and showtime.")
age = int(input("Enter Your Age:"))

showTime = int(input("Enter Your showTime(1000-2045):"))
amount = int(input("Enter Your Ticket Amount:"))
def ticket_price():
    if 1<age <=10 and 1700<showTime<2045:
        print ("Ticket price:300\n""Discount: 0.00\n""Discounted price: ",300*amount)
    elif 1<age <=10 and 1000<showTime<1700:
        print("Ticket price:300\n""Discount: 30.00\n""Discounted price: ", 270 * amount)
    elif 11<= age <=25 and 1700<showTime<2045:
        print("Ticket price:500\n""Discount: 0.00\n""Discounted price: ", 500 * amount)
    elif 11<= age <=25 and 1000<showTime<1700:
        print("Ticket price:500\n""Discount: 50.00\n""Discounted price: ", 450 * amount)
    elif 26<= age <= 60 and 1700<showTime<2045:
        print("Ticket price:800\n""Discount: 0.00\n""Discounted price: ", 800 * amount)
    elif 26<= age <= 60 and 1000<showTime<1700:
        print("Ticket price:800\n""Discount: 80.00\n""Discounted price: ", 720 * amount)
    elif age>60 and 1700<showTime<2045:
        print("Ticket price:400\n""Discount: 0.00\n""Discounted price: ", 400 * amount)
    elif age>60 and 1000<showTime<1700:
        print("Ticket price:400\n""Discount: 40.00\n""Discounted price: ", 360 * amount)
    elif  age<0:
            print("Invalid input. Age must be a positive integer.")
    elif showTime>2400:
            print("Invalid input. Please provide the showtime in the correct format.")
print(ticket_price())
