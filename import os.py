import os
from datetime import datetime, timedelta
# -------------------- DATA --------------------
books = [
    {
        "id": 101,
        "title": "Python Programming",
        "author": "Mark Lutz",
        "category": "Programming",
        "quantity": 5
    },
    {
        "id": 102,
        "title": "Data Structures",
        "author": "Seymour Lipschutz",
        "category": "Computer Science",
        "quantity": 3
    },
    {
        "id": 103,
        "title": "Operating Systems",
        "author": "Galvin",
        "category": "Computer Science",
        "quantity": 4
    }
]
students = []
issued_books = []
# -------------------- UTILITY FUNCTIONS --------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def pause():
    input("\nPress Enter to continue...")
def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None
def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None
# -------------------- BOOK MANAGEMENT --------------------
def add_book():
    clear_screen()
    print("=" * 55)
    print("                 ADD NEW BOOK")
    print("=" * 55)
    try:
        book_id = int(input("Enter Book ID: "))
        if find_book(book_id):
            print("\nBook ID already exists!")
            pause()
            return
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        category = input("Enter Category: ")
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            print("\nQuantity must be greater than 0.")
            pause()
            return
        books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "category": category,
            "quantity": quantity
        })
        print("\nBook added successfully!")
    except ValueError:
        print("\nInvalid input!")
    pause()
def display_books():
    clear_screen()
    print("=" * 90)
    print("                         ALL BOOKS")
    print("=" * 90)
    if not books:
        print("No books available.")
        pause()
        return
    print(
        f"{'ID':<8}"
        f"{'Title':<25}"
        f"{'Author':<20}"
        f"{'Category':<20}"
        f"{'Qty':<5}"
    )
    print("-" * 90)
    for book in books:
        print(
            f"{book['id']:<8}"
            f"{book['title'][:24]:<25}"
            f"{book['author'][:19]:<20}"
            f"{book['category'][:19]:<20}"
            f"{book['quantity']:<5}"
        )
    pause()
def search_book():
    clear_screen()
    print("=" * 55)
    print("                  SEARCH BOOK")
    print("=" * 55)
    keyword = input("Enter title, author or category: ").lower()
    found = False
    print()
    for book in books:
        if (
            keyword in book["title"].lower()
            or keyword in book["author"].lower()
            or keyword in book["category"].lower()
        ):
            print(f"Book ID   : {book['id']}")
            print(f"Title     : {book['title']}")
            print(f"Author    : {book['author']}")
            print(f"Category  : {book['category']}")
            print(f"Available : {book['quantity']}")
            print("-" * 40)
            found = True
    if not found:
        print("No matching book found.")
    pause()
def remove_book():
    clear_screen()
    print("=" * 55)
    print("                  REMOVE BOOK")
    print("=" * 55)
    try:
        book_id = int(input("Enter Book ID: "))
        book = find_book(book_id)
        if book is None:
            print("\nBook not found.")
        elif any(record["book_id"] == book_id for record in issued_books):
            print("\nCannot remove this book because it is issued.")
        else:
            books.remove(book)
            print("\nBook removed successfully.")

    except ValueError:
        print("\nInvalid Book ID.")
    pause()
# -------------------- STUDENT MANAGEMENT --------------------
def add_student():
    clear_screen()
    print("=" * 55)
    print("                 ADD STUDENT")
    print("=" * 55)
    try:
        student_id = int(input("Enter Student ID: "))
        if find_student(student_id):
            print("\nStudent ID already exists!")
            pause()
            return
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        phone = input("Enter Phone Number: ")
        students.append({
            "id": student_id,
            "name": name,
            "course": course,
            "phone": phone
        })
        print("\nStudent added successfully!")
    except ValueError:
        print("\nInvalid input!")
    pause()
def display_students():
    clear_screen()
    print("=" * 80)
    print("                       ALL STUDENTS")
    print("=" * 80)
    if not students:
        print("No students registered.")
        pause()
        return
    print(
        f"{'ID':<10}"
        f"{'Name':<25}"
        f"{'Course':<25}"
        f"{'Phone':<15}"
    )
    print("-" * 80)
    for student in students:
        print(
            f"{student['id']:<10}"
            f"{student['name'][:24]:<25}"
            f"{student['course'][:24]:<25}"
            f"{student['phone']:<15}"
        )
    pause()
def search_student():
    clear_screen()
    print("=" * 55)
    print("                SEARCH STUDENT")
    print("=" * 55)
    keyword = input("Enter Student ID or Name: ").lower()
    found = False
    for student in students:
        if (
            keyword in str(student["id"])
            or keyword in student["name"].lower()
        ):
            print("\nStudent ID :", student["id"])
            print("Name       :", student["name"])
            print("Course     :", student["course"])
            print("Phone      :", student["phone"])
            print("-" * 40)
            found = True
    if not found:
        print("\nStudent not found.")
    pause()
# -------------------- ISSUE BOOK --------------------
def issue_book():
    clear_screen()
    print("=" * 55)
    print("                  ISSUE BOOK")
    print("=" * 55)
    try:
        student_id = int(input("Enter Student ID: "))
        book_id = int(input("Enter Book ID: "))
        student = find_student(student_id)
        book = find_book(book_id)
        if student is None:
            print("\nStudent not found.")
            pause()
            return
        if book is None:
            print("\nBook not found.")
            pause()
            return
        if book["quantity"] <= 0:
            print("\nBook is currently unavailable.")
            pause()
            return
        # Check whether same student already has the book
        for record in issued_books:
            if (
                record["student_id"] == student_id
                and record["book_id"] == book_id
            ):
                print("\nThis student already has this book.")
                pause()
                return
        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=14)
        issued_books.append({
            "student_id": student_id,
            "book_id": book_id,
            "issue_date": issue_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d")
        })
        book["quantity"] -= 1
        print("\nBook issued successfully!")
        print("Issue Date :", issue_date.strftime("%Y-%m-%d"))
        print("Due Date   :", due_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("\nInvalid input!")
    pause()
# -------------------- RETURN BOOK --------------------
def return_book():
    clear_screen()
    print("=" * 55)
    print("                 RETURN BOOK")
    print("=" * 55)
    try:
        student_id = int(input("Enter Student ID: "))
        book_id = int(input("Enter Book ID: "))
        record = None
        for item in issued_books:
            if (
                item["student_id"] == student_id
                and item["book_id"] == book_id
            ):
                record = item
                break
        if record is None:
            print("\nNo issue record found.")
            pause()
            return
        book = find_book(book_id)
        if book:
            book["quantity"] += 1
        due_date = datetime.strptime(
            record["due_date"],
            "%Y-%m-%d"
        )
        return_date = datetime.now()
        overdue_days = (return_date - due_date).days
        if overdue_days > 0:
            fine = overdue_days * 5
            print(f"\nBook returned late by {overdue_days} day(s).")
            print(f"Fine: Rs. {fine}")
        else:
            print("\nBook returned on time.")
            print("Fine: Rs. 0")
        issued_books.remove(record)
        print("Book returned successfully!")
    except ValueError:
        print("\nInvalid input!")
    pause()
# -------------------- ISSUED BOOKS --------------------
def display_issued_books():
    clear_screen()
    print("=" * 100)
    print("                         ISSUED BOOKS")
    print("=" * 100)
    if not issued_books:
        print("No books are currently issued.")
        pause()
        return
    print(
        f"{'Student ID':<15}"
        f"{'Student Name':<25}"
        f"{'Book ID':<10}"
        f"{'Book Title':<25}"
        f"{'Due Date':<15}"
    )
    print("-" * 100)
    for record in issued_books:
        student = find_student(record["student_id"])
        book = find_book(record["book_id"])
        student_name = student["name"] if student else "Unknown"
        book_title = book["title"] if book else "Unknown"
        print(
            f"{record['student_id']:<15}"
            f"{student_name[:24]:<25}"
            f"{record['book_id']:<10}"
            f"{book_title[:24]:<25}"
            f"{record['due_date']:<15}"
        )
    pause()
# -------------------- STATISTICS --------------------
def library_statistics():
    clear_screen()
    total_books = sum(book["quantity"] for book in books)
    issued_count = len(issued_books)
    total_students = len(students)
    total_book_types = len(books)
    print("=" * 55)
    print("                LIBRARY STATISTICS")
    print("=" * 55)
    print(f"\nDifferent Books  : {total_book_types}")
    print(f"Available Copies : {total_books}")
    print(f"Issued Books     : {issued_count}")
    print(f"Registered Users : {total_students}")
    pause()
# -------------------- MAIN MENU --------------------
def main():
    while True:
        clear_screen()
        print("=" * 65)
        print("              LIBRARY MANAGEMENT SYSTEM")
        print("=" * 65)
        print("\n1.  Add Book")
        print("2.  Display All Books")
        print("3.  Search Book")
        print("4.  Remove Book")
        print("\n5.  Add Student")
        print("6.  Display Students")
        print("7.  Search Student")
        print("\n8.  Issue Book")
        print("9.  Return Book")
        print("10. Display Issued Books")
        print("\n11. Library Statistics")
        print("12. Exit")
        print("=" * 65)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            add_student()
        elif choice == "6":
            display_students()
        elif choice == "7":
            search_student()
        elif choice == "8":
            issue_book()
        elif choice == "9":
            return_book()
        elif choice == "10":
            display_issued_books()
        elif choice == "11":
            library_statistics()
        elif choice == "12":
            clear_screen()
            print("\nThank you for using Library Management System!")
            break
        else:
            print("\nInvalid choice!")
            pause()
# -------------------- PROGRAM START --------------------
if __name__ == "__main__":
    main()