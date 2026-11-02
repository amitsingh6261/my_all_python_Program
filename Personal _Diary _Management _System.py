
import os
from datetime import datetime

FILE_NAME = "diary.txt"


def add_entry():
    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    title = input("Enter diary title: ")
    content = input("Write your diary: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"\nDATE: {date}\n")
        file.write(f"TITLE: {title}\n")
        file.write(f"CONTENT: {content}\n")
        file.write("-------------------------\n")

    print("Diary entry saved successfully!")


def view_entries():
    if not os.path.exists(FILE_NAME):
        print("No diary entries found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.read()

    if data.strip() == "":
        print("Your diary is empty.")
    else:
        print("===== YOUR DIARY =====")
        print(data)


def search_entry():
    if not os.path.exists(FILE_NAME):
        print("No diary entries found.")
        return

    keyword = input("Enter title or word to search: ").lower()

    with open(FILE_NAME, "r") as file:
        entries = file.read()

    if keyword in entries.lower():
        print("Entry found:")
        lines = entries.split("-------------------------")

        for entry in lines:
            if keyword in entry.lower():
                print(entry)
    else:
        print("No matching entry found.")


def delete_diary():
    if not os.path.exists(FILE_NAME):
        print("Diary file does not exist.")
        return

    confirm = input("Are you sure you want to delete all entries? (yes/no): ")

    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("All diary entries deleted.")
    else:
        print("Delete operation cancelled.")


while True:
    print("===== PERSONAL DIARY SYSTEM =====")
    print("1. Add Diary Entry")
    print("2. View Diary")
    print("3. Search Diary")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        search_entry()

    elif choice == "4":
        delete_diary()

    elif choice == "5":
        print("Thank you for using Personal Diary!")
        break

    else:
        print("Invalid choice! Try again.")
