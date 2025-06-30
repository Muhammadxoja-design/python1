developer = {
    "FirstName": "Muhammadxoja",
    "LastName": "Kimyonazarov",
    "age": "15",
    "Number": "+998774041356",
    "mail": "coderkimyonazarov@gmail.com",
    "skills": ["js", "ts", "jsx", "tsx", "py", "php"],
}

# Fayldan userlarni o'qish
users = []
with open("text.txt", "r") as f:
    for line in f:
        if line.strip():
            users.append(eval(line.strip()))

print(f"👋 Hello! I'm {developer['FirstName']} {developer['LastName']}!")
print(f"I'm {developer['age']} years old. This is my first Python project.\n")


def get_input(prompt):
    """Bo'sh kiritishdan himoya qilish"""
    while True:
        value = input(prompt)
        if value.strip():
            return value
        print("❗ You must enter a value.")


if not users:
    print("📌 No users found. Let's register a new user.")
    name = get_input("🧑 Enter Your Full Name: ")
    username = get_input("👤 Choose a Username: ")
    password = get_input("🔒 Enter Password: ")
    verify_password = get_input("🔁 Verify Password: ")

    if password == verify_password:
        new_user = [name, username, password]
        with open("text.txt", "a") as f:
            f.write(f"{new_user}\n")
        print(f"\n✅ Okay {name}, you are successfully registered!")
    else:
        print("❌ Passwords do not match. Registration failed.")
else:
    print("🔐 Users already exist.")
    choice = get_input("Choose an option:\n1. 🔓 Login\n2. 📝 Register\nEnter 1 or 2: ")
    if choice == "1":
        input_username = get_input("👤 Username: ")
        input_password = get_input("🔒 Password: ")
        for user in users:
            if user[1] == input_username and user[2] == input_password:
                print(f"✅ Welcome back, {user[0]}!")
                break
        else:
            print("❌ Incorrect username or password.")
    elif choice == "2":
        print("📝 Register selected")
        name = get_input("🧑 Enter Your Full Name: ")
        username = get_input("👤 Choose a Username: ")
        password = get_input("🔒 Enter Password: ")
        verify_password = get_input("🔁 Verify Password: ")

        if password == verify_password:
            new_user = [name, username, password]
            with open("text.txt", "a") as f:
                f.write(f"{new_user}\n")
            print(f"\n✅ Okay {name}, you are successfully registered!")
        else:
            print("❌ Passwords do not match. Registration failed.")
    else:
        print("❗ Invalid choice.")
