class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def SoNutTrungGian(root):
    if root is None:
        return 0
    elif root.left is not None or root.right is not None:
        return 1 + SoNutTrungGian(root.left) + SoNutTrungGian(root.right)
    else:
        return 0

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
intermediate_nodes = SoNutTrungGian(root)
print("Số nút trung gian của cây nhị phân là:", intermediate_nodes)