import re

# pre_work = {
#     1: '',
#     2: '',
#     3: '1',
#     4: '1,2',
#     5: '4',
# }

# pre_flag = [0 for x in range(len(pre_work))]
# aft_flag = [0 for x in range(len(pre_work))]

# order = 0;

# for x in pre_work:
#     if x == '':
#         pre_flag[order] = 1
#     else:
#         for y in list(map(int, re.findall(r'(\d+)', x, flags=0))):
#             aft_flag[y-1] = 1
#     order += 1

# print (pre_flag, aft_flag)

# s = '1,2,4,3'

# if re.match(r'^(\d+)[|,((\d+),)*](\d+)$', s, flags=0):
#     mask_x = list(map(int, re.findall(r'(\d+)', s, flags=0)))
#     print(mask_x)

startwork = []
finalwork = []
allwork = []

for x in Projectlist:
    if !x:
        startwork.append(x.id)
    else:
        mask = list(map(int, re.findall(r'(\d+)', x.pre_work, flags=0)))
        for y in mask:
                finalwork.append(y)
        allwork.append(x.id)

nofinalwork = list(set(allwork) - set(finalwork))

project


