length = int(input("Enter the size of the pattern: "))

i = 0
while i < length:  # outer loop → rows
    j = 0
    while j < length:  # inner loop → columns
        print("*", end="")
        j += 1
    print()  # move to next row
    i += 1
