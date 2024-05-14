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

def KiemTraAVL(root):
    if root is None:
        return True
    
    left_height = ChieuCao(root.left)
    right_height = ChieuCao(root.right)
    
    if abs(left_height - right_height) <= 1 and KiemTraAVL(root.left) and KiemTraAVL(root.right):
        return True
    
    return False

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
if KiemTraAVL(root):
    print("Cây là một cây cân bằng AVL.")
else:
    print("Cây không phải là một cây cân bằng AVL.")