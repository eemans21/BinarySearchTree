
import time as tt

class Node:
    
    def __init__(self, cargo = None, left = None, right = None):
        
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        
        return str(self.cargo)


class BinarySearchTree:
    
    def __init__(self, root = None):
        
        self.root = root        

    def insert(self, val):
        
        if self.root == None:
            
            self.root = val

        elif self.root.cargo == None:
            
            self.root.cargo = val.cargo

        else:   
            
            self.insert_helper(self.root, val)

        def insert_helper(self, current_node, val):

            if val.cargo <= current_node.cargo:

                if current_node.left != None:

                    self.insert_helper(current_node.left, val)
                    
                else:

                    current_node.left = val

            if val.cargo > current_node.cargo:

                if current_node.right != None:

                    self.insert_helper(current_node.right, val)
                    
                else:

                    current_node.right = val

        def search(self, val):

            start_time = tt.time()
            time = self.search_helper(self.root, val)
            end_time = tt.time()
            time_taken = str(end_time - start_time)
            print("Elapsed time: " + time_taken)

            return time

        def search_helper(self, current_node, val):

            if current_node.cargo != None:

                if val == current_node.cargo.rstrip():

                    return True

                if current_node.left != None and val < current_node.cargo:

                    return True * self.search_helper(current_node.left, val)

                if current_node.right != None and val > current_node.cargo:

                    return True * self.search_helper(current_node.right, val)

                return False

            else:

                return False


        def constructBST(fileName):

            file = open(fileName, "r")
            line = file.readline()
            bst = BinarySearchTree()

            while line != "":
                line.rstrip()
                newNode = Node(line)
                bst.insert(newNode)
                line = file.readline()
                file.close()
                
                return bst  
