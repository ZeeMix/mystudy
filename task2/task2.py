def router(request: dict) -> callable:
    """"""
    path_dict = {
        "/api/v1/books/": books_list,
        "/api/v1/books/1337/": book_info,
        "/api/v1/books/1337/authors/": authors,
        "/api/v1/categories/": categories,
        "/api/v1/books/1337/categories/": categories_of_book,
    }

    return path_dict.get(request['path'], 404)


def books_list(request):
    """/api/v1/books/"""
    pass


def book_info(request):
    """/api/v1/books/1337/"""
    pass


def authors(request):
    """/api/v1/books/1337/authors/"""
    pass


def categories(request):
    """/api/v1/categories/"""
    pass


def categories_of_book(request):
    """/api/v1/books/1337/categories/"""
    pass
