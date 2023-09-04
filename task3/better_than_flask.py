class BetterThanFlask:

    views_dict = {}

    @classmethod
    def route(cls, path):
        def w2(func):
            BetterThanFlask.views_dict[path] = func

            def w():
                return func

            return w

        return w2


app = BetterThanFlask()


@app.route('/api/v1/books/1337/categories/')
def categories_of_book():
    pass


print(BetterThanFlask.views_dict)
