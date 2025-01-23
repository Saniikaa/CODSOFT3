import random
import string
import secrets

def generate_password(length, complexity):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None
    
    complexity = complexity.lower()
    
    if(complexity == "basic"):
        password = " ".join(random.choices(string.ascii_lowercase, k=length))
        return password
    
    elif(complexity == "intermediate"):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits)
        ]
        
        all_characters = lower + upper + digits
        password += random.choices(all_characters, k=length - 3)
        
        return ''.join(password)
    
    elif(complexity == "strong"):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation
        
        password = [
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(digits),
            secrets.choice(special)
        ]
        
        all_characters = lower + upper + digits + special
        password += random.choices(all_characters, k=length - 4)
        
        random.shuffle(password)
        
        return ''.join(password)
    
    else:
        print("Invalid complexity level. Please choose Basic, Intermediate, or Strong.")
        return None


try:
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter Complexity of password : (Basic, Intermediate, Strong)")
    password = generate_password(length, complexity)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Invalid input! Please enter a valid number.")
