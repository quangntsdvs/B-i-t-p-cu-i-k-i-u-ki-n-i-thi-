class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def KiemTraBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    
    if root.info <= min_val or root.info >= max_val:
        return False

    return (KiemTraBST(root.left, min_val, root.info) and
            KiemTraBST(root.right, root.info, max_val))

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
if KiemTraBST(root):
    print("Cây là một cây tìm kiếm nhị phân (BST).")
else:
    print("Cây không phải là một cây tìm kiếm nhị phân (BST).")