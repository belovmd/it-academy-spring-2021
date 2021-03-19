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


def replace_chars(chr_):
    if chr_ in ["{", "["]:
        return "("
    elif chr_ in ["]", "}"]:
        return ")"
    return chr_

def split_string_into_chr(str_):
    lst_ = list(str_)
    lst_of_element = []
    i = 0
    count_chars = 0
    while True:
        if len(lst_) == (i + 1):
            lst_of_element.append(lst_[i])
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

def merge_molecule_and_digit(new_list):
    i = 0
    molecule_dict = dict()
    while True:
        if len(new_list) <= (i + 1):
            if new_list[i-1].isdigit():
                break
            molecule_dict[new_list[i]] = 1
            break
        elif new_list[i + 1].isdigit():
            molecule_dict[new_list[i]] = int(new_list[i + 1])
            i += 2
        else:
            molecule_dict[new_list[i]] = 1
            i += 1
    return molecule_dict


def expand_breakets(lst_):
    open_prnth_pos = lst_.index("(")
    close_prnth_pos = lst_.index(")")
    sub_lst_ = lst_[open_prnth_pos + 1 : close_prnth_pos]
    count_open = sub_lst_.count("(") + 1
    count_close = 1
    previous_pos = 0
    while count_open:
        previous_pos = close_prnth_pos
        close_prnth_pos = lst_.index(")", close_prnth_pos + 1)
        count_close += 1
        count_open = count_open + lst_[previous_pos + 1: close_prnth_pos].count("(")
        count_open -= count_close
        count_close = 0
    return open_prnth_pos , close_prnth_pos -1

def merge_number_to_char(str_):
    symbl_lst = split_string_into_chr(str_)
    parentheses = list(filter(delete_other_symb, symbl_lst))
    new_list = list(map(replace_chars, symbl_lst))
    print(*new_list)
    count = new_list.count("(")
    if count == 0:
        new_dict = merge_molecule_and_digit(new_list)
        print(new_dict)
    if count > 1:
        pos = expand_breakets(new_list)
        new_list.pop(pos[0])
        new_list.pop(pos[1])
        print(new_list)
        pos = expand_breakets(new_list)
        new_list.pop(pos[0])
        new_list.pop(pos[1])
        print(new_list)








