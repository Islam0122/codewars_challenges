import collections
import decimal
import itertools
import re
import math
import sys
import gmpy2

""" top_3_words """
# def top_3_words(text):
#     res = []
#     words = re.findall(r"[a-zA-Z']+", text)
#     for word in words:
#         if any(char.isalpha() for char in word):
#             res.append(word.lower())
#     x = collections.Counter(res)
#     top_three = x.most_common(3)
#     three = []
#     for i in top_three:
#         three.append(i[0])
#     return three
#
# print(top_3_words("//wont won't won't"))


"""last_digit"""
# def last_digit(n1, n2):
#     if n2 == 0:
#         return 1
#     reduced_exponent = n2 % 4 if n2 % 4 != 0 else 4
#     return (n1 ** reduced_exponent) % 10
#
# print(last_digit(2,34))


"""permutations"""
# def permutations(s):
#     res = []
#     text =  list(itertools.permutations(s))
#     for i in text:
#         res2 = ""
#         for j in list(i):
#             res2 += j
#         res.append(res2)
#
#     return list(set(res))
#
# print(permutations('abc')) # ['abc','acb','bac','bca','cab','cba']


"""middle_permutation"""
# def middle_permutation(string):
#     s = sorted(string)
#     if len(s) % 2 ==0:
#         return s.pop(len(s)//2-1) +''.join(s[::-1])
#     else:
#         return s.pop(len(s)//2) + middle_permutation(s)

# print(middle_permutation("abc"))


"""next_smaller"""
# def next_smaller(n):
#     n_index = 0
#     res = []
#     text = list(itertools.permutations(str(n)))
#     for i in text:
#         res2 = ""
#         for j in list(i):
#             res2 += j
#         res.append(res2)
#     res2 = []
#     for i in sorted(list(set(res))):
#         res2.append(int(i))
#     for i in res2:
#         if n == i:
#             n_index += res2.index(i)
#     if res2[n_index] >= res2[n_index - 1]:
#         return res2[n_index-1]
#
#     return -1
#
#
# print(next_smaller(414))

"""sum_strings"""
# def sum_strings(x, y):
#     x = x or "0"
#     y = y or "0"
#     a = gmpy2.mpz(x)
#     b = gmpy2.mpz(y)
#     return str(a + b)
#
# print(sum_strings("4", "4"))

