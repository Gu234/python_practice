def is_num_in_list(ordered_list, num):
    output = num in ordered_list
    print(output)
    return output

is_num_in_list([1,2,3,4,5], 4)
is_num_in_list([1,2,3,4,5], 10)