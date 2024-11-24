true_password = '12345'
attempts=0
while True:
    password = input("Enter the password:")
    if password.lower()== true_password:
        print("Correct!Access granted.")
    else:
        attempts+=1
        if attempts==5:
            print("Maximum attempts reached.Authorities have been alerted.")
        else:
            print(f"Incorrect.{5-attempts}attempts left remaining.")

    



 






