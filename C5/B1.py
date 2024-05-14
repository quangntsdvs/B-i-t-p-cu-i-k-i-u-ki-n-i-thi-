class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def SoNut(root):
    if root is None:
        return 0
    else:
        return SoNut(root.left) + SoNut(root.right) + 1

def TaoCay():
    val = int(input("Nhập giá trị cho nút (hoặc nhập -1 để kết thúc): "))
    if val == -1:
        return None
    else:
        root = TreeNode(val)
        print("Nhập nút con bên trái của", val)
        root.left = TaoCay()
        print("Nhập nút con bên phải của", val)
        root.right = TaoCay()
        return root

root = TaoCay()
num_nodes = SoNut(root)
print("Số nút của cây nhị phân là:", num_nodes)