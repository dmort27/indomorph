#!/usr/bin/python3

import re


def morph_to_dict(props):
    """Convert morphological props to a dictionary"""
    if props == '_':
        return {}
    else:
        return {k: v for (k,v)
                in [x.split('=') for x in props.split('|')]}


def lemma_pos_morph_tr(token):
    """Lemma and morphological props as dictionary"""
    return (token[2], token[3], morph_to_dict(token[5]))


class ConllU:
    def __init__(self, fn, transform):
        self.fn = fn
        self.transform = transform

    def __iter__(self):
        sentence = []
        with open(self.fn, encoding='utf-8') as f:
            for word in f:
                word = word[:-1]
                if re.match('#.*', word):
                    continue
                elif re.match('^\s*$', word):
                    if sentence:
                        yield sentence
                        sentence = []
                else:
                    sentence.append(self.transform(word.split('\t')))
            yield sentence
