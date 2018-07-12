class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("\n Email has been updated to {email}.".format(email=self.email))

    def __repr__(self):
        books_read = []
        for book in self.books:
            books_read.append(book.title)
        return  ('''
                \n User's Name: {name}
                \n Email: {email}
                \n Books Read: {books} \n'''.format(name=self.name, email=self.email, books=books_read))

    def __eq__(self, other_user):
        if other_user.email == self.email and other_user.name == self.name:
            print("\n Both users are the same.")
            return True
        else:
            print("\n Users are different.")
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for book, rating in self.books.items():
            if rating is not None:
                total = total + rating
            else:
                pass
        average = total/(len(self.books))
        return average

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("\n ISBN has been updated to {new_isbn}.".format(new_isbn=new_isbn))

    def add_rating(self, rating):
        if (rating is not None) and not(rating >= 0 and rating <= 4):
            print("\n Invalid Rating")
        else:
            self.ratings.append(rating)

    def __eq__(self, other_book):
        if(self.title == other_book.title and self.isbn == other_book.isbn):
            print("\n This is the same book.")
            return True
        else:
            print("\n These books are different.")
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            if rating is not None:
                total = rating + total
                average = total/len(self.ratings)
            else:
                pass
        return average

    def __repr__(self):
        return "{title} || ISBN: {isbn}.".format(title=self.title, isbn=self.isbn)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.get_author

    def __repr__(self):
        return "{title} by {author}.".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}.".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if not(email in self.users):
            print("\n No user with email {email}.".format(email=email))
        else:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if not(book in self.books):
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        print("\n User {user} has been added with email {email}.".format(user=user.name, email=user.email))
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print('\n')
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        high_score = 0
        most_read = ""
        for book, readings in self.books.items():
            if readings > high_score:
                high_score = readings
                most_read = book
            else:
                pass
        return most_read

    def highest_rated_book(self):
        high_score = 0
        for book in self.books:
            if book.get_average_rating() > high_score:
                high_score = book.get_average_rating()
            else:
                pass
        return high_score

    def most_positive_user(self):
        high_score = 0
        most_positive = ""
        for user in self.users.values():
            if user.get_average_rating() > high_score:
                high_score = user.get_average_rating()
                most_positive = user
            else:
                pass
        return most_positive
