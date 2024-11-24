months = {1:31,2:28,3:31,4:30,5:51,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month_number = int(input("Enter the month number(1-12):"))
if 1<= month_number<=12:
    print(f"The month{month_number}has{months[month_number]}days.")
else:
    print("Please enter number between 1 and 12.")

leapyear=input("Is it leap year?") 
leapyear= "Yes"

if leapyear.lower() == leapyear.lower():
    print("February has 29 days in leap year.") 
else:
    print("February has 28 days in non-leap year") 