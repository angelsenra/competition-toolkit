from inputloop import ntimes  # custom snippet


def ADN_matches():
    """Last input is where to search. (others are strings to be found there).
    You need to output the first matching position or 0 if there is no match.
    In case of a match, output the number of mutations as well (0 or 1)."""
    out = ntimes(plus=1)
    s = out[-1]
    for i in out[:-1]:
        if i in s:
            print(s.index(i) + 1, 0)
            continue
        for a, j in enumerate(i):
            for x in set("ATCG") - set([j]):
                if i[:a] + x + i[a + 1:] in s:
                    print(s.index(i[:a] + x + i[a + 1:]) + 1, 1)
                    break
        else:
            print(0)

ADN_matches()
