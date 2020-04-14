from os.path import join, isdir, exists
from os import listdir, rmdir
from shutil import move

import sys
import re

tr_name = []
key_val = {}
key_idx = {}

val_name = []
val_idx = {}

with open("dic_from_words.txt") as f:
    for line in f:
        (key, val) = re.split(r'\t', line)
        tr_name.append(key)
        key_val[key] = val[:-1] # remove \n

with open("train.txt", "w") as f:
    for idx, _name in enumerate(tr_name):
        key_idx[_name] = idx
        for cnt in range(500):
            f.write(_name + "/"+_name+"_"+str(cnt)+".JPEG" + " " + str(idx)+"\n")

with open("val/val_annotations.txt") as f:
    for line in f:
        (_n, _k, _1, _2, _3, _4) = re.split(r'\t', line)
        val_name.append(_k)
        val_idx[_k] = key_idx[_k]

with open("val.txt", "w") as f:
    for idx, _name in enumerate(val_name):
        f.write("images/val_" + str(idx) +".JPEG" + " " + str(val_idx[_name]) + "\n")

    