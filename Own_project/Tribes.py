import copy
# with open("Own_project/numbers.txt") as file_tribes:
#     file_content = file_tribes.read()
#     lines = file_content.split("\n")
#     data_dict = {}
#     for line in lines[1::]:
#         key, value = line.split(",")
#         data_dict[key.strip()] = value.strip()
# print(data_dict)  # Original Order

# change_data_dict = copy.deepcopy(data_dict)
# ordered_data_dict = dict(
#     sorted(change_data_dict.items(), key=lambda x: x[1], reverse=True))
# print(ordered_data_dict)


# # The strip() method is used to remove any leading or trailing
# # whitespace from the keys and values.

# with open("Own_project/numbers_dict.txt", "w") as dict_file:
#     for line in data_dict:
#         dict_file.write(f"{line} : {data_dict[line]}\n")


# --------------------------New Challenge ---------------------------
# create a dictionary using two txt files and combine them into one dictionary.
# it can be nested dictionary

with open("Own_project/numbers.txt") as numbers_file:
    with open("Own_project/clan_chief.txt") as clan_chief_file:
        numbers_file_content = numbers_file.read()
        clan_chief_file_content = clan_chief_file.read()
        lines_numbers = numbers_file_content.split("\n")
        lines_clan_chiefs = clan_chief_file_content.split("\n")
        data_dict_1 = {}
        data_dict_2 = {}
        for line_number in lines_numbers[1::]:
            key, value = line_number.split(",")
            data_dict_1[key.strip()] = value.strip()
        for line_clan_chief in lines_clan_chiefs[1::]:
            key, value = line_clan_chief.split(",")
            data_dict_2[key.strip()] = value.strip()

        final_dict = {}
        for key, value in data_dict_1.items():
            final_dict[key] = {'number': value}
            if key in data_dict_2:
                final_dict[key]['clan_chief'] = data_dict_2[key]
print(final_dict)
