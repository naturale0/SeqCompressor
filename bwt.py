#!python3
import numpy as np
import sys

def bw_transform(seq):
    # use ' ' as EOF char
    seq = seq + " "
    length = len(seq)
    seq = list(seq) * 2

    table = [seq[i:i+length] for i in range(length)]
    #table = [''] * length #np.zeros((length, length), dtype=str)
    #for i in range(length):
    #    table[i] = seq[i:i+length]

    table.sort()
    #table_np = np.asartable
    return "".join([row[-1] for row in table]) #''.join(table_np[:, -1])


def bw_recover(bw_seq):
    bw_seq = list(bw_seq)
    length = len(bw_seq)
    table = np.zeros((length, length), dtype=str)
    for i in range(1, length+1):
        if i > 1:
            table = table[np.argsort(table[:, -i+1], kind="mergesort")]
        table[:, -i] = bw_seq

    #print(table[:, -1] == " ")
    seq = table[table[:, -1] == " "][0]
    return "".join(seq[:-1])


if __name__ == "__main__":
    _, seq = sys.argv
    from itertools import groupby
    print(bw_transform(seq))
    print('')
    recovered = bw_recover(bw_transform(seq))
    print(recovered)
    print(seq)
    print('')
    print('Recovered: {}'.format(seq == recovered))
