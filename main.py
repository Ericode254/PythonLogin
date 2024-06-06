import mysql.connector

def registration():
    print("\t\tRegistration")
    user_name = input("Enter your username: ")
    if (user_name == ""):
        print("You must enter a username")
        registration()

    password = input("Enter your password: ")
    if (password == ""):
        print("You must enter a password")
        registration()

    phone = input("Enter your phone number: ")
    if (phone  == ""):
        print("You must enter a phone number")
        registration()
    return user_name, password, phone


def login():
    user_name = input("Enter your username: ")
    if (user_name == ""):
        print("You must enter a username")
        login()

    password = input("Enter your password: ")
    if (password == ""):
        print("You must enter a password")
        login()

    return user_name, password


def DataBaseRegistration(username, password, phone):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "Erico",
        password = "@JilloErick254",
        database = "Logs"
    )

    cursor = mydb.cursor()
    sql = "INSERT INTO Users (username, password, phone) VALUES (%s, %s, %s)"
    val = (username, password, phone)
    cursor.execute(sql, val)

    mydb.commit()


def DataBaseLogin(username, password):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )

    cursor = mydb.cursor()
    sql = "SELECT * FROM Users WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    data = cursor.fetchall() # [(username, password)]

    try:
        if data[0][0] == username and data[0][1] == password:
            print("Successfully logged in")
            return
    except IndexError:
        print("Login failed")
        main()


def main():
    print(""" What to you want to do:
                1. Register
                2. Login
    """
    )

    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_name, password, phone = registration()
        DataBaseRegistration(user_name, password, phone)

    elif choice == 2:
        username, password = login()
        DataBaseLogin(username, password)
    else:
        print("Choice is invalid");
        main()


if __name__ == "__main__":
    main()


