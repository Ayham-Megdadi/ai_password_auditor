def Lest():
    return [ "123456", "password", "admin", "12345678", "user", "111222333!", "test", "ZXCdsaQWE@231",
             "A1b2C3!", "Jordan", "Strong_P@ss1", "A1b@C3d#", "PA@swo#2", "pAs!312", "Val1d_P@ssw0rd!"]

def User():
    username = ("ayham", "admin", "user")
    birth_year = "2004"
    password = "admin"
    return username, birth_year, password

def main():
    username, birth_year, password = User()

    print(f"{'Password':<20} | {'Score':<5} | {'Classification':<10}")
    print("-" * 45)

    for pwd in Lest():
        score = 0

        if len(pwd) >= 8:
            score += 1
        if any(c.isupper() for c in pwd) and any(c.islower() for c in pwd):
            score += 1
        if any(c.isdigit() for c in pwd):
            score += 1
        if any(c in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|" for c in pwd):
            score += 1
        if not any(u in pwd.lower() for u in username):
            score += 1
        if birth_year not in pwd:
            score += 1

        if score <= 2:
            classification = "Weak"
        elif 3 <= score <= 4:
            classification = "Medium"
        else:
            classification = "Strong"

        print(f"{pwd:<20} | {score:<5} | {classification:<10}")

def check(pwd):
    username, birth_year, _ = User()
    score = 0

    if len(pwd) >= 8:
        score += 1
    if any(c.isupper() for c in pwd) and any(c.islower() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()-_=+" for c in pwd):
        score += 1
    if not any(u in pwd.lower() for u in username):
        score += 1
    if birth_year not in pwd:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength


def login():
    username, birth_year, password = User()

    print("Logging in...")
    x = input("Enter your name: ")
    y = input("Enter your password: ")

    if x in username and y == password:
        print("____________________________")
        print("Hello admin\n")
        print("1- Show password list")
        print("2- Check a password")

        z = input("Make your choice: ")
        if z == "1":
            main()
        elif z == "2":
            pwd = input("Enter password to check: ")
            strength = check(pwd)
            print(f"Strength: {strength}")
        else:
            print("1 or 2 not > or < ")
    else:
        print("Login failed")

login()
