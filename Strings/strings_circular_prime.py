def is_prime(n):
    if n > 1:
        for i in range(2, n, 1):
            if n % i == 0:
                return False
        return True
    else:
        return False
    
def is_circular_prime(n):
    #first one's primality always checked, start with next combo
    amazonPrimeMembership = is_prime(n)
    n_string = str(n)
    counter = 1
    storage_list = []

    if amazonPrimeMembership == True:
        for i in range(1,len(n_string),1):
            # insert first_int into n_string index at i

            first_int = n_string[0]
            for i in range (0, len(n_string), 1):
                storage_list.append(n_string[i])

            #move data to storage array, reformat and clear array
            storage_list.pop(0)
            storage_list.append(first_int)
            n_string = n_string = str(storage_list)
            n_string = n_string.replace("[", "")
            n_string = n_string.replace("]", "")
            n_string = n_string.replace("'", "")
            n_string = n_string.replace(" ", "")
            n_string = n_string.replace(",", "")
            storage_list.clear()

            if is_prime(int(n_string)) == False:
                return False
            else:
                counter = counter + 1
        if counter == len(n_string):
            return True

    else:
        return False
    
def main():
    user_input = int(input("Enter a positive integer: "))
    answer = is_circular_prime(user_input)
    if answer == True:
        print(f"{user_input} is a circular prime")
    else:
        print(f"{user_input} is not a circular prime")
main()