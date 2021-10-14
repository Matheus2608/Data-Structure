from pythons3.basic import Stack


def matches(sym_left, sym_right):
    all_lefts = "{[{"
    all_rigts = ")]}"
    return all_lefts.index(sym_left) == all_rigts(sym_right)


def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if not matches(s.pop(), symbol):
                return False
    return s.is_empty()
