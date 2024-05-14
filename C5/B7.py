class TreeNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def Chep(root):
    if root is None:
        return None
    
    new_root = TreeNode(root.info)
    new_root.left = Chep(root.left)
    new_root.right = Chep(root.right)
    
    return new_root

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
copied_tree = Chep(root)

print("Cây đã được sao chép:")
def InOrderTraversal(root):
    if root:
        InOrderTraversal(root.left)
        print(root.info, end=' ')
        InOrderTraversal(root.right)

InOrderTraversal(copied_tree)