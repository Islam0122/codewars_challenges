""" filter_list """
# def filter_list(l):
#     res = []
#     for i in l:
#         if type(i) ==  int:
#             res.append(i)
#     return res
#
# print(filter_list([1, 2, 3, 4, 5,"a"]))


"""get_sum"""
# def get_sum(a,b):
#     if a == b:
#         return a
#     start, end = min(a, b), max(a, b)
#     return (end - start + 1) * (start + end) // 2
#
# print(get_sum(-1,-2))

"""number"""
# def number(bus_stops):
#     return sum(on - off for on, off in bus_stops)
#
# print(number([[10,0],[3,5],[5,8]]))