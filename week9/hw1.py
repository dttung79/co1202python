titles = []
authors = []
genres = []
publication_years = []

def add_book(titles, authors, genres, publication_years):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    publication_year = int(input("Enter book publication year: "))
    titles.append(title)
    authors.append(author)
    genres.append(genre)
    publication_years.append(publication_year)
    print(title)

def delete_book(titles, authors, genres, publication_years):
    title = input("Enter book title: ")
    for i, book_title in enumerate(titles[:]):
        if book_title == title:
            titles.pop(i)
            authors.pop(i)
            genres.pop(i)
            publication_years.pop(i)
            print(title)
            return
    print(f'Book {title} not found')

def edit_book(titles, authors, genres, publication_years):
    title = input("Enter book title: ")
    new_title = input("Enter new book title: ")
    new_author = input("Enter new book author: ")
    new_genre = input("Enter new book genre: ")
    new_publication_year = int(input("Enter new book publication year: "))
    
    for book_title in titles:
        if book_title == title:
            titles[i] = new_title
            authors[i] = new_author
            genres[i] = new_genre
            publication_years[i] = new_publication_year
            print('title edited')
            return
    print('title not found')

def search_books_by_genre(titles, authors, genres, publication_years):
    genre = input("Enter genre to search for: ")
    found_books = False 
    n = len(titles)
    for i in range(n):
        if genres[i] == genre:
            found_books = True
            print('Title is', titles[i])
            print('Author is',authors[i])
            print('Publication year is', publication_years[i])

    if found_books == False:
        print('No books found')

def print_books_by_publication_year(titles, authors, genres, publication_years):
    for i in range(len(titles) - 1):
        for j in range(i+1, len(titles)):
            if publication_years[i] > publication_years[j]:
                # general swap algorithm
                p = publication_years[i]
                publication_years[i] = publication_years[j]
                publication_years[j] = p
                # swap by python
                titles[i], titles[j] = titles[j], titles[i]
                authors[i], authors[j] = authors[j], authors[i]
                genres[i], genres[j] = genres[j], genres[i]


def run():
    while True:
        print("1. Add book")
        print("2. Delete book")
        print("3. Edit book")
        print("4. Search books by genre")
        print("5. Print books by publication year")
        print("6. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book(titles, authors, genres, publication_years)
        elif choice == 2:
            delete_book(titles, authors, genres, publication_years)
        elif choice == 3:            
            edit_book(titles, authors, genres, publication_years)
        elif choice == 4:
            search_books_by_genre(titles, authors, genres, publication_years)
        elif choice == 5:
            print_books_by_publication_year(titles, authors, genres, publication_years)
        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()