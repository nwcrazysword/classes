#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-08 12:58:54
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword

import re
# from collections import Counter

# read content from text file
def getcontent(fpath):
    with open(fpath, 'r') as f:
        return f.read(8089)

# clean up the content
def cleancontent(content):
    seplist = '.\-,():'
    content = re.sub(r'[%s]+' % seplist, ' ', content)
    return content


# get the list of the word
def genwords(content):
    def isword(word):
        word = word.strip()
        if word:
            return True
        else:
            return False
    return filter(isword, content.split())

# count and sorted
def countwords(words):
    rdict = {}
    for word in words:
        num = rdict.get(word, 0)
        rdict[word] = num + 1
    return sorted(rdict.items(), key=lambda x: x[1], reverse=True)

# save to file
def saveresult(rpath, rlist):
    lines = ''
    with open(rpath, 'w') as f:
        for word, num in rlist:
            line = '%-15s -> %2d \n' %(word,num)
            lines += line
        f.write(lines)

def main():
    fpath = r'doc.txt'
    rpath = r'result.txt'

    content = getcontent(fpath)
    content = cleancontent(content)
    words = genwords(content)
    rlist = countwords(words)
    saveresult(rpath, rlist)

if __name__ == '__main__':
    main()
