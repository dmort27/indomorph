#!/usr/bin/env python3

import mmap
import fstinter
import glob
import os.path
import sys
import tqdm

def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines

def get_cost(aml):
    analysis, morphs, lemma = aml
    c = 0
    if 'Nom' in morphs:
        c += 1
    if len(lemma) < 2:
        c += 4
    return c

def main(fstpath, path_in, path_out):
    fst = fstinter.FST(fstpath, get_cost)
    for fnin in glob.glob(path_in):
        print("Analyzing {}...".format(fnin))
        fnout = os.path.join(path_out, os.path.basename(fnin))
        with open(fnin, encoding='utf-8') as fin, open(fnout, 'w', encoding='utf-8') as fout:
            for line in tqdm.tqdm(fin, total=get_num_lines(fnin)):
                output = []
                tokens = line.strip().split()
                analyses = fst.analyses(tokens)
                for (token, (morphs, lemma)) in analyses:
                    props = [] if len(morphs) < 2 else morphs[1:]
                    output.append('w:{}~l:{}~m:{}'.format(token,
                                                          lemma,
                                                          '+'.join(props)))
                print(' '.join(output), file=fout)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
