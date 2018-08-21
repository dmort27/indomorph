#!/usr/bin/env python3

import fstinter
import glob
import os.path
import sys
import multiprocessing
from functools import partial


def get_cost(aml):
    analysis, morphs, lemma = aml
    c = 0
    if 'Nom' in morphs:
        c += 1
    if len(lemma) < 2:
        c += 4
    return c


def analyze_line(fst, line):
    tokens = line.strip().split()
    tem = 'w:{}~l:{}~m:{}'
    analyses = fst.analyses(tokens)
    return ' '.join([tem.format(w, l, '+'.join([] if len(p) < 2 else p[1:]))
                     for (w, (p, l))
                     in analyses])


def main(fstpath, path_in, path_out):
    pool = multiprocessing.Pool(processes=16)
    fst = fstinter.FST(fstpath, get_cost)
    fst_analyze_line = partial(analyze_line, fst)
    for fnin in glob.glob(path_in):
        fnout = os.path.join(path_out, os.path.basename(fnin))
        with open(fnin, encoding='utf-8') as fin:
            lines = fin.readlines()
            out_data = pool.map(fst_analyze_line, lines)
            out_data = '\n'.join(out_data)
        with open(fnout, 'w', encoding='utf-8') as fout:
            fout.write(out_data)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
