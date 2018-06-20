#!python3
import sys
import os
import multiprocessing as mp
import LZ77
from utils import *

def bytearr2seq(byte, n_placehold):
    trim = n_placehold // 2
    byte2seq = Byte2Seq().data
    seq_list = [byte2seq[dec2binstr(b)] for b in list(byte)]
    seq_list[-1] = seq_list[-1][trim:]
    return "\n".join(["".join(seq_list[i:i+15]) for i in range(0, len(seq_list), 15)])

def main(two_name):
    out_name = os.path.splitext(two_name)[0] + ".2.fa"
    try:
        n_cpu = mp.cpu_count() // 2
        pool = mp.Pool(processes=n_cpu)
        multi = True
    except PermissionError:
        multi = False

    rb = open(two_name, "rb")
    w = open(out_name, "w")

    lb = rb.readline()
    while lb:
        name = ">" + "".join([chr(i) for i in lb])
        lb = rb.readline()
        seq_bytes = lb[:-1].replace(br"\n", b"\n")
        lb = rb.readline()
        n_placehold = int.from_bytes(lb.strip(), "little")
        seq = bytearr2seq(seq_bytes, n_placehold) + "\n"

        #print(name)
        #print(seq)
        w.write(name + seq)
        lb = rb.readline()
    w.close()
    rb.close()

    return "* DONE"


if __name__ == "__main__":
    print( main(sys.argv[1]) )
