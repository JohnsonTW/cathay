def game(i, j):
    if i == 1:
        return 0
    else:
        return (game(i - 1, j) + j) % i

while True:
    try:
        total_num = int(input("Input total number of people:（0 < number <= 100）: "))
        if 1 <= total_num <= 100:
            break
        else:
            print("Please input the correct number(0 < number <= 100）！")
    except ValueError:
        print("Please input a INTEGER")
        
out_num = 3
last_one = game(total_num, out_num) + 1
print("The last one is:", last_one)
