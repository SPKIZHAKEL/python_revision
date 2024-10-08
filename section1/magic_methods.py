'''
what are magic methods?
These are Dunder (double underscore) methods = __init__, __str__ and __eq__
They are automatically called by many of Python's built in operation, and they allow devs to customize
behaviour of the objects
'''
class Book:

    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title==other.title and self.author==self.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key=="title":
            return self.title
        if key=="author":
            return self.author


book1=Book("The Hobbit","JRR tolkien",310)
book2=Book("merchant of venice","shakespeare",275)
book3=Book("the lion the with the wardrobe","sam",123)
book4=Book("The Hobbit","JRR tolkien",310)

print(book2) #without the __str__ method it would return output as object i.e memory adress. the __str__ returns a string representation of the object
print(book1==book4) #even though both objects are identical its coming as false by default, to change this behaviour we add __eq__
print(book1==book2)

#by default i cant compare to objects so i use __lt__
print(book1<book2)
print(book3<book4)

print(book1+book4)

print("The Hobbit" in book4)

#to index an object
print(book3['title'])
print(book3['author'])