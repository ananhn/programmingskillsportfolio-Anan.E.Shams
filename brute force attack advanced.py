true_password = "12345"
max_attempts = 5

for attempt in range(max_attempts):
    password = input("Enter the password: ")
    if password == true_password:
        print("Password correct. Access granted.")
    else:
        remaining_attempts = max_attempts - attempt - 1
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempts remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")