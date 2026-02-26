def dragon_solution(is_dead, number_of_cows):
    fat_alive_cow_index = 0
    thin_alive_cow_index = number_of_cows - 1
    if number_of_cows == 1:
        return 0
    while fat_alive_cow_index < thin_alive_cow_index:
        middle_cow = int(((fat_alive_cow_index+1) + thin_alive_cow_index) / 2)
        if is_dead(middle_cow):
            if middle_cow == number_of_cows-1:
                return number_of_cows
            if not is_dead(middle_cow+1):
                return middle_cow
            else:
                fat_alive_cow_index = middle_cow
        else:
            if is_dead(middle_cow-1):
                return middle_cow-1
            elif middle_cow == 1 - is_dead(middle_cow-1):
                return 0
            elif middle_cow == number_of_cows-1:
                 return number_of_cows
            else:
                thin_alive_cow_index = middle_cow
    return middle_cow