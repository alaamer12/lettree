import os
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

def build_tree(root, parent_node=None):
    # Create a node for the root directory
    node = Node(os.path.basename(root), parent=parent_node)
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            # if path.startswith("."):  # Skip hidden directories
            #     continue
            build_tree(path, node)  # Recursively build the tree
        else:
            Node(item, parent=node)  # Create a node for the file
    return node

# Define the root path of the directory tree
root_path = r"E:\TOURS\Tours\The Programming Tour"

# Build the tree
tree_root: Node = build_tree(root_path)
# print(tree_root)
# Print the tree structure to the console
for pre, _, node in RenderTree(tree_root):
    print(f"{pre}{node.name}")

# Export the tree to a DOT file using UniqueDotExporter
UniqueDotExporter(tree_root).to_dotfile("directory_tree.dot")

# Optionally, you can convert the DOT file to a PNG image using Graphviz
os.system("dot -Tpng directory_tree.dot -o directory_tree.png")
