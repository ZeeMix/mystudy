def pars(request: str) -> dict:
    """Преобразование строки запроса к словарю"""
    request_dict = {}

    request_lines = request.splitlines()

    start_values = request_lines[0].split()

    full_path = start_values[1].split('?') if '?' in start_values[1] else [start_values[1], '']

    request_dict['method'] = start_values[0]
    request_dict['path'] = full_path[0]

    request_dict['raw_path'] = request_dict['path'].encode()

    request_dict['type'], request_dict['http_version'] = start_values[2].split('/')

    request_dict['query_string'] = full_path[1].encode()

    headers = []

    for ind in range(1, len(request_lines)):
        if request_lines[ind]:
            line_list = request_lines[ind].split(': ')
            headers.append([line_list[0], line_list[1]])
            request_dict['headers'] = headers
        else:
            request_dict['body'] = '\n'.join(request_lines[ind + 1:])
            return request_dict

    return request_dict
