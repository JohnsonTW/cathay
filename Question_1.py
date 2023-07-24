def update_score(input_list):
    output_score = []
    for number in input_list:
        swap_num = number % 10 * 10 + number // 10
        output_score.append(swap_num)
    return output_score

original_score = [53, 64, 75, 19, 92]
final_score = update_score(original_score)
print(final_score)
