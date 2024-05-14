def BacDinh(graph, v):
    return len(graph[v])

num_nodes = int(input("Nhập số đỉnh của đồ thị: "))
graph = {}

for i in range(num_nodes):
    print("Nhập các đỉnh kề của đỉnh", i, "(cách nhau bằng dấu cách, nhập -1 để kết thúc):")
    neighbors = list(map(int, input().split()))
    if -1 in neighbors:
        neighbors.remove(-1)
    graph[i] = neighbors


print("Đồ thị:", graph)


vertex = int(input("Nhập đỉnh cần tính bậc: "))

print("Bậc của đỉnh", vertex, "là:", BacDinh(graph, vertex))