# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm

array = [3,5,1,4,7,333,4,5555]

print(min(array))
print(max(array))

for num in range(2, 101):

        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)


def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]


# Test cases
word = "racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

phrase = "A man a plan a canal Panama"
if is_palindrome(phrase):
    print(f"'{phrase}' is a palindrome")
else:
    print(f"'{phrase}' is not a palindrome")
