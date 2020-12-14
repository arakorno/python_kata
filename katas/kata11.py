import string


def sort(data):
    let_map = dict((key, 0) for key in string.ascii_lowercase)
    for c in data.lower():
        if c in let_map:
            let_map[c] += 1
    res = ""
    for key in let_map:
        res += key*let_map[key]
    return res

