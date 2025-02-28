import random
import string
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="wachtwoordengenerator"
)

# Wachtwoord lengte vragen
length = int(input("Enter the password length: "))

# Vragen of er hoofdletter in het wachtwoord moeten
uppercase1 = input("Do you want uppercase: (yes or no) ")
if uppercase1 == "yes":
    characters1 = string.ascii_letters
elif uppercase1 == "no":
    characters1 = string.ascii_lowercase
else:
    raise Exception("Sorry, type yes or no") 

# Vragen of er cijfers in het wachtwoord moeten
digits1 = input("Do you want digits: (yes or no) ")
if digits1 == "yes":
    characters2 = characters1 + string.digits
elif digits1 == "no":
    characters2 = characters1
else:
    raise Exception("Sorry, type yes or no")

# Vragen of er tekens in het wachtwoord moeten
punctuation1 = input("Do you want punctuation: (yes or no) ")
if punctuation1 == "yes":
    characters3 = characters2 + string.punctuation
elif punctuation1 == "no":
    characters3 = characters2
else:
    raise Exception("Sorry, type yes or no") 

# Functie die het wachtwoord maakt
def generate_password():
    password = ''.join(random.choice(characters3) for i in range(length))
    return password

# Hier voer ik het wachtwoord in de database
mycursor = mydb.cursor()
sql = "INSERT INTO wachtwoorden (wachtwoord) VALUES (%s)"
val = (generate_password(),)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.close()
mydb.close()

print("Generated password:", generate_password())