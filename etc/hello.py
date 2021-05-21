bind = '0.0.0.0:8080'
def application(env, start_response):
    response_body = [
    	bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')
    ]
    #response_body = '\n'.join(response_body)
    status = '200 OK'
    headers = [
    	('content-type', 'text/plain')
    ]	

    start_response(status, headers)
    return response_body
