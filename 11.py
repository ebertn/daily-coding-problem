def autocomplete(q, words):
    d = preprocess(words)
    print(d)

    s = ""
    result = []
    cur = d
    for letter in q:
        print(s, result)
        s += letter

        if '\0' in cur:
            result.append(s)

        if letter in cur:
            cur = cur[letter]
        else:
            print(letter, cur)
            return result

    return result

def get_

def preprocess(words):
    d = {}
    for word in words:
        cur = d
        for letter in word:
            if letter not in cur:
                cur[letter] = {}

            cur = cur[letter]
        
        cur['\0'] = None # Could be set to anything, I think
    
    return d




