#!/usr/bin/python3

import re

class ConllU:
    def __init__(self, fn, transform):
        self.fn = fn
        self.transform = transform

    def __iter__(self):
        sentence = []
        with open(self.fn, encoding='utf-8') as f:
            for word in f:
                word = word[:-1]
                word = re.sub('#.*', '', word)
                if re.match('^\s*$', word):
                    if sentence:
                        yield list(map(self.transform, sentence))
                        sentence = []
                else:
                    sentence.append(word.split('\t'))
            yield sentence
