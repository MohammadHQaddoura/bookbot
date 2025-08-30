def num_words(text):
        return len(text.split())

def num_characters(text):
        tracker = {}
        lc_words = text.lower()
        
        for j in lc_words:
                if j in tracker:
                        tracker[j] += 1
                else:
                        tracker[j] = 1
        return tracker


def sort_on(items):
    return items["num"]

def pretty_list(diction):
        character_list = []

        for i in diction:
                tempDict = {}
                if i.isalpha():
                        tempDict["char"] = i
                        tempDict["num"] = diction[i]
                        character_list.append(tempDict)

        character_list.sort(reverse=True, key=sort_on)
        return character_list