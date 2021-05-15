#! /usr/bin/env python3

'''
Universal Dependencies for Tagalog
2014-06313  Aquino, Angelina A.

tokenize_text_to_conllu.py
Tokenizes a text file (without restrictions on newline location).
Prints the tokenization in the CoNLL-U format, with all other fields blank.

Arguments:
[1] input text filename
'''

import sys
from nltk.tokenize import sent_tokenize, word_tokenize

txt_file_name = sys.argv[1]
txt_file = open(txt_file_name, 'r', encoding='utf-8')
txt_lines = txt_file.readlines()
txt_file.close()

txt_running = ' '.join([line.rstrip() for line in txt_lines])
txt_sents = sent_tokenize(txt_running)
txt_words = [word_tokenize(sent) for sent in txt_sents]

for i in range(len(txt_sents)):
    sent = txt_sents[i]
    print('# text = ' + sent)

    words_running = ''

    for j in range(len(txt_words[i])):
        word = txt_words[i][j]

        if sent[len(words_running)] != word[0]:
            if (word == '``' or word == "''") and sent[len(words_running)] == '"':
                word = '"'

        words_running += word
        if len(words_running) != len(sent):
            if sent[len(words_running)] == ' ':
                misc = '_'
                words_running += ' '
            else:
                misc = 'SpaceAfter=No'
        else:
            misc = '_'

        print(str(j + 1) + '\t', end='') # ID
        print(word + '\t', end='') # FORM
        print('_\t', end='') # LEMMA
        print('_\t', end='') # UPOS
        print('_\t', end='') # XPOS
        print('_\t', end='') # FEATS
        print('_\t', end='') # HEAD
        print('_\t', end='') # DEPREL
        print('_\t', end='') # DEPS
        print(misc) # MISC

    print()
