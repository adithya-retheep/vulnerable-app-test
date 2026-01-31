import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)

    print("User:", username)
