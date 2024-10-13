import sqlite3

connection = sqlite3.connect("not_telegram2.db")
curs = connection.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#Заполните её 10 записями:
for i in range(1, 11):
    curs.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

#Обновите balance у каждой 2ой записи начиная с 1ой на 500:

curs.execute("UPDATE Users SET balance = ? WHERE username = ? ", (500, "User1"))
curs.execute("UPDATE Users SET balance = ? WHERE username = ? ", (500, "User3"))
curs.execute("UPDATE Users SET balance = ? WHERE username = ? ", (500, "User5"))
curs.execute("UPDATE Users SET balance = ? WHERE username = ? ", (500, "User7"))
curs.execute("UPDATE Users SET balance = ? WHERE username = ? ", (500, "User9"))

#Удалите каждую 3ую запись в таблице начиная с 1ой:

curs.execute("DELETE FROM Users WHERE username = ?", ("User1",))
curs.execute("DELETE FROM Users WHERE username = ?", ("User4",))
curs.execute("DELETE FROM Users WHERE username = ?", ("User7",))
curs.execute("DELETE FROM Users WHERE username = ?", ("User10",))

#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
curs.execute("SELECT age FROM Users WHERE age != ?", (60,))
users = curs.fetchall()
for j in users:
    print(j)

curs.execute("DELETE FROM Users WHERE age = ?", (60,))

# Удаление пользователя с id=6

curs.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчёт кол-ва всех пользователей
curs.execute("SELECT COUNT(*) FROM Users")
col_user = curs.fetchone()[0]
print(col_user)
# Подсчёт суммы всех балансов
curs.execute("SELECT SUM(balance) FROM Users")
sum_balance = curs.fetchone()[0]
print(sum_balance)
print(sum_balance/col_user)


connection.commit()
connection.close()