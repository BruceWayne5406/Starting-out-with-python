import random
import string

def generate_password():
    p_len=int(input("how many characters do you want in your password? "))
    characters=list(string.ascii_letters + string.digits + "/?.><,!@#$%^&*()_+")
    random.shuffle(characters)

    password=[]

    for i in range(p_len):
        password.append(random.choice(characters))
    random.shuffle(password)

    password="".join(password)
    print(password)


choice=input("Do you want to generate a password? ")
if choice =="yes":
    generate_password()
else:
    print("program terminated")
