# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)

# numbers_list = [x for x in range(30) if x % 2 ==0]
#
# note_mate = {"Ana Maria":5, "Ion Popescu":4, "Maria Elena":9}
# # numbers_list = [x for x,y in note_mate.items() if y > 4]
#
# numbers_list = [x if y<5 else '' for x,y in note_mate.items()]
#
# print(numbers_list)


# dictionar = {}
# for i in range(1,11):
#     dictionar[i] = i*i

dictionar = {i: i*i for i in range(1,11) if i % 2 == 0}
print(dictionar)