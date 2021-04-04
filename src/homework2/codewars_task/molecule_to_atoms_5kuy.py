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

Note that brackets may be round, square or curly and can also be nested.
Index after the braces is optional.

"""


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
    while True:
        if len(lst_) == (i + 1):
            lst_of_element.append(lst_[i])
            break
        if lst_[i].isupper() and lst_[i + 1].islower():
            lst_of_element.append(lst_[i] + lst_[i + 1])
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
            if new_list[i - 1].isdigit():
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
    sub_lst_ = lst_[open_prnth_pos + 1: close_prnth_pos]
    count_open = sub_lst_.count("(") + 1
    count_close = 1
    previous_pos = 0
    if count_open == 1:
        return open_prnth_pos, close_prnth_pos
    while count_open:
        previous_pos = close_prnth_pos
        close_prnth_pos = lst_.index(")", close_prnth_pos + 1)
        count_close += 1
        count_open = count_open + lst_[previous_pos + 1: close_prnth_pos]\
            .count("(")
        count_open -= count_close
        count_close = 0
    return open_prnth_pos, close_prnth_pos


def merge_molecule_and_digit_expression(lst_, pos):
    open_prnth, close_prnth = pos
    if (len(lst_) - 1 > close_prnth) and lst_[close_prnth + 1].isdigit():
        num = lst_[close_prnth + 1]
    else:
        num = 0
    lst_.pop(open_prnth)
    lst_.pop(close_prnth - 1)
    slice_lst = lst_[open_prnth: close_prnth - 1]
    if num != 0:
        slice_with_num = add_digit_to_slice(slice_lst, num)
        result_slice = lst_[: open_prnth] + slice_with_num + lst_[close_prnth:]
    else:
        result_slice = lst_.copy()
    return result_slice


def add_digit_to_slice(slice_lst, num):
    open_prnth, close_prnth = 0, 0
    new_lst = []
    if slice_lst.count("("):
        open_prnth, close_prnth = expand_breakets(slice_lst)
    i = 0
    while i < len(slice_lst):
        if open_prnth and i in range(open_prnth, close_prnth + 1):
            new_lst.append(slice_lst[i])
            i += 1
            continue
        new_lst.append(slice_lst[i])
        if (i + 1) < len(slice_lst) and slice_lst[i + 1].isdigit():
            new_num = int(num) * int(slice_lst[i + 1])
            new_lst.append(str(new_num))
            i += 2
        else:
            new_lst.append(str(num))
            i += 1
    return new_lst


def kostyl(lst_):
    i = 0
    new_lst = []
    while i < len(lst_):
        if (i + 1) < len(lst_) and lst_[i].isdigit() and lst_[i + 1].isdigit():
            new_num = int(lst_[i]) * int(lst_[i + 1])
            new_lst.append(str(new_num))
            i += 2
        else:
            new_lst.append(lst_[i])
            i += 1
    return new_lst


def calculate_repeat_molecule(lst_):
    new_lst = []
    pattern_lst = []
    i = 0
    while i < len(lst_):
        if lst_.count(lst_[i]) > 1 and (not lst_[i].isdigit()) \
                and not(lst_[i] in pattern_lst):
            z = 0
            total_num = 0
            pattern_lst.append(lst_[i])
            while z < len(lst_):
                if lst_[z] == lst_[i]:
                    if (z + 1) < len(lst_) and lst_[z + 1].isdigit():
                        total_num += int(lst_[z + 1])
                        z += 2
                        continue
                    else:
                        total_num += 1
                        z += 1
                        continue
                z += 1
            new_lst.append(lst_[i])
            new_lst.append(str(total_num))
            i += 1
        elif (i - 1) > 0 and lst_[i - 1] in pattern_lst and lst_[i].isdigit():
            i += 2
        elif not lst_[i] in pattern_lst:
            new_lst.append(lst_[i])
            i += 1
        else:
            i += 1
    return new_lst


def merge_number_to_char(str_):
    symbl_lst = split_string_into_chr(str_)
    new_list = list(map(replace_chars, symbl_lst))
    count = new_list.count("(")
    if count == 0:
        new_dict = merge_molecule_and_digit(new_list)
        return new_dict
    while count > 0:
        pos = expand_breakets(new_list)
        new_list = merge_molecule_and_digit_expression(new_list, pos)
        new_list = kostyl(new_list)
        count -= 1
    new_list = calculate_repeat_molecule(new_list)
    return merge_molecule_and_digit(new_list)


def print_molecule_to_atoms():
    print("\n", "-" * 40)
    print("\t\tTask5: Molecule to atoms - 5kuy")
    print("Mg(OH)MgCa[CaO]2 =>", merge_number_to_char("Mg(OH)2MgCa2[CaO]2"))
    print("Mg(OH)2=>", merge_number_to_char("Mg(OH)2"))
    print("C2(OH)2{MgCa}[CaO]2 =>", merge_number_to_char(
        "C2(OH)2{MgCa}2[CaO]2"))
    print("-" * 40)
