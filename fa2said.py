#!python3
import sys
import os
import numpy as np
#import multiprocessing as mp
from itertools import groupby
from bwt import bw_transform
from utils import *


def run2byte(said_seq):
    run_ints = []
    # 1 byte: 8 bits [00000000]
    ## first 3 bits represents BASE TYPE (ATGCN)
    ## last 5 bits represents REPEATS (how many times it occurs consequently)

    for baseint, left, times in said_seq:
        if times < 1:
            run_ints.append(baseint + left)
        else:
            [run_ints.append(baseint + 31) if i <= times \
             else run_ints.append(baseint + left) \
             for i in range(1, times+2)]

    return bytes(run_ints)


def seq2said(seq):
    base2byte = Base2Byte().data
    # [(baseint, run_length, 0)] --- if run_length <= 32
    # [(baseint, run_length%32, run_length//32)] -- if run_length <= 32
    runs = [(base2byte[base], len(list(run))) for base, run in groupby(seq)]
    return [(base, run, 0) if run <= 31 \
            else (base, run%31, run//31) \
            for base, run in runs]


def seq2byte(seq, use_bwt=False):
    if use_bwt:
        return run2byte(seq2said(bw_transform(seq)))
    return run2byte(seq2said(seq))


def main(fa_fname):
    out_name = os.path.splitext(fa_fname)[0] + ".said"
    wb = open(out_name, "wb")
    r = open(fa_fname, "r")

    name = None
    for line in r:
        if line.startswith(">"):
            if name is not None:
                byte_seq = seq2byte(seq)
                wb.write(name.encode() + b"\n" + byte_seq + b"\n")
                #print(name)
                #print(seq)

            # Get a NEW sequence name / Erase and initialize NEW seq
            name = line[1:].split()[0]
            seq = ""
            #sys.stdout.write('\r{}'.format(name))
            #sys.stdout.flush()
        else:
            seq += line.strip().upper()

    byte_seq = seq2byte(seq)
    wb.write(name.encode() + b"\n" + byte_seq + b"\n")
    #print(name)
    #print(seq)

    wb.close()
    r.close()

    return "\n* DONE"

if __name__ == "__main__":
    print (main(sys.argv[1]))
