class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    ########################  All elements in an ascending Order ###########################

    def in_order_traversal(self):
        elements =[]

        #### Visit left
        if self.left:
            elements+=self.left.in_order_traversal()

        #### Visit Base Node
        elements.append(self.data)

        #### Visit Right Node
        if self.right:
            elements+=self.right.in_order_traversal()
        
        return elements
    
    ##################################### SEARCH IN TREE #################################

    def search(self,val):
        if self.data==val:
            return True
        
        if val < self.data:
            if self.left==None:
                return False
            else:
                self.left.search(val)
        
        if val > self.data:
            if self.right==None:
                return False
            else:
                self.right.search(val)


    
############################################### BUILD TREE #####################################

def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

########################################## DRIVER ############################################

if __name__=="__main__":

    elements=[17,4,1,20,9,8,23,18,34]
    number_tree=build_tree(elements)

    print(number_tree.in_order_traversal())

    print(number_tree.search(17))



##################################  SOLUTION  #########################################

"""[1, 4, 8, 9, 17, 18, 20, 23, 34]
True"""