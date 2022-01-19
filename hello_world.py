# s = {'four': 1, 'score': 1, 'and': 6, 'seven': 1, 'years': 1, 'ago': 1, 'our': 2, 'fathers': 1, 'brought': 1,
#      'forth': 1, 'on': 2, 'this': 4, 'continent': 1, 'a': 7, 'new': 2, 'nation': 5, 'conceived': 2, 'in': 4,
#      'liberty': 1, 'dedicated': 4, 'to': 8, 'the': 11, 'proposition': 1, 'that': 13, 'all': 1, 'men': 2, 'are': 3,
#      'created': 1, 'equal': 1, 'now': 1, 'we': 10, 'engaged': 1, 'great': 3, 'civil': 1, 'war': 2, 'testing': 1,
#      'whether': 1, 'or': 2, 'any': 1, 'so': 3, 'can': 5, 'long': 2, 'endure': 1, 'met': 1, 'battle': 1, 'field': 2,
#      'of': 5, 'have': 5, 'come': 1, 'dedicate': 2, 'portion': 1, 'as': 1, 'final': 1, 'resting': 1, 'place': 1,
#      'for': 5, 'those': 1, 'who': 3, 'here': 8, 'gave': 2, 'their': 1, 'lives': 1, 'might': 1, 'live': 1, 'it': 5,
#      'is': 3, 'altogether': 1, 'fitting': 1, 'proper': 1, 'should': 1, 'do': 1, 'but': 2, 'larger': 1, 'sense': 1,
#      'not': 5, 'consecrate': 1, 'hallow': 1, 'ground': 1, 'brave': 1, 'living': 2, 'dead': 3, 'struggled': 1,
#      'consecrated': 1, 'far': 2, 'above': 1, 'poor': 1, 'power': 1, 'add': 1, 'detract': 1, 'world': 1, 'will': 1,
#      'little': 1, 'note': 1, 'nor': 1, 'remember': 1, 'what': 2, 'say': 1, 'never': 1, 'forget': 1, 'they': 3, 'did': 1,
#      'us': 3, 'rather': 2, 'be': 2, 'unfinished': 1, 'work': 1, 'which': 2, 'fought': 1, 'thus': 1, 'nobly': 1,
#      'advanced': 1, 'task': 1, 'remaining': 1, 'before': 1, 'from': 2, 'these': 2, 'honored': 1, 'take': 1,
#      'increased': 1, 'devotion': 2, 'cause': 1, 'last': 1, 'full': 1, 'measure': 1, 'highly': 1, 'resolve': 1,
#      'shall': 3, 'died': 1, 'vain': 1, 'under': 1, 'god': 1, 'birth': 1, 'freedom': 1, 'government': 1, 'people': 3,
#      'by': 1, 'perish': 1, 'earth': 1, 'abraham': 1, 'lincoln': 1, 'november': 1, '19': 1, '1863': 1}
#
# from datetime import datetime, timedelta
#
#
# def datetime_range(start, end, delta):
#     current = start
#     while current < end:
#         yield current
#         current += delta
#
#
# start_time = datetime(2021, 9, 1, 8, 30)
# end_time = datetime(2021, 9, 1, 8, 53)
# delta = timedelta(minutes=10)
#
#
# def sum(a, b):
#     count = list(range(a, b))
#
#     return count[0]
#
#
# def time_series_in_timedelta(start_time, end_time, delta):
#     minute_time_ll = []
#     while start_time < end_time:
#         current = start_time
#         start_time += delta
#         end = start_time
#
#         if start_time >= end_time:
#             minute_time_ll.append((current, end_time))
#             break
#         else:
#             minute_time_ll.append((current, end))
#     return minute_time_ll
#
#
# minute_time_ll = time_series_in_timedelta(start_time, end_time, delta)
# start_time = datetime(2021, 9, 1, 8, 30)
# end_time = datetime(2021, 9, 1, 8, 53)
# delta = timedelta(minutes=10)
# count = sum(10000, 10001)
# while int(count) >= 1000:
#     minute_time_ll = time_series_in_timedelta(start_time, end_time, delta)
#     count = sum(10, 20)
#
#

dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}