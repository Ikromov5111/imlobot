from uzwords import words
from difflib import get_close_matches

def checkWords(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word,words))
    available = False #bunday so'z mavjud emas

    if word in matches:
        available = True #mavjud
        matches = word

    return {'available':available,'matches':matches}

if __name__ == '__main__':
    print(checkWords('олм',words))
    print(checkWords(words[88],words))
    print(checkWords(words[77],words))
    print(checkWords(words[5111],words))
    print(checkWords(words[3108],words))



