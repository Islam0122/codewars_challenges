""" factorial """
def factorial(n):
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# """RomanNumerals """
# class RomanNumerals:
#     dict_roman = {
#         "M":1000,
#         "CM":900,
#         "D":500,
#         "CD":400,
#         "C":100,
#         "XC":90,
#         "L":50,
#         "XL":40,
#         "X":10,
#         "IX":9,
#         "V":5,
#         "IV":4,
#         "I":1
#     }
#     @staticmethod
#     def to_roman(val : int) -> str:
#         for i in RomanNumerals.dict_roman:
#             if val == RomanNumerals.dict_roman[i]:
#                 return i
#     @staticmethod
#     def from_roman(roman_num : str) -> int:
#         res = []
#         for i in roman_num:
#             if i in RomanNumerals.dict_roman:
#                 res.append(RomanNumerals.dict_roman[j])
#         return sum(res)
#
#
# print(RomanNumerals.from_roman(RomanNumerals.from_roman(["M"])))