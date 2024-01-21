print("Cross Product")
v = input("x, y, z: ")
u = input("a, b, c: ")

v = [int(num) for num in v.split(",")]
u = [int(num) for num in u.split(",")]

print(sum([pair[0] * pair[1] for pair in zip(v, u)]))
