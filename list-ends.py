def list_ends(input_list):
    if len(input_list) < 2:
        return input_list
    return [input_list[0], input_list[-1]]


a = [5, 10, 15, 20, 25]
print(list_ends(a)) 
