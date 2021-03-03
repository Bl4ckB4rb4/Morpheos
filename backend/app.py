#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, request

# Importacion de nuestras funciones
from modules.cookies.cookies_analyzer import f_cookies
from modules.history import top_domains_global

app = Flask(__name__)


# Las URLs que ejecutaran nuestras funciones
@app.route("/cookies")
def p_cookies():
    return f_cookies()


@app.route('/history/top-domains')
def top_domains():
    '''
        Top domains

        For the specified browser/s, looks for the most visited domains. The
        number of domains to look for can be specified via the query parameter
        'n', and the browser can be specified through the 'browser' parameter
        to fetch from only one history or from all of them, if 'browser'
        is set to 'all'. If no query is given, 'n' is set to 10 and 'browser'
        to 'all'. Currently, specific browser searches are not developed
    '''
    browser = request.args.get('browser', default='all')
    qty = int(request.args.get('n', default=10))
    response_json = {'command': 'top-domains'}

    if browser == 'all':
        try:
            response_json['status'] = 'OK'
            response_json['topDomains'] = top_domains_global(qty)

        except Exception as e:
            response_json['status'] = 'ERROR'
            response_json['message'] = e.args[0]

    else:
        response_json['status'] = 'FAIL'
        response_json['message'] = 'Function not implemented'

    return response_json


if __name__ == '__main__':
    app.run()
