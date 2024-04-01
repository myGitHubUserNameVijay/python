import array as arr

vals = arr.array("i", [5, 2, 6, 7])  # i indicates type of data being stored in the array

print(vals.buffer_info())
print(vals.typecode)
print(vals)


vals.reverse()
print(vals)
print(vals[2])