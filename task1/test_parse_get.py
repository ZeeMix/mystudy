from task1 import pars


def test1_good_get():
    with open("tests/test1.txt", "r", encoding="utf-8") as http_text:
        http_request = http_text.read()
        assert pars(http_request) == {
            "type": "HTTP",
            "http_version": "1.1",
            "method": "GET",
            "path": "/hello.htm",
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


def test2_good_post():
    with open("tests/test2.txt", "r", encoding="utf-8") as http_text:
        http_request = http_text.read()
        assert pars(http_request) == {
            "type": "HTTP",
            "http_version": "1.1",
            "method": "POST",
            "path": "/cgi-bin/process.cgi",
            "raw_path": b"/cgi-bin/process.cgi",
            "query_string": b"",
            "headers": [
                ["User-Agent", "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)"],
                ["Host", "www.tutorialspoint.com"],
                ["Content-Type", "application/x-www-form-urlencoded"],
                ["Content-Length", "length"],
                ["Accept-Language", "en-us"],
                ["Accept-Encoding", "gzip, deflate"],
                ["Connection", "Keep-Alive"],
            ],
            "body": "licenseID=string&content=string&/paramsXML=string",
        }


def test3_good_post_longbody():
    with open("tests/test3.txt", "r", encoding="utf-8") as http_text:
        http_request = http_text.read()
        assert pars(http_request) == {
            "type": "HTTP",
            "http_version": "1.1",
            "method": "POST",
            "path": "/cgi-bin/process.cgi",
            "raw_path": b"/cgi-bin/process.cgi",
            "query_string": b"",
            "headers": [
                ["User-Agent", "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)"],
                ["Host", "www.tutorialspoint.com"],
                ["Content-Type", "application/x-www-form-urlencoded"],
                ["Content-Length", "length"],
                ["Accept-Language", "en-us"],
                ["Accept-Encoding", "gzip, deflate"],
                ["Connection", "Keep-Alive"],
            ],
            "body": "licenseID=string&content=string&/paramsXML=string\n\n\n\nlicenseID=string&content=string&/paramsXML=string",
        }


def test4_query_string():
    with open("tests/test4.txt", "r", encoding="utf-8") as http_text:
        http_request = http_text.read()
        assert pars(http_request) == {
            "type": "HTTP",
            "http_version": "1.1",
            "method": "POST",
            "path": "/cgi-bin/process.cgi",
            "raw_path": b"/cgi-bin/process.cgi",
            "query_string": b"name=ferret&color=purple",
            "headers": [
                ["User-Agent", "Mozilla/4.0 (compatible; MSIE5.01; Windows NT)"],
                ["Host", "www.tutorialspoint.com"],
                ["Content-Type", "application/x-www-form-urlencoded"],
                ["Content-Length", "length"],
                ["Accept-Language", "en-us"],
                ["Accept-Encoding", "gzip, deflate"],
                ["Connection", "Keep-Alive"],
            ],
            "body": "licenseID=string&content=string&/paramsXML=string\n\n\n\nlicenseID=string&content=string&/paramsXML=string",
        }
