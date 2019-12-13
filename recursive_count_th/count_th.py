'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, i, j, value):
    if i >= len(word):
        print("Sorry, but the values you're looking for are not here.")

    if word[i] == value[0] and word[j] == value[1]:
        return i + 1

    return count_th(word, i + 1, j + 1, value)

print(count_th("eethoughts", 0, 1, "th"))
