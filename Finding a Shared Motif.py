# -*- coding: utf-8 -*-

"""This script finds a longest common motif between sequences"""


file = r"fasta_sequences.txt" # requires fasta sequence file input

# function that takes fasta file and returns only the sequences
def get_fasta_seqs(fasta_file):
    with open(fasta_file, 'r') as open_file:
        readlines = open_file.readlines()
    sequences = []
    seq = ""
    for line in readlines:
        if line.startswith('>'):
            sequences.append(seq)
            seq=""
        else:
            seq += line.rstrip()
    sequences.append(seq)
    sequences.pop(0)
    return sequences
        
        

# function to test if a pattern (eg. 'ATCG') is found in all sequences in a list
def in_all(pattern, list_of_seqs):
    tally = []
    for seq in list_of_seqs:
        if pattern in seq:
            continue
        else:
            return False
            break
    return True
    
# function to find all substrings of a sequence starting with the same letter
def find_substring(sequence):
    sub_seqs = []
    count = 1
    for i in range(len(sequence)):
        sub_seqs.append(sequence[:i+1])
        count += 1
    return sub_seqs

# function to find all substrings starting from any letter (includes above function)
def get_all_subs(sequence):
    result = []
    seq = sequence
    for i in range(len(sequence)):
        one = find_substring(seq)
        result.extend(one)
        seq = seq[1:]
    return result
    
# combines all functioality into a single function. 
# takes fasta file of sequences and returns longest common shared motif
# it only returns one if there are many of equal length
def longest_shared_motif(fasta_file):
    sequences = get_fasta_seqs(fasta_file)
        
    substrings = get_all_subs(sequences[0])

    common_substrings = []
    for pattern in substrings:
        if in_all(pattern, sequences):
            common_substrings.append(pattern)
    main = sorted(common_substrings, key = len)
    return main[-1]
    
        
print(longest_shared_motif(file))