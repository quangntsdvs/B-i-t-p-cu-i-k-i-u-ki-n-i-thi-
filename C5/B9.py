class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def KiemTraGiong(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    else:
        return (root1.info == root2.info and
                KiemTraGiong(root1.left, root2.left) and
                KiemTraGiong(root1.right, root2.right))

def CayCon(cay1, cay2):
    if cay1 is None:
        return False
    elif KiemTraGiong(cay1, cay2):
        return True
    else:
        return CayCon(cay1.left, cay2) or CayCon(cay1.right, cay2)

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

print("Nhập cây 1:")
cay1 = TaoCay()

print("Nhập cây 2:")
cay2 = TaoCay()

if CayCon(cay1, cay2):
    print("Cây 2 là cây con của cây 1.")
else:
    print("Cây 2 không là cây con của cây 1.")