
class Book:

    def __init__(self, title, author, page_number):
        self.title = title
        self.author = author
        self.page_number = page_number

    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __repr__(self):
        return f'{self.title} by {self.author}!!!'

    def __len__(self):
        book_len = len(self.title) + len(self.author)
        return book_len
    
    def __lt__(self, other_obj):
        # self.other_obj = other_obj
        # is_less_than = self.page_number < self.other_obj.page_number
        return self.page_number < other_obj.page_number
    
    def __add__(self, other_obj):
        # self.other_obj = other_obj
        # is_less_than = self.page_number + self.other_obj.page_number
        return self.page_number + other_obj.page_number


book_1 = Book('Pyhton for Beginners', 'James Brown', 233)

book_2 = Book('Flutter for Beginners', 'Google Inc.', 544)

print(book_1.__str__())

print(book_1.__repr__())

print(book_1.__len__())

# print(dir(book_1))

# print(len(book_1))

# a_list = [4, 1, 3, 5]

# print(dir(a_list))

# print(30000 < 700)

print(book_1 < book_2)

print(book_1 is book_2)

print(id(book_1))
print(id(book_2))


