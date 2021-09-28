user = {}

while True:
    login_or_signup = input("Login (L) or Signup (S) or End (E): ")
    login_or_signup = login_or_signup.lower()
    complete = False
    if login_or_signup == "s":
        user.update({input("Create new username: "): input("Create new password: ")})
    if login_or_signup == "l":
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username == user and password == password:
                continue
            elif username not in user:
                print("This is not a valid username or password, try again!")
                break
                login_or_signup = input("Login (L) or Signup (S) or End (E): ")
            elif password != user[username]:
                print("This is not a valid username or password, try again!")
                break
                login_or_signup = input("Login (L) or Signup (S) or End (E): ")
            elif password == user[username]:
                print(f"Welcome, {username} ")
                print(f"Thank you for logging in.")
                break
    if login_or_signup == "e":
        break
        print("The program is ended")
