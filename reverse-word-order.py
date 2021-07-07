def reverse_word_order(sentence):
    target = sentence.split(sep=' ')
    target.reverse()
    return ' '.join(target)

my_string = 'My name is Michele'
print(reverse_word_order(my_string))
