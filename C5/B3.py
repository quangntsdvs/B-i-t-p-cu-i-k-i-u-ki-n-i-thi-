class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def SoNutLa(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return SoNutLa(root.left) + SoNutLa(root.right)

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
leaf_nodes = SoNutLa(root)
print("Số nút lá của cây nhị phân là:", leaf_nodes)