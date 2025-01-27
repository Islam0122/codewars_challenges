import collections
""" array diff  """
# def array_diff(a=list, b=list):
#     my_list = []
#     for  a_1 in a:
#         if a_1 not in b:
#             my_list.append(a_1)
#
#     return my_list
#
#
# print(array_diff([1, 2,2,3, 3], [1,2]))


""" create_phone_number """
# def create_phone_number(n):
#     phone_1 = ""
#     for i in  n[0:3]:
#         phone_1 += str(i)
#     phone_2 = ""
#     for i in  n[3:6]:
#         phone_2 += str(i)
#     phone_3 = ""
#     for i in n[6:9+1]:
#         phone_3 += str(i)
#     return f"({ phone_1}) {phone_2}-{phone_3}"
#
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # => returns "(123) 456-7890"


"""find_uniq"""
# def find_uniq(arr):
#     uniq = collections.Counter(arr).most_common()[-1][0]
#     return uniq
#
# output = find_uniq([ 1, 1, 1, 2, 1, 1 ])
# print(output)


"""duplicate_count"""
# def duplicate_count(text):
#     duplicate_numbers = collections.Counter(text.lower()).items()
#     res = 0
#     for i in duplicate_numbers:
#         if i[1] >= 2:
#             res += 1
#     return res
#
# print(duplicate_count("abcdeaB"))

