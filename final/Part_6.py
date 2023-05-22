# Using a dictionary comprehension create a dictionary with n associated to the nth prime number for the
# first k primes. K is provided by the user and is not part of the comprehension.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


print(is_prime(5))

k = int(input("Enter"))
dict_prime = {n: p for n, p in enumerate(
    filter(is_prime, range(2, int(k ** 2)+1)), start=1) if n <= k}
print(dict_prime)


# we want the nth key with a prime value
# k = int(input("Enter: "))
# dict_num = {n: p for n, p in enumerate(
#     filter(is_prime, range(2, int(k**2)+k)), start=1) if n <= k}
# print(dict_num)


# Write a function, signature(n) that and returns a string with same letters in lexicographic order.
# For example, signature(stop) ➔ opst
# n is a string , we might use ASCII to solve this problem

def signature(n):
    dict_str = {letter: ord(letter) for letter in n.lower()}
    list_str = sorted(dict_str.values(), key=lambda x: x)
    list_str = [chr(x) for x in list_str]
    new_str = "".join(list_str)
    return new_str


print(signature("Stop"))
