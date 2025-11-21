from binaryTree import BTree

# Main program
def print_nodes(nodes):
    if not nodes:
        print("No nodes created.")
        return
    print("Index  Data  Left  Right")
    for i, n in enumerate(nodes):
        left = 'Y' if n.left is not None else 'N'
        right = 'Y' if n.right is not None else 'N'
        print(f"{i:5d}  {n.data!s:4s}   {left}     {right}")

def input_index(prompt, nodes):
    try:
        idx = int(input(prompt))
    except ValueError:
        print("Invalid index.")
        return None
    if idx < 0 or idx >= len(nodes):
        print("Index out of range.")
        return None
    return idx

def menu():
    nodes = []
    root = None

    while True:
        print("\nMenu:")
        print("1) Create root")
        print("2) Add LEFT child to a node")
        print("3) Add RIGHT child to a node")
        print("4) Delete LEFT child of a node (leaf only)")
        print("5) Delete RIGHT child of a node (leaf only)")
        print("6) Show node list")
        print("7) Print tree")
        print("8) Preorder")
        print("9) Inorder")
        print("10) Postorder")
        print("11) Double Traversal")
        print("12) Size (root)")
        print("13) Height (root)")
        print("14) Clear tree data (set nodes' data to 0)")
        print("0) Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            if root is not None:
                print("Root already exists.")
                continue
            try:
                v = input("Enter root value: ").strip()
            except (KeyboardInterrupt, EOFError):
                print()
                continue
            root = BTree(v)
            nodes.append(root)
            print("Root created at index 0.")

        elif choice == '2' or choice == '3':
            if root is None:
                print("Create a root first.")
                continue
            print_nodes(nodes)
            idx = input_index("Parent node index: ", nodes)
            if idx is None:
                continue
            parent = nodes[idx]
            try:
                val = input("Enter child value: ").strip()
                if choice == '2':
                    child = parent.addLeft(val)
                else:
                    child = parent.addRight(val)
            except AssertionError as e:
                print("Error:", e)
                continue
            nodes.append(child)
            print(f"Child added at index {len(nodes)-1}.")

        elif choice == '4' or choice == '5':
            if root is None:
                print("Create a root first.")
                continue
            print_nodes(nodes)
            idx = input_index("Parent node index: ", nodes)
            if idx is None:
                continue
            parent = nodes[idx]
            try:
                if choice == '4':
                    if parent.left is None:
                        print("Left child absent.")
                        continue
                    child_ref = parent.left
                    parent.delLeft()
                else:
                    if parent.right is None:
                        print("Right child absent.")
                        continue
                    child_ref = parent.right
                    parent.delRight()
            except AssertionError as e:
                print("Error:", e)
                continue
            # remove child from nodes list if present
            if child_ref in nodes:
                nodes.remove(child_ref)
            print("Child deleted.")

        elif choice == '6':
            print_nodes(nodes)

        elif choice == '7':
            if root is None:
                print("No tree.")
            else:
                print(root)

        elif choice == '8':
            if root is None:
                print()
            else:
                print("Preorder:", root.preOrder())

        elif choice == '9':
            if root is None:
                print()
            else:
                print("Inorder:", root.inOrder())

        elif choice == '10':
            if root is None:
                print()
            else:
                print("Postorder:", root.postOrder())

        elif choice == '11':
            if root is None:
                print()
            else:
                print("Double Traversal:", root.doubleTraversal())

        elif choice == '12':
            if root is None:
                print("Size: 0")
            else:
                print("Size:", root.size())

        elif choice == '13':
            if root is None:
                print("Height: 0")
            else:
                print("Height:", root.height())

        elif choice == '14':
            if root is None:
                print("No tree.")
            else:
                root.clearTree()
                print("All node data set to 0.")

        elif choice == '0':
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")