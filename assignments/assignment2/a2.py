def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1

def is_valid_sequence(dna):
    for char in dna:
        if not(char in 'ATCG'):
            return False
    return True

def insert_sequence(dna1, dna2, x):
    
    return dna1[:x] + dna2 + dna1[x:]

def get_complement(dna):
    if dna == "A":
        return "T"
    elif dna == "T":
        return "A"
    elif dna == "C":
        return "G"
    elif dna == "G" :
        return "C"
    else:
        return "error"
        

def get_complementary_sequence(dna):
    complement = ""
    for char in dna:
        complement = complement + get_complement(char)
    return complement



