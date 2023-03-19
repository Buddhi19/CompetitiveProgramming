class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
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

    ################################### FIND MINIMUM IN A TREE ###################

    def find_min(self):
        if self.left==None:
            return self.data

        else:
            return self.left.find_min()


    ###################### DELETE FUNCTION ###################

    def delete(self,val):
        if val< self.data:
            if self.left:
                self.left=self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right=self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val=self.right.find_min()
            self.data = min_val
            self.right=self.right.delete(min_val)
            
        return self

##################### BUILDING TREE ###################################

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

    print(number_tree.delete(17))

    print(number_tree.in_order_traversal())



        