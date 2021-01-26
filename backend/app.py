#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask

# Importacion de nuestras funciones
from modules.cookies.cookies_analyzer import f_cookies

app = Flask(__name__)


# Las URLs que ejecutaran nuestras funciones
@app.route("/cookies")
def p_cookies():
    return f_cookies()


if __name__ == '__main__':
    app.run()
