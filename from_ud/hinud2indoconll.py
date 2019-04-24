#!/usr/bin/python3

import conllu
from functools import reduce
from hinud2indo import ud2indo
from udpos import udpos

def transform(record):
    token = record[1]
    lemma = record[2]
    pos = record[3]
    props = {ud2indo[tuple(p.split('='))] for p in record[5].split('|')}
    props = reduce(lambda x, y: x | y, props)
    props = props | {udpos[pos]}
    return (token, lemma, props)


def main(fn):
    sentences = conllu.ConllU(fn, transform)
    for sentence in sentences:
        for token, lemma, props in sentence:
            print('{}\t{}+{}'.format(token, lemma, '+'.join(props)))
        print()

if __name__ == '__main__':
    main('/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-test.conllu')
