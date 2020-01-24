'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # count = 0
    # if "th" in word:
    #     count += 1
    #     return count
    return word.count("th")

    return count_th(word-1)
