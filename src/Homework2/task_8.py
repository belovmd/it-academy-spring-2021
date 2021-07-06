"""
Complete the function that takes two integers (a, b, where a < b)
and return an array of all integers between the input parameters, including them.


"""


def between(a, b):
    lst = []
    if a < b:
        for i in range(a, b + 1):
            lst.append(i)
    return lst


print(between(-2, 2))

"""
Deoxyribonucleic acid, DNA is the primary information
storage molecule in biological systems.
It is composed of four nucleic acid bases Guanine ('G'),
Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells.
RNA differs slightly from DNA its chemical structure and contains no Thymine.
In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

"""


def dna_to_rna(dna):
    rna = dna
    if 'T' in dna:
        rna = dna.replace('T', 'U')

    return rna


"""
You're at the zoo... all the meerkats look weird.
Something has gone terribly wrong - someone has
gone and switched their heads and tails around!

Save the animals by switching them back.
You will be given an array which will have three values (tail, body, head).
It is your job to re-arrange the array so that the animal
is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests:
you have to change the element positions with the same exact logics
"""


def reverse(arr):
    return arr[::-1]
