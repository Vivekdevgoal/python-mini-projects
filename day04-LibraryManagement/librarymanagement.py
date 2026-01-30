import json 
import os 

library_file = "library.json"
books = {}

def load_books():
    global books
    try: 
        if os.path.exists(library_file):
            with open(library_file,'r') as lf:
                books = json.load(lf)
    except (FileNotFoundError, json.JSONDecodeError):
        books = {}

def view_books():
    if not books:
        print("no books in library.")
        return
    
    for book_id, info in books.items():
        print(f"book_id = {book_id}")
        print(f"\tname = {info['name']}")
        print(f"\tauthor = {info['author']}")
        print(f"\ttotal copies = {info['total_copies']}")
        print(f"\tavailable copies = {info['available_copies']}")
        print("**********************\n")

def save_books():
    with open(library_file,'w') as wf:
        json.dump(books, wf,indent = 4)

def add_book():
    book_id = int(input("enter book id:"))
    if book_id in books:
        print("book id already exists.")
        return 
    
    name = input("enter book name:")
    author = input("enter auther's name:")
    copies = int(input("enter number of tatal copies:"))
    
    avail_copies = int(input("enter number of available copies: "))
    if avail_copies > copies:
        print("avilable copies cannot exceed total copies.")
        return 

    books[book_id] = { 
        "name": name,
        "author": author,
        "total_copies": copies,
        "available_copies": avail_copies 
    }
    save_books()
    print("book added successfully.")

def issue_book():
    book_id = int(input("enter book id to issue:"))
    if book_id not in books:
        print("id not valid.")
        return
    
    if books[book_id]["available_copies"] <= 0:
        print("books not available to issue.")
        return

    books[book_id]["available_copies"] -= 1
    save_books()
    print("thank you, pls return it on time.")

def return_book():
    book_id = int(input("entet the book id to return: "))
    if book_id not in books:
        print("book with this id doesn't exist or invalid id.")
        return
    
    if books[book_id]["available_copies"] >= books[book_id]["total_copies"]:
        print("all copies are already present.")
        return
    
    books[book_id]["available_copies"] += 1
    save_books()
    print("book returned successfully, thank you!!!")

def issued_books():
    found = False

    for book_id, info in books.items():
        issued_books = info["total_copies"] - info["available_copies"]
        print(f"{issued_books} books of {info['name']} is issued.")
        found = True
    if not found:
        print("no books are issued currently")  

def total_books_issued():
    total_issued = 0
    for info in books.values():
        total_issued += info["total_copies"] - info["available_copies"]
    print("total books issued is: ",total_issued)


def main():
    load_books()
    while True:
        print("***** Library Management *****")
        print("1. view books available.")
        print("2. add new book.")
        print("3. issue book.")
        print("4. return book.")
        print("5. view issued books.")
        print("6. view total issued books.")
        print("7. exit.")

        choice = input("enter the task no. to perform: ")
        if choice == '1':
            view_books()

        elif choice == '2':
            add_book()
        
        elif choice == '3':
            issue_book()
        
        elif choice == '4':
            return_book()

        elif choice == '5':
            issued_books()

        elif choice == '6':
            total_books_issued()

        elif choice == '7':
            print('exiting library system')
            break

        else:
            print("enter the valid task number to perform, fucker!!!")

if __name__ == "__main__":
    main()