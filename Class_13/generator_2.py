# def gap(l):
#     num_of_zeros = []
#     counter = 0
#     for i in l:
#         if i == 1:
#             yield counter
#             counter = 0
#             num_of_zeros.append(counter)
#         else:
#             counter += 1
#             num_of_zeros.append(counter)

#     yield num_of_zeros


# runs = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
# generator = gap(runs)
# for i in generator:
#     print(i)


# def gap_generator(l, limit):
#     num_of_zeros = []
#     counter = 0
#     try:
#         for i in l:
#             yield counter
#             if i == 1:
#                 yield counter
#                 counter = 0
#                 num_of_zeros.append(counter)
#             else:
#                 counter += 1
#                 num_of_zeros.append(counter)

#     except StopIteration:
#         print("Gap Exceeded - Warning! ")


# runs = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
# num = int(input("Enter n: "))
# generator = [i for i in gap_generator(runs, num)]


def count_good(data, limit):
    count = 0
    for i in data:
        try:
            if i == 1:
                yield count
                count = 0
            else:
                count += 1
                if count > limit:
                    raise StopIteration("Warning, gap exceeded.")
        except StopIteration as e:
            print(e)
            break
    yield count


runs = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
num = int(input("Enter n: "))
generator = [i for i in count_good(runs, num)]
