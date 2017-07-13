user_input = input("Enter a string, to check for a palindrom")

reverse_input = user_input[::-1]

if reverse_input == user_input:
    print("word is a palindrom")
else:
    print("word is not a palindrom")