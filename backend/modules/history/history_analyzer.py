#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from browser_history import get_history
from browser_history import browsers

from urllib.parse import urlparse

# Gathers the histories from all available browsers
#
# The histories in [(datetime, url)] format can be accessed through outputs.histories
# Some useful methods of the returned object are to_json() and to_csv(), both returning strings
# 
def fetch_all():
    return get_history()

# Gathers information from specific browsers
#
# The browsers to be analyzed are specified in the first argument, which is an array of strings
# 
def fetch_specific(args):
    dict_browsers = {
            'Brave': browsers.Brave,
            'Chrome': browsers.Chrome,
            'Chromium': browsers.Chromium,
            'Edge': browsers.Edge,
            'Firefox': browsers.Firefox,
            'Opera': browsers.Opera,
            'OperaGX': browsers.OperaGX,
            'Safari': browsers.Safari
    }

    output = {}

    for browser_name in args:
        if browser_name in dict_browsers:
            try:
                brows_init = dict_browsers[browser_name]()
            
                output[browser_name] = brows_init.fetch_history()
            except AssertionError:
                print('INFO: browser {} not supported'.format(browser_name))

    return output

if __name__ == '__main__':
    print(fetch_all().histories)
