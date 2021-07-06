user_string = input('Enter a string =>')
palindrome = True
for i in range(len(user_string)//2):
    if user_string[i] != user_string[-i-1]:
        palindrome = False
        break
if palindrome:
    print("String is a palindrome")
else:
    print("String isn't a palindrome")
