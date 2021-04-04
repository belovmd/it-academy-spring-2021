"""
                    Merged String Checker - раздел string

At a job interview, you are challenged to write an algorithm to check
if a given string, s, can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2
should be in the same order as in s.
The interviewer gives you the following example and
 tells you to figure out the rest from the given test cases.
For example:
'codewars' is a merge from 'cdw' and 'oears':
    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""


def compare_length(s, part1, part2):
    return len(s) == (len(part1) + len(part2))


def compare_chars(s, part1, part2):
    part_string_chars = set(part1).union(set(part2))
    diff_two_string = part_string_chars.symmetric_difference(set(s))
    return True if not diff_two_string else False


def compare_sequence_of_chars_simple(s, part1, part2):
    for chr_ in s:
        if part1 and chr_ == part1[0]:
            part1 = part1[1:]
            continue
        if part2 and chr_ == part2[0]:
            part2 = part2[1:]
            continue
        return False
    return True


def compare_sequence_of_chr(s, part1, part2):
    k = 0
    while True:
        if len(s) == 1:
            if part1 and s[0] == part1[0]:
                return True
            elif part2 and s[0] == part2[0]:
                return True
            else:
                return False
        elif part1 and part2 and part1[k] == part2[k]:
            k += 1
        elif part1 and part1[k] == s[k]:
            k = k if k != 0 else 1
            part1 = part1[k:]
            s = s[k:]
            k = 0
        elif part2 and part2[k] == s[k]:
            k = k if k != 0 else 1
            part2 = part2[k:]
            s = s[k:]
            k = 0
        elif not s:
            return True
        else:
            return False


def is_merge(s, part1, part2):
    if not compare_length(s, part1, part2):
        return False
    if not compare_chars(s, part1, part2):
        return False
    if compare_sequence_of_chars_simple(s, part1, part2):
        return True
    if compare_sequence_of_chars_simple(s, part2, part1):
        return True
    if compare_sequence_of_chr(s, part1, part2):
        return True
    return False


def print_merged_string_checker():
    print("\n", "-" * 40)
    print("\t\tTask4: Merged String Checker - 5kuy\n")
    print("s:{} \npart1: {} \npart2{} \nresult => {}\n".format(
        "Can we merge it? No, we can't", "Can merget? scn", " we iYe, we a!",
        is_merge("Can we merge it? No, we can't", "Can merget? scn", " we iYe, we a!", )))
    print("s:{} \npart1: {} \npart2{} \nresult => {}\n".format(
        "codewars", "cdw", "oears", is_merge("codewars", "cdw", "oears")))
    print("-" * 40)
