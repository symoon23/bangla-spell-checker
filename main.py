from spell import is_banan_correctly
from spell import suggested_word





values = input()
for value in values.split(" "):
    if not is_banan_correctly(value):
        print("Spelling error: " + value)
        print("Suggested word: " + str(suggested_word(value)))

    else:
        print("Correct!")