#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.parse import urlparse


def summarize_generic(histories, get_key_lambda):
    '''
        Generic tmeplate for various possible operations with histories

        The idea is to return an output as { key: amount }
        The key is provided by the get_key_lambda argument,
        which is then used to classify the whole history

        In order to use custom get_key lambdas keep in mind that
        they must take a single argument, which is a history entry
        with format (datetime, url)
    '''
    summarized = {}

    for entry in histories:
        if get_key_lambda(entry) in summarized:
            summarized[get_key_lambda(entry)] += 1
        else:
            summarized[get_key_lambda(entry)] = 1

    return summarized


def summarize_by_domain(histories):
    '''
        Counts how many entries there are with equal domains

        Uses the urllib library for parsing the urls
    '''
    def get_key(entry):
        return urlparse(entry[1]).netloc

    return summarize_generic(histories, get_key)


def summarize_by_path(histories):
    '''
        Counts how many entries there are with equal paths
        (domain+path, without queries or fragments)
        Uses the urllib library for parsing the urls
    '''

    def get_key(entry):
        parsed_url = urlparse(entry[1])
        return parsed_url.netloc + parsed_url.path

    return summarize_generic(histories, get_key)
