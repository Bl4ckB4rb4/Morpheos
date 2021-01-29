#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from browser_history import get_history
from browser_history import browsers

# Gathers the histories from all available browsers
#
# The return object is an array with all the history entries encountered,
# with format (datetime, url)
#
# One thing to note is that the data obtained from this method deosn't distinguish between
# browsers, meaning you can't find out which entry belongs to which browser
#
def fetch_all():
    return get_history().histories

# Gathers information from specific browsers
#
# The browsers to be analyzed are specified in the first argument, which is an array of strings
# The output format is { browser_name: [ (datetime, url) ] }; you can check
# pesos/browser_history's documentation for details of the Outputs object
#
def fetch_specific(*args):
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
            
                output[browser_name] = brows_init.fetch_history().histories
            except AssertionError as err:
                print('INFO: browser {} not supported'.format(err))

    return output
