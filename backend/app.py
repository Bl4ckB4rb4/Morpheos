#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, request, make_response

# Importacion de nuestras funciones
from modules.cookies.cookies_analyzer import f_cookies
from modules.history.history_analyzer import top_domains_global

app = Flask(__name__)


# Las URLs que ejecutaran nuestras funciones
@app.route("/cookies")
def p_cookies():
    return f_cookies()

@app.route('/history/top-domains')
def top_domains():
    browser = request.args.get('browser', default='all')
    qty = int(request.args.get('n', default=10))
    data = []
    if browser == 'all':
        try:
            data = top_domains_global(qty)
        except Exception as e:
            return make_response({
                'status': 'ERROR',
                'command': 'top-domains',
                'message': e.args[0]
                }, 500)

    return make_response({
            'status': 'OK',
            'command': 'top-domains',
            'topDomains': data
    }, 200)

if __name__ == '__main__':
    app.run()
