'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # "th" is at least 2 letters
    if len(word) < 2:
        return 0

    if word[:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])
