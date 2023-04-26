# Files Inputs and Outputs
# default iterable is line
# Make sure to add open and close
# or use with example where it closes automatically.
# read() to read the whole thing
# read a large file use chunks - read(number)

# write to files
# file = open("Class_10/bear.txt")
# for i in file:
#     print(i)
# the_read = file.read()
# print(the_read)
# file.close()


# with open("Class_10/bear.txt") as file:
#     z = file.read()
#     # z = z.split(' ')
#     z = z.splitlines()
#     print(z)


# Write a program to read this file and print out the students name followed by their average on all
# exams. (DO IT HOME)
# with open("Class_10/grades.txt") as grade_files:
#     with open("Class_10/new_grades.txt", "w") as new_grade_file:
#         for line in grade_files:
#             split_lines = line.split()
#             total_grades = 0
#             for i in range(1, len(split_lines)):
#                 total_grades += int(split_lines[i])
#                 current_average = (total_grades / (len(split_lines)-1))
#             new_grade_file.write(
#                 f"Student Name: {split_lines[0]} and their average is {current_average:.2f}\n")  # type: ignore
# with open("Class_10/new_grades.txt", "r") as new_grade_file:
#     back_to_terminal = new_grade_file.read()
#     print(back_to_terminal)


with open("Class_10/grades.txt") as grade_files:
    with open("Class_10/new_grades.txt", "w") as new_grade_file:
        for line in grade_files:
            print(line, end="")
            split_lines = line.split()
            print(split_lines)
            total_grades = 0
            for i in range(1, len(split_lines)):
                total_grades += int(split_lines[i])

                current_average = (total_grades / (len(split_lines)-1))

            new_grade_file.write(
                f"Student Name: {split_lines[0]} and their average is {current_average:.2f} \n")
            print(total_grades)
            print(len(split_lines)-1)
            print(current_average)
