# Problem:
# Write a function that reverses a string. Remember, a string is not mutable! Do it two ways.
# Answer:

def reverse(str):
    reversed_str = ""
    for c in range(len(str)-1, -1, -1):
        reversed_str += str[c]
    print(reversed_str)


reverse("hello")


def reverse_2(str_1):
    return str_1[::-1]


print(reverse_2("world"))

# Problem:
# Write a function is_len(s,n) which returns True if string s is at least n characters long, and False
# otherwise.
# Answer:


def is_len(s, n):
    if len(s) >= n:
        return True
    else:
        return False


print(is_len("hello", 3))  # True
print(is_len("world", 6))  # False


# Problem:
# Write a function one_upper(s) which returns True if exactly one character in string s is capitalized, and
# False otherwise. You can assume that the string s contains only alphabetic characters and no blanks. You
# might want to consider other string functions from the documentation.
# Answer:


def one_upper(s):
    cap = 0
    for i in s:
        if i.isupper():
            cap += 1
            if cap > 1:
                return False
    return cap == 1


print(one_upper("Lion"))
print(one_upper("KiNG"))


# Problem:
# Write a function clear(x) where x is a list of “words”. Each word is a string that might have either a ‘.’
# ‘,’, or’;’ tacked on at the end. clear() will return a list with the original words stripped of the
# punctuation.

def clear(x):
    # x list of words.
    new_list = []
    for word in x:
        strip_word = word.strip(".,;")
        new_list.append(strip_word)
    print(new_list)


a = ['asd', 'er.', 'rt,', 'fgh;']

clear(a)


# Problem:
# Write a function scrape(s) which take a string s representing the HTML of a web page and returns a
# list of all links found on the page. We recognize the beginning of a link by looking for ‘http://’.
# Answer:

# def scrape(s):
#     links = []
#     for line in s.splitlines():
#         words = line.split()
#         for word in words:
#             if word.startswith('http://'):
#                 links.append(word)
#     return links


def scrape(s):
    updated_links = []
    for i in s.splitlines():
        words = i.split()
        for word in words:
            if word.startswith("http://"):
                updated_links.append(word)
    return (updated_links)


html = '<a href="http://www.google.com">Google</a> <a href="http://www.yahoo.com">Yahoo</a>'
links = scrape(html)
print(links)  # ['http://www.google.com', 'http://www.yahoo.com']


# Write a program that prompts the user for some integer n, and calculates the number of occurrences of
# the digit ‘1’ in all the numbers from 1-n inclusive.
# For example, if n=20 the program will print 12 since

def count_one(n):
    sum_num = 0
    for num_one in range(1, n+1):
        str_number = str(num_one)
        count = str_number.count('1')
        sum_num += count
    print(f"Number of 1's : {sum_num}")


number = int(input("Enter: "))
count_one(number)
