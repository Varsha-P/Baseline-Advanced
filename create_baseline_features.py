#!/usr/bin/env python3

"""hw3_corpus_tools.py: CSCI544 Homework 3 Corpus Code

USC Computer Science 544: Applied Natural Language Processing

Provides two functions and two data containers:
get_utterances_from_file - loads utterances from an open csv file
get_utterances_from_filename - loads utterances from a filename
DialogUtterance - A namedtuple with various utterance attributes
PosTag - A namedtuple breaking down a token/pos pair

This code is provided for your convenience. You are not required to use it.
Feel free to import, edit, copy, and/or rename to use in your assignment.
Do not distribute."""

__author__ = "Christopher Wienberg"
__email__ = "cwienber@usc.edu"

from collections import namedtuple
import csv
import glob
import os
import sys

def main():

    def get_utterances_from_file(dialog_csv_file):
        """Returns a list of DialogUtterances from an open file."""
        reader = csv.DictReader(dialog_csv_file)
        return [_dict_to_dialog_utterance(du_dict) for du_dict in reader]

    def get_utterances_from_filename(dialog_csv_filename):
        """Returns a list of DialogUtterances from an unopened filename."""
        with open(dialog_csv_filename, "r") as dialog_csv_file:
            return get_utterances_from_file(dialog_csv_file)

    DialogUtterance = namedtuple(
    "DialogUtterance", ("act_tag", "speaker", "pos", "text"))

    DialogUtterance.__doc__ = """\
An utterance in a dialog. Empty utterances are None.

act_tag - the dialog act associated with this utterance
speaker - which speaker made this utterance
pos - a list of PosTag objects (token and POS)
text - the text of the utterance with only a little bit of cleaning"""

    PosTag = namedtuple("PosTag", ("token", "pos"))

    PosTag.__doc__ = """\
A token and its part-of-speech tag.

token - the token
pos - the part-of-speech tag"""

    def _dict_to_dialog_utterance(du_dict):
        """Private method for converting a dict to a DialogUtterance."""

    # Remove anything with 
        for k, v in du_dict.items():
            if len(v.strip()) == 0:
                du_dict[k] = None

    # Extract tokens and POS tags
        if du_dict["pos"]:
            du_dict["pos"] = [
                PosTag(*token_pos_pair.split("/"))
                for token_pos_pair in du_dict["pos"].split()]
        return DialogUtterance(**du_dict)
    inputFile = sys.argv[1]
    A = get_utterances_from_filename(inputFile)
    first = dict()
    first = A[0]
    speaker = first[1]
    count = 0
    for i in A:
        count += 1
        d = dict()
        d = i
        if(d[0] is not None):
            print(d[0],end="\t")
        else:
            print("abcde",end="\t")
        if(count == 1):
            print("first_seq",end='\t')
        if(d[1]==speaker):
            print("",end="")
        else:
            speaker = d[1]
            print("sp_change",end="\t")
        if(d[2] is not None):
            dd = dict()
            dd = d[2]
            for m in dd:
                if(m[0]==":"):
                    print('token_colon',end="\t")
                elif(m[0]=="\\"):
                    print('token_backslash',end="\t")
                else:
                    print('token_'+m[0],end="\t")
            for k in dd:
                if(k[1]==":"):
                    print('pos_colon',end="\t")
                elif(k[1]=='\\'):
                    print('pos_backslash',end="\t")
                else:
                    print('pos_'+k[1],end="\t")
        else:
            dd = dict()
            dd = d[3]
            print('notokens_'+dd,end="\t")
        print()
    print()

if __name__=="__main__":main()
