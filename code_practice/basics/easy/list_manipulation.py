A = ["Red", "Blue", "Green", "Orange", "Yellow"]
B = ["Black", "Yellow", "Orange", "White"]
# Print all items from list A that are not present in list B
# PLease do not use in/not in comparison of lists
# Do not use sets/intersection


# Loop A and Loop B, find common colors from A existing in B.
# Remove the common colors in list A

# Loop A to find all the colors
C = A
for colorA in range(len(A)):
    # Loop B to find the colors
    color_present = False
    for colorB in range(len(B)):
        # Use a string comparison to find the same colors in list B
        if A[colorA] == B[colorB]:
            color_present = True

    # Remove the common colors from list A
            # A.pop(colorA)
    if not color_present:
        print(A[colorA])


# print(A)
