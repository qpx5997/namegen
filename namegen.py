import random
CONSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "sh", "ch", "ph", "th"]
VOWELS = ["a", "e", "ee", "i", "o", "oo", "u", "y"]
CV_COMB = ["c", "c", "c", "c", "c", "c", "c", "c", "c", "v", "v", "v", "v", "v", "v", "v","v", "cc", "cc", "cc", "vv", "vv", "cv", "cv", "cv", "cv", "cv", "cv", "cv", "cv", "cv", "cc", "cc", "vc", "vc", "vc", "vc", "vc", "cc"] # there are duplicates because the duplicated ones will appear more often

def randname_customizable(template, capitalize=False):
    return_name = ""
    for letter in template:
        if letter == "c":
            return_name += random.choice(CONSONANTS)
        elif letter == "v":
            return_name += random.choice(VOWELS)
        else:
            raise SyntaxError(f"Undefined letter type: \"{letter}\". Did you mean \"c\" or \"v\"?")
    if capitalize == True:
        return_name = return_name[0].upper() + return_name[1:]  
    return return_name

def randname(length, capitalize=False):
    if length is None:
        length = random.randint(3, 7)
    template = ""
    for i in range(0, length+1):
        template += random.choice(CV_COMB)
    if capitalize == True:
        return_name = randname_customizable(template, capitalize=True)
    else:
        return_name = randname_customizable(template)
    return return_name
