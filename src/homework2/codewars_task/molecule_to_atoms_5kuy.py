"""
                              Molecule to atoms - раздел parsing

For a given chemical formula represented by a string, count the number
of atoms of each element contained in the molecule and return an object
 (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

As you can see, some formulas have brackets in them. The index
outside the brackets tells you that you have to multiply count of e
ach atom inside the bracket on this index. For example, in Fe(NO3)2
you have one iron atom, two nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

"""



find_last_pos = lambda lst_, chr_: len(lst_) - 1 - lst_[::-1].index(chr_)


def split_string_into_chr(str_):
    lst_ = list(str_)
    lst_of_element = []
    i = 0
    count_chars = 0
    while True:
        if len(lst_) == i:
            break
        if lst_[i].isupper() and lst_[i+1].islower():
            lst_of_element.append(lst_[i] + lst_[i+1])
            i += 2
        else:
            lst_of_element.append(lst_[i])
            i += 1
    return lst_of_element


def delete_other_symb(chr_):
    parentheses = list("()[]{}")
    if chr_ in parentheses:
        return True
    else:
        return False

def add_digit_to_string(lst_, digit_):
    pass


def brackets(symbl_lst, parentheses):
    pattern_parenthrses = {"(":")", "{":"}", "[":"]"}
    first_prnth = parentheses.pop(0)
    pos_last_prnth = find_last_pos(parentheses, pattern_parenthrses[first_prnth])
    last_prnth = parentheses.pop(pos_last_prnth)
    first_sub_prnth = symbl_lst.index(first_prnth)
    last_sub_prnth = find_last_pos(symbl_lst, last_prnth)
    new_sub_list = symbl_lst[first_sub_prnth + 1 : last_sub_prnth]
    print(new_sub_list)
    if (symbl_lst[pos_last_prnth + 1]).isdigit():
        pass


def merge_number_to_char(str_):
    symbl_lst = split_string_into_chr(str_)
    parentheses = list(filter(delete_other_symb, symbl_lst))
    brackets(symbl_lst, parentheses)





