def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes(par+'\n', 'ascii') for par in env['QUERY_STRING'].split('&')]
    