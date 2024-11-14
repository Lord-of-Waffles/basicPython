def print_matrix_sum(first_m, second_m):
    answer_m = [[0 for _ in range(len(first_m[0]))] for _ in range(len(first_m))]
    for i in range(len(first_m)):
        for j in range(len(first_m[0])):
            answer_m[i][j] = first_m[i][j] + second_m[i][j]
    # printing loop
    for i in range(len(answer_m[0]), len(answer_m)[-1], 1):
        #if 2 rows
        if len(answer_m[0]) <= 2:
            #for loop going twice
            for i in range(0, 1, 1):
                print(f"{answer_m[i][0]} {answer_m[i][1]} {answer_m[i][2]}/n")
        #if 3 row
        elif len(answer_m[0]) == 3:
            #for loop going thrice
            for i in range(0, 2, 1):
                print(f"{answer_m[i][0]} {answer_m[i][0]} {answer_m[i][0]}/n")

            




def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)
main()