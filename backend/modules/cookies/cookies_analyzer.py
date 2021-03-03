#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import browser_cookie3
import http.cookiejar
from collections import Counter
import time
import traceback
import json
import os
from datetime import datetime, timedelta


def process_data(json_cookie):
    """Get information from data cookie JSON

    Args:
        json_cookie (json): Json data from browser's cookies
    Return:
      [ ] Cookies per browser
      [ ] Domains per browser
      [ ] Domains Summarized
      [ ] Domains Summarized per browser
      [ ] Domains expired per browser
      [ ] Domains expired summarized
    """

    for browser in json_cookie:
        # Browser things
        cookie_domain = []
        for cookie in json_cookie[browser]:
            cookie_domain.append(cookie['domain'])

        print("Qty of cookies for {} is {}".format(
            browser, len(cookie_domain)))


def p_cookies():

    # File to improve performance
    cookies_file = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "cookies-browser.json")

    # Expiration of 1 day or cookie file
    expiration_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    print("Cookie file : {}".format(cookies_file))
    if (os.path.isfile(cookies_file)
        and (expiration_date < datetime.fromtimestamp(
            os.path.getmtime(cookies_file)).strftime('%Y-%m-%d'))):

        with open(cookies_file, 'r') as f:
            total = json.load(f)

    else:

        ref = ["chromium", "opera", "edge", "firefox", "chrome"]
        index = 0
        json_cookie = {}
        for cookie_fn in [browser_cookie3.chromium,
                          browser_cookie3.opera,
                          browser_cookie3.edge,
                          browser_cookie3.firefox,
                          browser_cookie3.chrome]:
            cookie_list = []
            try:
                for cookie in cookie_fn(domain_name=""):
                    cookie_item = {
                        "version": cookie.version,
                        "name": cookie.name,
                        "value": cookie.value,
                        "domain": cookie.domain,
                        "port": cookie.port,
                        "path": cookie.path,
                        "secure": cookie.secure,
                        "expires": cookie.expires,
                        "discard": cookie.discard,
                        "comment": cookie.comment,
                        "comment_url": cookie.comment,
                        "rfc2109": cookie.rfc2109,
                        "port_specified": cookie.port_specified,
                        "domain_specified": cookie.domain_specified,
                        "domain_initial_dot": cookie.domain_initial_dot,
                        "is_expired": cookie.is_expired()
                    }
                    cookie_list.append(cookie_item)
            except Exception as e:
                print(e)

            json_cookie[ref[index]] = cookie_list
            index += 1

        # Process data
        process_data(json_cookie)

        total = []
        total.append({'module': 'cookies'})
        status = []
        status.append({"code": 0})
        total.append({'status': status})
        total.append({'data': json_cookie})

        # Write cookie file
        with open(cookies_file, 'w') as f:
            f.write(json.dumps(total, ensure_ascii=True, indent=2))

    return total


def t_cookies():
    """Execute the extract cookies and handle error

    Returns:
        [string]: JSON with data
    """
    total = []
    tic = time.perf_counter()
    try:
        total = p_cookies()
    except Exception as e:
        traceback.print_exc()
        traceback_text = traceback.format_exc()
        total.append({'module': 'cookies'})

        status = []
        status.append({"code": 10,  # this code is arbitrary
                       "reason": "{}".format(e),
                       "traceback": traceback_text})
        total.append({"status": status})

    toc = time.perf_counter()
    print(f"Cookie - Response in {toc - tic:0.4f} seconds")

    return total


def output(data):
    """Print JSON

    Args:
        data (string): JSON
    """
    print(json.dumps(data, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    result = t_cookies()
    output(result)
