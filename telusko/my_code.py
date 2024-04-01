av = 5

x = int(input("how many candies you want?"))

i = 1
while i <= x:
    if i > av:
        print("out of the stock")
        break

    print(i)
    print("candy")
    i += 1

print("bye")
