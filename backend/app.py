#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, request

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
        data = top_domains_global(qty)

    if len(data) == qty:
        return {
                'status': 'OK',
                'command': 'top-domains',
                'topDomains': data
        }
    else:
        return {
                'status': 'ERROR',
                'commands': 'top-domains'
        }

if __name__ == '__main__':
    app.run()
