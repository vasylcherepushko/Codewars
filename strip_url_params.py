# Link to this kata
# https://www.codewars.com/kata/strip-url-params

def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url

    queries = url.split('?')[1].split('&')
    params = [query.split('=')[0] for query in queries]
    for i in range(len(params) - 1, -1, -1):
        if params[i] in params[0:i] or params[i] in params_to_strip:
           queries.pop(i)

    return '{0}?{1}'.format(url.split('?')[0], '&'.join(queries))