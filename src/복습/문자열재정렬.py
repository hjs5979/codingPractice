strings = list(input())

answer_str_list = []

answer_num = 0

for i in strings:
    if i.isdigit():
        answer_num += int(i)
    else:
        answer_str_list.append(i)

answer_str_list.sort()
answer_str = ''.join(answer_str_list)

print(answer_str + str(answer_num))