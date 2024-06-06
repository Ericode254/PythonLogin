# PythonLogin
A simple login system with mysql as the database

## Set up
Make sure that mysql is set up on your machine. Follow the link for more info:
https://www.mysql.com
Create a database instance in your mysql:
`CREATE DATABASE database_name;`

`    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = ""
    )

`

host = "the host name"
user = "the name used while setting up mysql"
password = "your password"
database = "the database name"

## Run
`python3 main.py`

