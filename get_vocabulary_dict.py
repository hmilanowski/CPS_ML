#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    
    num_word = dict()
    
    with open('data/vocab.txt', newline='') as csv_file:
        spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for row in spamreader:
            split_str = row[0].split()
            number = int(split_str[0])
            word = split_str[1]
            num_word[number] = word

    return num_word
