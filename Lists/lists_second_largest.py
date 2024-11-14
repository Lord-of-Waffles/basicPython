def second_largest(list):
    new_set = set(list)
    unique_list = sorted(new_set)
    if len(unique_list) > 1:
        return unique_list[-2]
    else:
        return None

def main():
    second_largest()