"""
            Scramblines - раздел string
Complete the function scramble(str1, str2) that returns true if a portion
of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered

Input strings s1 and s2 are null terminated.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""


def scramble1(s1, s2):   # STDERR Execution Timed Out (12000 ms)
    for char in s2:
        pos = s1.find(char)
        if pos == -1:
            return False
        s1 = s1[:pos] + s1[pos+1:]
    return True


def scramble2(s1, s2):   # STDERR Execution Timed Out (12000 ms) =(
    for char in s2:
        if not(char in s2):
            return False
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        if count_s1 < count_s2:
            return False
    return True


def scramble(s1, s2):   # STDERR Execution Timed Out (12000 ms) =(
    if set(s2).issubset(s1):
        if len(s2) == len(set(s2)):
            return True
        for char in s2:
            if s1.count(char) < s2.count(char):
                return False
        return True
    return False


def print_scramble():
    print("\n", "-" * 40)
    print("\t\tTask3: Scramblines - 5kuy")
    print("rkqodlw and world =>", scramble("rkqodlw", "world"))
    print("katas and steak =>", scramble("katas", "steak"))
    print("-" * 40)
