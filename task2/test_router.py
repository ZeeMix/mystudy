import task2


def test1_right_view_test():
    test_dict = {
            "type": "HTTP",
            "http_version": "1.1",
            "method": "GET",
            "path": "/api/v1/books/",
            "raw_path": b"/hello.htm",
            "query_string": b"",
            "headers": [
                ["User-Agent", "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)"],
                ["Host", "www.tutorialspoint.com"],
                ["Accept-Language", "en-us"],
                ["Accept-Encoding", "gzip, deflate"],
                ["Connection", "Keep-Alive"],
            ],
        }
    assert task2.router(test_dict) == task2.books_list


def test2_wrong_view_test():
    test_dict = {
            "type": "HTTP",
            "http_version": "1.1",
            "method": "GET",
            "path": "wrong_path",
            "raw_path": b"/hello.htm",
            "query_string": b"",
            "headers": [
                ["User-Agent", "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)"],
                ["Host", "www.tutorialspoint.com"],
                ["Accept-Language", "en-us"],
                ["Accept-Encoding", "gzip, deflate"],
                ["Connection", "Keep-Alive"],
            ],
        }
    assert task2.router(test_dict) == 404