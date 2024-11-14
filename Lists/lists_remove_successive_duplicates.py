def remove_successive_duplicates(list):

    for i in range(len(list) -1, 0 , -1):
        if list[i] == list[i-1]:
            del list[i]  


def main():
    remove_successive_duplicates()

