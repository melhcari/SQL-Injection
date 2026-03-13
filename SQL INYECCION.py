import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

usuario = input("Usuario: ")
password = input("Password: ")

query = "SELECT * FROM usuarios WHERE usuario = '" + usuario + "' AND password = '" + password + "'"

cursor.execute(query)

resultado = cursor.fetchone()

if resultado:
    print("Login correcto")
else:
    print("Usuario o contraseña incorrectos")
