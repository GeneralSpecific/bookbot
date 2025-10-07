def count_words(text):
    return len(text.split())

def count_characters(text):
    dictionary = dict()
    dedupe = text.lower()
    
    for character in dedupe:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    iterated_list=[]
    for character in dictionary:
        character_count = dictionary[character] #
        dict_stub={"char": character , "num": character_count}
        iterated_list.append(dict_stub)
    
   # print(iterated_list.sort(reverse=True, key=sort_on))
  #  for idx, d in enumerate(iteratedlist):
   #     if not ("char" in d and "num" in d):
    #        print("Bad element at", idx, d)
    iterated_list.sort(reverse=True, key=sort_on)
    return iterated_list
    