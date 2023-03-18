class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        ######## We are adding a child to self thus self becomes a parent of the entry
        child.parent = self 
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            p=p.parent
            level+=1
        print(" "*level,end='')
        return level

    def print_tree(self):
        self.get_level()
        print(self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    computers = TreeNode("Computers")
    mobiles=TreeNode("Mobiles")
    root.add_child(computers)
    root.add_child(mobiles)

    computers.add_child(TreeNode("Laptops"))
    computers.add_child(TreeNode("desktops"))

    mobiles.add_child(TreeNode("Iphonrs"))
    mobiles.add_child(TreeNode("Samsung"))

    # print(root.print_tree())
    return root

if __name__=="__main__":
    root=build_product_tree()
    root.print_tree()
    pass


