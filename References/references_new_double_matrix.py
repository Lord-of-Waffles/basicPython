from copy import deepcopy

def new_doubled_matrix(m):
    result = deepcopy(m)
    for i in range(0, len(result), 1):
        result[i] = result[i] * 2
    return result

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)
main()