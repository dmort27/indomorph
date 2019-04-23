#!/usr/bin/env python3

import conllu
import epitran

def main(treebanks):
    nouns = {}
    # epi = epitran.Epitran('hin-Deva')
    for treebank in treebanks:
        for sentence in conllu.ConllU(treebank, conllu.lemma_pos_morph_tr):
            for lemma, pos, props in sentence:
                # final_seg = epi.trans_list(lemma)[-1]
                if pos == 'NOUN' and 'Gender' in props:
                    if props['Gender'] == 'Fem':
                        if lemma[-1] == 'ि':
                            classnum = 'III'
                        else:
                            classnum = 'IV'
                    elif props['Gender'] == 'Masc':
                        if lemma[-1] == 'ा':
                            classnum = 'I'
                        else:
                            classnum = 'II'
                    nouns[lemma] = classnum
    for lemma, classnum in sorted(nouns.items()):
        print(f'{lemma} Class{classnum} ;')

if __name__ == '__main__':
    main(['/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-train.conllu',
          '/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-dev.conllu',
          '/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-test.conllu'])
