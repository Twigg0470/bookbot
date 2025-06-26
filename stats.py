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

def sort_dict(dictionary):
    sorted_list = []
    def sort_on(items):
        return items["num"]
    
    for key, value in dictionary.items():
        if key.isalpha() == True:
            new_dict = {}
            new_dict["char"] = key
            new_dict["num"] = value

            sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
            


        


