class TreeNode:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None

def isBSTTuanTu(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is None:
        return isBSTTuanTu(root.left)
    
    if root.left is None and root.right is not None:
        return isBSTTuanTu(root.right)
    
    if root.left is not None and root.right is not None:
        return isBSTTuanTu(root.left) and isBSTTuanTu(root.right)

def input_tree():
    root_value = int(input("Nhập giá trị của nút gốc: "))
    root = TreeNode(root_value)
    
    queue = [root]
    while queue:
        current = queue.pop(0)
        
        left_value = input(f"Nhập giá trị của nút con trái của {current.info} (nếu không có, nhập 'None'): ")
        if left_value.lower() != 'none':
            left_node = TreeNode(int(left_value))
            current.left = left_node
            queue.append(left_node)
        
        right_value = input(f"Nhập giá trị của nút con phải của {current.info} (nếu không có, nhập 'None'): ")
        if right_value.lower() != 'none':
            right_node = TreeNode(int(right_value))
            current.right = right_node
            queue.append(right_node)
    
    return root

root = input_tree()
result = isBSTTuanTu(root)
print("Cây đã nhập là BST theo tuần tự." if result else "Cây đã nhập không phải BST theo tuần tự.")