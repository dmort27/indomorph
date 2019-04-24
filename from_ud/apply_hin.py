#!/usr/bin/env python3

from subprocess import Popen, PIPE
import conllu

def main(fstfile, conllufn):
    for sentence in conllu.ConllU(conllufn, lambda x: x[1]):
        tokens = '\n'.join(sentence)
        pipe = Popen(['flookup', '-a', '-x', fstfile],
                     stdout=PIPE, stdin=PIPE)
        analyses, resp = pipe.communicate(input=tokens.encode('utf-8'))
        analyses = analyses.decode('utf-8').strip()
        for token, parses in zip(sentence, analyses.split('\n\n')):
            parses = parses.split('\n')
            # parse = sorted(parses, reverse=True, key=lambda x: len(x))[0]
            parse = '|'.join(parses)
            print(f'{token}\t{parse}')
        print()

if __name__ == '__main__':
    main('../indomorph/hin/hin.fst',
         '/Users/mortensen/Data/Universal Dependencies 2.3/ud-treebanks-v2.3/UD_Hindi-HDTB/hi_hdtb-ud-test.conllu')
