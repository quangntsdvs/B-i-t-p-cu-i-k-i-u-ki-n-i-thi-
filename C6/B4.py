def Hop(arr1, arr2):
    combined_arr = sorted(set(arr1 + arr2))
    return combined_arr

arr1 = list(map(int, input("Nhập mảng a các số nguyên, cách nhau bằng dấu cách: ").split()))
arr2 = list(map(int, input("Nhập mảng b các số nguyên, cách nhau bằng dấu cách: ").split()))

result = Hop(arr1, arr2)
print("Mảng c chứa các số (không trùng) có trong mảng a và / hoặc có trong mảng b:", result)