# prints out only odd numbers = 1,3,5,7,9

for x in range(10):
    # First check if x is even

    if x % 2 == 0:
        continue
    print("Value is:", x)