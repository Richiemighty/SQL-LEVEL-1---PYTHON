# book_info = "richard kehinde ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
book_info = "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
book_info = book_info.split(";")


author, book_title,  year_published, isbn_number, no_of_pages, cost = book_info

author = author.title()
book_title = book_title.strip(" ")
isbn_number = isbn_number.replace('ISN', 'ISBN')
cost = float(cost)

formatted_book_info = f"""
The book {book_title} was written by {author} and published in {year_published}.
It has {no_of_pages} pages and {isbn_number} and costs {cost:.2f}.
"""

print(formatted_book_info)
