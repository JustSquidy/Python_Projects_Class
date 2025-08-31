class Author:
    def __init__(self,name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        book_list = ', '.join(self.books) or 'No Books'
        return f'Name: {self.name}  Books Published: {book_list}'
    
Fujimoto = Author('Tatsuki Fujimoto')
Fujimoto.publish('Chainsaw Man')
Fujimoto.publish('Look Back')
print(Fujimoto)

Javier = Author('Javier Reyes')
print(Javier)