ans_str = "Hello welcome to Cathay 60th year anniversary"
input_list = list(ans_str)

count_letter = {}
count_num = {}

for i in input_list:
       
    if i.isdigit():
        if i in count_num:
            count_num[i] += 1
        else:
            count_num[i] = 1
    elif i.isalpha():
        i = i.upper()
        if i in count_letter:
                count_letter[i] += 1
        else:
            count_letter[i] = 1

result = []
for number in "0123456789":
    if number in count_num:
        result.append(f"{number} {count_num[number]}")
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in count_letter:
        result.append(f"{letter} {count_letter[letter]}")

print("\n".join(result))
