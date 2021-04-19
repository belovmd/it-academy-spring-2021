import hwFuncs


def runner(*args):

    def execute_func(element_):
        print('Function start: {}()'.format(element_))
        return getattr(hwFuncs, element_)()

    if not args:
        for element in [_ for _ in dir(hwFuncs) if callable(getattr(hwFuncs, _))]:
            return execute_func(element)

    else:
        for element in args:
            return execute_func(element)


runner('sort_list_hw3_6')
runner('dict_comprehensions_hw4_1', 'longest_word_hw2_2')
