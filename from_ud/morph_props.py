#!/usr/bin/env python3

import conllu

def get_props(fn):
    props = set()
    for sentence in conllu.ConllU(fn, lambda x: x[5]):
        for word in sentence:
            word_props = [tuple(x.split('=')) for x in word.split('|')]
            props.update(word_props)
    return props

def print_props(props):
    props = list(props)
    props.sort()
    for prop in props:
        print(prop)

def main(fns):
    props = set()
    for fn in fns:
        props.update(get_props(fn))
    print_props(props)

if __name__ == '__main__':
    main(['/Users/mortensen/Downloads/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-test.conllu',
          '/Users/mortensen/Downloads/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-train.conllu',
          '/Users/mortensen/Downloads/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-dev.conllu'])
