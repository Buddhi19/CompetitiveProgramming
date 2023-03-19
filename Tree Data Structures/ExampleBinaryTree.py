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

    ################################### FIND MINIMUM IN A TREE ###################

    def find_min(self):
        if self.left==None:
            return self.data

        else:
            return self.left.find_min()
            
    #################################  FIND MAXIMUM IN A TREE ######################

    def find_max(self):
        if self.right==None:
            return self.data
        
        else:
            return self.right.find_max()
        

    ##########################  FIND SUM OF THE TREE #################################

    def find_sum(self):
        sum=0

        if self.left:
            sum+=self.left.find_sum()
        
        sum+=self.data

        if self.right:
            sum+=self.right.find_sum()

        return sum
    

######################### BUILD TREE #########################################
        
    
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root


############################## DRIVER CODE ############################

if __name__=="__main__":
    elements=[12,45,34,2,5,6,89,23]
    number_tree=build_tree(elements)

    print(number_tree.find_min())

    print(number_tree.find_max())

    print(number_tree.find_sum())


################ SOLUTIONS ############################################

"""
2
89
216

"""