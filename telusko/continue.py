
# continue example
for i in range(1, 101):

    if i % 3 == 0 or i % 5 == 0:
        continue

    print(i)

print("bye")

# pass example
for i in range(1, 101):

    if i % 2 != 0:
        pass
    else:
        print(i)

print("bye")
