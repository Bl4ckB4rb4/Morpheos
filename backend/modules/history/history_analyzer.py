#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from browser_history import get_history
from browser_history import browsers

import summarize

# Gathers the histories from all available browsers
#
# The object returned is of type <browser_history.generic.Outputs>
# The histories in [(datetime, url)] format can be accessed through outputs.histories
# Some useful methods of the returned object are to_json() and to_csv(), both returning strings
#
# One thing to note is that the data obtained from this method deosn't distinguish between
# browsers, meaning you can't find out which entry belongs to which browser
#
def fetch_all():
    return get_history()

# Gathers information from specific browsers
#
# The browsers to be analyzed are specified in the first argument, which is an array of strings
# The output format is { browser_name: <browser_history.generic.Outputs> }; you can check
# pesos/browser_history's documentation for details of the Outputs object
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
    data = fetch_specific(['Firefox'])['Firefox']
    print(data)
    print(summarize.summarize_by_domain(data.histories))
    print(summarize.summarize_by_path(data.histories))
