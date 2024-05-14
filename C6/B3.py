def Giao(arr1, arr2):
    common_elements = sorted(set(arr1) & set(arr2))
    return common_elements

arr1 = list(map(int, input("Nhập mảng a các số nguyên, cách nhau bằng dấu cách: ").split()))
arr2 = list(map(int, input("Nhập mảng b các số nguyên, cách nhau bằng dấu cách: ").split()))

result = Giao(arr1, arr2)
print("Mảng c chứa các số (không trùng) đồng thời có trong mảng a và mảng b:", result)