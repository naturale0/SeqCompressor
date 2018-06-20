#!python3
import sys
import os
import multiprocessing as mp
import LZ77
from utils import *

def said2seq(byte):
    bin2base = Bin2Base().data
    said_list = [dec2binstr(b) for b in bytearray(byte)]
    seq = "".join([bin2base[b[:3]] * int(b[3:], 2) for b in said_list])
    return "\n".join([seq[i:i+60] for i in range(0, len(seq), 60)])

def main(said_name):
    out_name = os.path.splitext(said_name)[0] + ".s.fa"
    try:
        n_cpu = mp.cpu_count() // 2
        pool = mp.Pool(processes=n_cpu)
        multi = True
    except PermissionError:
        multi = False

    rb = open(said_name, "rb")
    w = open(out_name, "w")

    lb = rb.readline()
    while lb:
        name = ">" + "".join([chr(i) for i in lb.strip()]) + "\n"
        lb = rb.readline()
        seq_bytes = lb[:-1]
        seq = said2seq(seq_bytes) + "\n"

        #print(name)
        #print(seq)
        w.write(name + seq)
        lb = rb.readline()
    w.close()
    rb.close()

    return "\n* DONE"


if __name__ == "__main__":
    print( main(sys.argv[1]) )
