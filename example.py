import sqlite3

# Establish a connection and cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query data
cursor.execute("select * from events where date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cats City', '2088.10.17'),
			('Hens', 'Hes City', '2088.10.17')]
cursor.executemany("insert into events values(?,?,?)", new_rows)
connection.commit()
