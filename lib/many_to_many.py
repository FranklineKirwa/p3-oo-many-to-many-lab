class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string.")
        self.title = title
        Book.all_books.append(self)


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string.")
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Royalties must be an integer between 0 and 100.")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Royalties must be an integer between 0 and 100.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

