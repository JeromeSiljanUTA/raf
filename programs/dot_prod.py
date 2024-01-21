def str_dot_product():
    v = [int(num) for num in v.split(",")]
    u = [int(num) for num in u.split(",")]

    print(sum([pair[0] * pair[1] for pair in zip(v, u)]))


def input_dot_product():
    print("Dot Product")
    v = input("x, y, z: ")
    u = input("a, b, c: ")
    return v, u


v, u = input_dot_product()
str_dot_product(v, u)
