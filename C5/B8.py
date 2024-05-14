class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def SoSanh(cay1, cay2):
    if cay1 is None and cay2 is None:
        return True
    elif cay1 is None or cay2 is None:
        return False
    else:
        return (cay1.info == cay2.info and
                SoSanh(cay1.left, cay2.left) and
                SoSanh(cay1.right, cay2.right))

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

if SoSanh(cay1, cay2):
    print("Hai cây giống hệt nhau.")
else:
    print("Hai cây không giống hệt nhau.")