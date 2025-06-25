def count_words(text):
    return len(text.split())

def character_repeat_count(text):
    text = text.lower()
    letter_int = {}
    for i in text:
        if i not in letter_int:
            letter_int[i] = 1
        elif i in letter_int:
            letter_int[i] += 1
    return letter_int

