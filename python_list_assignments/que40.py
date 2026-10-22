numbers = [30, 10, 20, 10]

numbers.append(40)
print("append:", numbers)

numbers.insert(1, 50)
print("insert:", numbers)

numbers.remove(10)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

new_list = numbers.copy()
print("copy:", new_list)
print("count:", numbers.count(10))
print("index:", numbers.index(20))


numbers.extend([60, 70])
print("extend:", numbers)


numbers.sort()
print("sort:", numbers)


numbers.reverse()
print("reverse:", numbers)


numbers.clear()
print("clear:", numbers)