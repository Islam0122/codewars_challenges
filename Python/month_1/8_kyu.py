"""bool to word """
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"
#
# print( bool_to_word(True))

""" summation """
# def summation(num):
#     return sum(list(range(1, num + 1)))
#
# print(summation(8))


"""check"""
# def check(seq, elem):
#     if elem in seq :
#         return True
#     else:
#         return False
#
# print(check([1,2,3],2))


""" string_to_number """
# def string_to_number(s):
#     return int(s)
#
# print(string_to_number("1"))


"""boolean_to_string"""
# def boolean_to_string(b):
#     return str(b)
#
# print(boolean_to_string(True))


""" are_you_playing_banjo"""
# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
#
# print(are_you_playing_banjo("islam"))


""" paperwork"""
# def paperwork(n, m):
#     if m >0 and n>0 :
#         return n*m
#     else:
#         return 0
#
# print(paperwork(5,10))


""" check_for_factor"""
# def check_for_factor(base, factor):
#    if base % factor == 0:
#        return True
#    else:
#        return False
#
# print(check_for_factor(10, 2))


"""between"""
# def between(a,b):
#     return list(range(a,b+1))
#
# print(between(2,4))

""" past """
# def past(h, m, s):
#     return (h * 3600 + m * 60 + s) * 1000
#
# print(past(12,12,12))

""" make_negative"""
# def make_negative(number):
#     return -abs(number)
#
# print(make_negative(0))
# print(make_negative(1))

""" name_shuffler """
# def name_shuffler(str_):
#     text = str_.split()
#     return str(text[1])+" "+str(text[0])
#
# print(name_shuffler("john McClane"))

""" no_boring_zeros """
# def no_boring_zeros(n):
#     x = ""
#     for i in str(n):
#          if i == '0':
#              pass
#          else:
#              x += i
#     return int(x)
#
# print(no_boring_zeros(506))


"""multi_table"""
# def multi_table(number):
#     table = ""
#     for i in range(1, 11):
#         table += f"{i} * {number} = {i * number}\n"
#     return table[:-1]
#
# print(multi_table(4))


"""sp_eng"""
# def sp_eng(sentence):
#     if 'english' in sentence.lower():
#         return True
#     else:
#         return False
#
# print(sp_eng("1234egn lis;h"))

"""sum_arra"""
# def sum_array(a:list):
#     return sum(a)
#
# print(sum_array([1,2,3]))

"""hoop_count"""
# def hoop_count(n):
#     if n >= 10:
#         return "Great, now move on to tricks"
#     return "Keep at it until you get it"
#
# print(hoop_count(5))

"""smash"""
# def smash(words):
#     res = ""
#     for word in words:
#         res += f"{word} "
#     return res[:-1]
#
#
# print(smash(["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]))


"""maps"""
# def maps(a):
#     return list(map(lambda x: x + 1, a))
#
# print(maps([1,2,3]))


"""solution"""
# def solution(string):
#     return string[::-1]
# print(solution("hello world"))


"""number_to_string"""
# def number_to_string(num):
#     return str(num)


"""find_smallest_int"""
# def find_smallest_int(arr):
#     return min(arr)


"""count_sheep"""
# def count_sheep(n):
#     res = ""
#     for i in range(1, n + 1):
#         if n > 0:
#             res += f"{i} sheep..."
#     return res
# print(count_sheep(0))


"""double_integer"""
# def double_integer(i):
#     return i*2


"""make_upper_case"""
# def make_upper_case(s):
#     return s.upper()
# print(make_upper_case("hello world"))


"""count_positives_sum_negatives"""
# def count_positives_sum_negatives(arr):
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []
# print(count_positives_sum_negatives([1, 2, 3, 4, 5]))

