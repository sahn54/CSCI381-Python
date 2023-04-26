# palindrome = int(input("please enter four digit integer: "))
# num = palindrome
# # 1 2 3 4

# a = num % 10
# # if num is 1221 num % 10 = 1
# num //= 10
# # 1221 //= 10 = 122
# b = num % 10
# num //= 10
# c = num % 10
# num //= 10
# d = num

# if a == d and b == c:
#     print(palindrome, "is a palindrome.")

# else:
#     print(palindrome, "is not a plaindrome. ")


# #assume you have a function ispalindrome() which tells you if a string is a palindrome or not.
# def ispalindrome(my_string):
#   #let's iterate through and check the first character against the last character, the second against the second-to-last, etc until we hit the middle
#   stopping_point = len(my_string) // 2
#   #if the string is seven characters long, suppose racecar
#   #we can stop when we hit the third character (check 0, 1, 2 against 6,5,4 respectively. 3 == 3 automatically)
#   #if the string is six characters long, suppose speeps
#   #we can stop when we hit the third character (check 0,1,2 against 5,4,3 respectively)
#   for x in range(stopping_point):
#     char_1 = my_string[x]
#     char_2 = my_string[(-1 * x) - 1]
#     if char_1 != char_2:
#       return False
#   return True

# #write a function that takes in any size integer and prints to the user whether or not it is a palindrome
# # def is_integer_palindrome(number):
# #   return ispalindrome(str(number))

# def is_integer_palindrome(number):
#   number_string = ""
#   while number > 0:
#     next_digit = number % 10
#     number //= 10
#     number_string = str(next_digit) + number_string
#   return ispalindrome(number_string)

# # print(is_integer_palindrome(100001))
# # print(is_integer_palindrome(232))
# print(is_integer_palindrome(123456))
def isPalindrome(string):
    mainpoint = len(string) // 2
    for x in range(mainpoint):
        char1 = string[x]
        char2 = string[(-1 * x)-1]
        if char1 != char2:
            return False
        return True


def isPalindrome_int(number):
    numberToString = ""
    while number > 0:
        next_num = number % 10
        number //= 10
        numberToString = str(next_num) + numberToString
    return isPalindrome(numberToString)


print(isPalindrome_int(5005))
print(isPalindrome("level"))
