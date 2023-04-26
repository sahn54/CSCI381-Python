def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"Your year, {year} is a leap year. ")
            else:
                print(f"Your year, {year} is not a leap year.")
        else:
            print(f"Your year ,{year} is a leap year.")
    else:
        print(f"Your year, {year} is not a leap year. ")


leap(4)
