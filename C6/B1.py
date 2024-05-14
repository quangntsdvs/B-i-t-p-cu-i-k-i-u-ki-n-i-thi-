def Duynhat(arr):
    unique_arr = sorted(set(arr))
    return unique_arr

arr = list(map(int, input("Nhập mảng các số nguyên, cách nhau bằng dấu cách: ").split()))

result = Duynhat(arr)
print("Mảng b sau khi loại bỏ các phần tử trùng nhau và sắp xếp:", result)