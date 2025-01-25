# def mix(s1, s2):
#     words_s1 = []
#     words_s2 = []
#     for word in s1:
#         for letter in word:
#             if letter.isalpha():
#                 words_s1.append(letter)
#
#     for word in s2:
#         for letter in word:
#             if letter.isalpha():
#                 words_s2.append(letter)
#
#     counter_s1 = collections.Counter(words_s1).items()
#     counter_s2 =  collections.Counter(words_s2).items()
#     res = []
#     for key_s1 in counter_s1:
#         for key_s2 in counter_s2:
#             if key_s1[0] == key_s2[0]:
#                 if key_s1[1] > key_s2[1]:
#                     res.append(f"1:{key_s1[0]* key_s1[1]}/")
#                 elif key_s1[1] < key_s2[1]:
#                     res.append(f"2:{key_s2[0]* key_s2[1]}/")
#                 elif key_s1[1] == key_s2[1]:
#                     if len(key_s1[0] * key_s1[1]) > 1:
#                         res.append(f"=:{key_s2[0]* key_s1[1]}/")
#                 else:
#                     if len(key_s1[0] * key_s1[1]) > 1:
#                         res.append(f"=:{key_s2[0] * key_s1[1]}/")
#
#
#
#     start_num = ""
#     start_letter = ""
#     for i in sorted(res):
#         if i[0] == "2" or i[0] == "1":
#             start_num += i
#         else:
#             start_letter += i
#     result = start_num + start_letter
#     return result[:-1]
#
#
# print(mix("Are they here", "yes, they are here"))  # 2:eeeee/2:yy/=:hh/=:rr
