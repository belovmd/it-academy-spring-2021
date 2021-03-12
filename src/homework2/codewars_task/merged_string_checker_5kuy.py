"""
                    Merged String Checker

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


def compare_sequence_of_chars(s, part1, part2):
    for chr in s:
        if part1 and chr == part1[0]:
            part1 = part1[1:]
            continue
        if part2 and chr == part2[0]:
            part2 = part2[1:]
            continue
        return False
    return True


def is_merge(s, part1, part2):
    if not compare_length(s, part1, part2):
        return False
    if not compare_chars(s, part1, part2):
        return False
    if compare_sequence_of_chars(s, part1, part2):
        return True
    return False

