class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found:
            return found
        return self._find(node.right, name)

    def insert(self, parent_name, doctor_name, side):
        if side not in ("left", "right"):
            print(f"Invalid side: {side}")
            return False
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Parent not found: {parent_name}")
            return False
        if getattr(parent, side) is not None:
            print(f"{parent_name} already has a {side} report")
            return False
        setattr(parent, side, DoctorNode(doctor_name))
        return True

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]

if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))

    tree.insert("Dr. Nobody", "Dr. X", "left")   # missing parent
    tree.insert("Dr. Croft", "Dr. X", "middle")  # invalid side
    tree.insert("Dr. Croft", "Dr. X", "left")    # occupied side