class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def ChieuCao(root):
    if root is None:
        return 0
    else:
        left_height = ChieuCao(root.left)
        right_height = ChieuCao(root.right)
        return max(left_height, right_height) + 1

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
height = ChieuCao(root)
print("Chiều cao của cây nhị phân là:", height)