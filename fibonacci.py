def generate_fibonacci_numbers(sequence_length):
    if sequence_length == 1:
        return [1]
    elif sequence_length == 2:
        return [1, 1]
    else:
        target = [1, 1]
        remaining_length = sequence_length - 2
        while remaining_length > 0:
            target.append(target[-1] + target[-2])
            remaining_length -= 1
        return target


print(generate_fibonacci_numbers(20))
