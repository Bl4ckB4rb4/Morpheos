#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, jsonify

# Import our functions
from modules.cookies.cookies_analyzer import t_cookies

app = Flask(__name__)


# The URLs that execute our functions
@app.route("/cookies")
def p_cookies():
    res = t_cookies()
    return jsonify(result=res)


if __name__ == '__main__':
    app.run()
