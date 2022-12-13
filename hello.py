def app(env, start_response):
    q_string = env.get('QUERY_STRING')
    params = q_string.split('&')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return params