score_list = [1, 2, 3, 5, 10, 15, 30]

for i in score_list:
    print(i)

score_list.append(60)

list_len = len(score_list)
print("length is", list_len)

score_list.remove(60)

list_len = len(score_list)
print("length is", list_len)
