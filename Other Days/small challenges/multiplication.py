no_of_columns = ((int(input("How many multiplication columns do you want?"))) + 1)

for row in range(1, 11):
    for column in range(1, no_of_columns):
        print(f"{row * column}", end=" ")
    print()
