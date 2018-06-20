#!python3
import sys
import os
import multiprocessing as mp
import LZ77
from utils import *


def seq2twobit(seq):
    base2bit = Base2Bit().data
    bits = [base2bit[base] for base in seq]
    return ["".join(bits[i:i+4]) for i in range(0, len(bits), 4)]

def twobit2bytes(twobit):
    bit_seq = bytes(map(lambda x: int(x, 2), twobit))
    n_placehold = bytes([8 - len(twobit[-1])])
    return bit_seq, n_placehold

def pipeline(seq):
    return twobit2bytes(seq2twobit(seq))

def name2lz77(name):
    return LZ77.encode(name.encode())

def main(fa_fname, idx=False):
    out_name = os.path.splitext(fa_fname)[0] + ".two"
    if idx:
        idx_name = os.path.splitext(fa_fname)[0] + ".idx"

    try:
        n_cpu = mp.cpu_count() // 2
        pool = mp.Pool(processes=n_cpu)
        multi = True
    except PermissionError:
        multi = False

    wb = open(out_name, "wb")
    r = open(fa_fname, "r")

    name = None
    _names, _seqs = [], []
    buffer = b""
    if idx: _idx = []
    for line in r:
        if line.startswith(">"):
            if name is not None:
                _seqs.append(seq)
                if len(_names) == n_cpu*10:
                    if multi:
                        bit_seqs = pool.map(pipeline, _seqs)
                    else:
                        bit_seqs = map(pipeline, _seqs)

                    for name, (bit_seq, n_placehold) in zip(_names, bit_seqs):
                        buffer += name.encode() + b"\n" \
                                + bit_seq.replace(b"\n", br"\n") + b"\n" \
                                + n_placehold + b"\n"
                    if idx:
                        _idx += _names

                    wb.write(buffer)
                    buffer = b""
                    _names.clear()
                    _seqs.clear()

            # Get a NEW sequence name / Erase and initialize NEW seq
            name = line[1:].split()[0]
            seq = ""
            _names.append(name)
        else:
            seq += line.strip().upper()

    # write last seq to file
    if len(_names) > 0:
        _seqs.append(seq)
        if multi:
            bit_seqs = pool.map(pipeline, _seqs)
        else:
            bit_seqs = map(pipeline, _seqs)

        for name, (bit_seq, n_placehold) in zip(_names, bit_seqs):
            #print(seq2twobit(seq))
            wb.write(name.encode() + b"\n" \
                   + bit_seq.replace(b"\n", br"\n") + b"\n" \
                   + n_placehold + b"\n")
        if idx:
            _idx += _names

    if idx:
        with open(idx_name, "w") as w:
            [w.write(name+"\n") for name in _idx]

    return "\n* DONE"

if __name__ == "__main__":
    print (main(sys.argv[1]))
