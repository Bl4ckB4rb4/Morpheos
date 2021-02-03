#!/usr/bin/env python
# -*- encoding: utf-8 -*-

## History analizer
#
# This is the main file for this module, where the test cases should be developed and where
# the functions called by the API must be located it depends on several other files, mainly:
#
# fetcher.py    - Uses the browser_history library to actually obtains the histories
# summarize.py  - Collects the data to analyze repetitions and patterns. Its outputs may easily be represented in a histogram
#
# Other files may be added as needed while the development continues

from modules.history.fetcher import fetch_all
from modules.history.summarize import summarize_by_domain
from modules.history.statistics import most_repeated

def top_domains_global(n):
    data = fetch_all()
    if len(data) == 0:
        raise Exception('No history entries found')

    summarized = summarize_by_domain(data)
    top_n = most_repeated(summarized, n)

    return top_n

if __name__ == '__main__':
    data = fetch_all()

    print(data)
