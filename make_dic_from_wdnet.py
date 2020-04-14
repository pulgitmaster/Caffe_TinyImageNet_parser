import sys
import re

wordnet = {}
with open("words.txt") as f:
    for line in f:
        (key, val) = re.split(r'\t', line)
        wordnet[key] = val[:-1] # remove \n

#print('print(wordnet[\'n02124075\']) : ', wordnet['n02124075'])

wnids = {}
with open("wnids.txt") as f:
    for line in f:
        wnid = {}
        key = line.split()[0]
        wnid[key] = ''
        wnids.update(wnid)

#print(winds)
for key in wnids.keys():
    wnids[key] = wordnet[key]
#    winds.update(key=wordnet[key])

# print(winds)
with open("dic_from_words.txt", "w") as f:
    for word in wnids:
        f.write(word + '\t' + wnids[word] + '\n')