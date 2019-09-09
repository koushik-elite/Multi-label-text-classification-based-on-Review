import mysql.connector

mydb = mysql.connector.connect(
  host="10.0.1.149",
  user="remote",
  passwd="HgE78eKhvCs7"
)

print(mydb)