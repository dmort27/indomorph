#!/usr/bin/env python3

from subprocess import Popen, PIPE
import regex as re

class FST(object):
    def __init__(self, fst=None, get_cost=None):
        self.fst = fst
        self._get_cost = get_cost

    def _to_morphs(self, analysis):
        try:
            morphs = analysis.split('+')
            if morphs[0] == '':
                return morphs[1:]
            else:
                return morphs
        except IndexError:
            return []

    def _get_lemma(self, morphs):
        if morphs:
            return morphs[0]
        else:
            return ''

    def _get_best_analysis(self, analyses):
        morph_list = [self._to_morphs(x) for x in analyses]
        lemma_list = [self._get_lemma(x) for x in morph_list]
        costs = [self._get_cost(x)
                 for x in zip(analyses, morph_list, lemma_list)]
        try:
            sorted_list = sorted(zip(list(costs), morph_list, lemma_list))
            _, morphs, lemma = sorted_list[0]
            return (morphs, lemma)
        except IndexError:
            return (None, None)

    def analyses(self, tokens):
        token_list = '\n'.join(tokens)
        pipe = Popen(['flookup', '-a', '-x', self.fst],
                     stdout=PIPE, stdin=PIPE)
        analyses, resp = pipe.communicate(input=token_list.encode('utf-8'))
        analyses = analyses.decode('utf-8').strip()
        analysis_list = []
        for token, token_analyses in zip(tokens, analyses.split('\n\n')):
            morphs, lemma = self._get_best_analysis(token_analyses.split('\n'))
            if lemma == '?':
                analysis_list.append(([token], token))
            elif lemma:
                analysis_list.append((morphs, lemma))
            else:
                analysis_list.append(([token], token))
        return zip(tokens, analysis_list)
