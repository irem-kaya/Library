class Student:
    def __init__(self, first_name, last_name, birth_year):
      self.first_name = first_name 
      self.last_name = last_name
      self.birth_year = birth_year
      self._is_active = True

   
    def toggle_active(self,token):
        if token == 'secret':
            self._is_active = not self._is_active
            return True
        return False    

    def __str__(self):
        return '<'+ self.first_name + ' ' + self.last_name + '>'

    def __repr__(self):
        return '<'+ self.first_name + ' ' + self.last_name + '>'

  

class Library:
    def __init__(self,name):
      self._students = []
      self._books = []
      self.taken_books = []
      self.name = name

    def add_book(self,book):
      if type(book) is Book:
        self._books.append(book)
        return book
      return False

    def get_books(self):
       return self._books.copy()

    def get_available_books(self):
        return [book for book in self._books if book._is_available]

    def get_book(self,book,student):
        if type(book) is Book and book in self._books and book._is_available and type(student) is Student and student in self._students:
            book._is_available = False
            self.taken_books.append(TakenBook(book , student))
            return True
        return False


    def add_student(self,student):
      if type(student) is Student:
        self._students.append(student)
        return True
      return False

    def get_students(self):
      return self._students.copy()

    def get_active_students(self):
      return [student for student in self._students if student._is_active]

    def del_student(self,student) :
      if type(student) is Student and student in self._students:
        if student in self._students:
          self._students.remove(student)
          return True  
        return False

    def get_taken_books(self):
        return self.taken_books.copy()



class Book:
    def __init__(self,title,author,year):
       self.title = title
       self.author = author
       self.year = year
       self._is_available = True

    def toggle_available(self,token):
       if token == 'secret':
          self._is_available = not self._is_available
          return True
       return False


    def __str__(self):
        return '<' + self.title +  '  by  '   + self.author + '>'

    def __repr__(self):
       return  '<' + self.title +  '  by  '   + self.author + '>' 



class TakenBook:
    def __init__(self,book,student):
            self.book =book
            self.student=student
        
    def __str__(self):
            return '<' + self.book.title + '  by  ' + self.book.author + '  is taken by  ' + self.student.first_name + ' ' + self.student.last_name
          
    def __repr__(self):
            return '<' + self.book.title + '  by  ' + self.book.author + '  is taken by  ' + self.student.first_name + ' ' + self.student.last_name
           


irem= Student('İrem','Kaya',2003)
akif= Student('Akif','Kaya',2017)
volkan=Student('Volkan','Taşcı',1980)
library = Library('Kütüphane')

book1= library.add_book(Book('Python' ,'Volkan Taşçı' , 2019 ))
library.add_book(Book('JAVA' ,'Volkan TAŞÇI' ,2020))
library.add_book(Book('C' ,'Volkan TAŞÇI' ,2020))
library.add_book(Book('C++' ,'Volkan TAŞÇI' ,2020))
library.add_book(Book('C#' ,'Volkan TAŞÇI' ,2020))


library.add_student(irem)
library.add_student(akif)
library.add_student(volkan)

library.get_book(book1,irem)

print(library.get_taken_books())







    

       