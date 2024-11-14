def sum_every_other (list):
    if len(list) > 0:
        sum = 0
        for i in range(0, len(list), 2):
            sum += list[i]
        return sum
    else:
        return None
def main():
    sum_every_other()