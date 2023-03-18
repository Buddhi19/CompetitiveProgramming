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
        print(" "*level*2,end='')
        return level

    def print_tree(self):
        self.get_level()
        print(self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()

################# Building The Tree #######################

def build_tree():
    CEO=TreeNode("NILUPUL")
    CTO=TreeNode("CHINMAY")
    CEO.add_child(CTO)

    Infrastructure_Head=TreeNode("Vishwa")
    CTO.add_child(Infrastructure_Head)

    Cloud_Manager=TreeNode("Dhaval")
    Infrastructure_Head.add_child(Cloud_Manager)

    App_Manager=TreeNode("Abhijit")
    Infrastructure_Head.add_child(App_Manager)

    Application_Head=TreeNode("Aamir")
    CTO.add_child(Application_Head)

    HR_Head=TreeNode("GELS")
    CEO.add_child(HR_Head)

    Recruiment_Manager=TreeNode("Peter")
    HR_Head.add_child(Recruiment_Manager)

    Policy_Manager=TreeNode("Waqas")
    HR_Head.add_child(Policy_Manager)

    return CEO

############## Running code ##############################

if __name__=="__main__":
    tree=build_tree()
    tree.print_tree()
    pass

################ Tree ######################################

# NILUPUL
#   CHINMAY
#     Vishwa
#       Dhaval
#       Abhijit
#     Aamir
#   GELS
#     Peter
#     Waqas