def Hieu(a, b):
    set_a = set(a)
    set_b = set(b)

    c = sorted(list(set_a - set_b))

    return c

a = list(map(int, input("Nhập mảng a, các phần tử cách nhau bằng dấu cách: ").split()))

b = list(map(int, input("Nhập mảng b, các phần tử cách nhau bằng dấu cách: ").split()))

print("Mảng c:", Hieu(a, b))