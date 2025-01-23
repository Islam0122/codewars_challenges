import collections
import re

""" top_3_words """
def top_3_words(text):
    res = []
    words = re.findall(r"[a-zA-Z']+", text)
    for word in words:
        if any(char.isalpha() for char in word):
            res.append(word.lower())
    x = collections.Counter(res)
    top_three = x.most_common(3)
    three = []
    for i in top_three:
        three.append(i[0])
    return three

print(top_3_words("//wont won't won't"))
