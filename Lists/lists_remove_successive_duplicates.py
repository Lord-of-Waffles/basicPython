def remove_successive_duplicates(list):
    for i in range(len(list)):
        if i == list[i+1]:
            list.pop(i)
    return list


def main():
    remove_successive_duplicates()

# currently not working