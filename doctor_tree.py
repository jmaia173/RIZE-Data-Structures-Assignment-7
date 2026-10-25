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