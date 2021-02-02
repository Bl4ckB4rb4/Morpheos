#!/usr/bin/env python
# -*- encoding: utf-8 -*-

### Statistics
#
# This file holds functions to be used with the results of 
# sumarizations (see file summarize.py).

def most_repeated (summarized, n):
    '''
        Looks for most repeated items in summarization

        This function looks for the most repeated keys in a summarization.
        Given that all summarizations defined in summarize.py have the format
            { key_str: qty_of_repetitions }
        , the output will have the form
            [ (key_str, qty_of_repetitions) ]
        , limited to a length of n, and in descending order
    '''
    return sorted(summarized.items(), key=lambda entry: entry[1], reverse=True)[:n]
