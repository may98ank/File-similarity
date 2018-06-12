from nltk.tokenize import sent_tokenize as st

def lines(a, b):
    """Return lines in both a and b"""
    lines_a = a.split("\n")
    lines_b = b.split("\n")
    ls = []
    for line in lines_a:
        if line in lines_b and not line in ls:
            ls.append(line)

    return ls


def sentences(a, b):
    """Return sentences in both a and b"""
    sen_a = st(a)
    sen_b = st(b)
    ls = []
    for sen in sen_a:
        if sen in sen_b and not sen in ls:
            ls.append(sen)

    return ls

def find_substr(s, n):
    ls = []
    l = len(s)
    for i in range(l-n+1):
        ls.append(s[i:i+n])

    return ls

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    substr_a = find_substr(a, n)
    substr_b = find_substr(b, n)
    ls = []
    for s in substr_a:
        if s in substr_b and not s in ls:
            ls.append(s)
    # TODO
    return ls
