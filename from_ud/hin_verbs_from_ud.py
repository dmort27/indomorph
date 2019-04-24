#!/usr/bin/env python3

import conllu
import epitran

def main(treebanks):
    words = {}
    # epi = epitran.Epitran('hin-Deva')
    for treebank in treebanks:
        for sentence in conllu.ConllU(treebank, conllu.lemma_pos_morph_tr):
            for lemma, pos, props in sentence:
                if pos == 'VERB':
                    words[lemma] = props
    for lemma, classnum in sorted(words.items()):
        print(f'{lemma} Suffix ;')

if __name__ == '__main__':
    main(['/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-train.conllu',
          '/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-dev.conllu',
          '/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-test.conllu'])
