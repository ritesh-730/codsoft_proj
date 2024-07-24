import random
import string

def pass_gen():
    print("Welcome to the Password Generator!")
    pass_len = int(input("Enter the desired length of the password: "))
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    all_characters = lowercase + uppercase + digits + special_chars
    password = ''.join(random.choice(all_characters) for _ in range(pass_len))
   
    print("Generated Password: ", password)

while True:
    pass_gen()
    ch = input("Do you want to continue?(y/n): ")
    if ch=="n":
        print("Thankyou for using") 
        break 
 
