class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def _insert(self,root,value):
        if root is None:
            new_node=Node(value)
            root=new_node
            return root
        if root.data<value:
          root.right=  self._insert(root.right,value)
        else:
           root.left= self._insert(root.left,value)        
        return root

        
    def insert(self,value):
        self.root=self._insert(self.root,value)

    def _transversal(self,root):
        if root is None:
            return
        
        self._transversal(root.left)
        print(root.data,end=" ")
        self._transversal(root.right)

    def _search(self,root,target,count):
        if root is None:
            return count
        count+=1
        if root.data==target:
            return count
        elif root.data<target:
            return self._search(root.right,target,count)
        else:
            return self._search(root.left,target,count)
    def _remove(self,root,target)   :
        if root is None:
            return root
        elif root.data<target:
            root.right=self._remove(root.right,target)
        elif root.data>target:
            root.left=self._remove(root.left,target)  
        else:      
             if root.left is None and root.right is None:
                 root=None
             #    return root
             elif root.left is None:
                 temp=root.right
                 root=None
                 return temp
             elif root.right is None:
                 temp=root.left
                 root=None
                 return temp
             else:
                 min_node=self._find_min_node(root.right)
                 root.data=min_node.data
                 root.right= self._remove(root.right,min_node.data)
        return root     
    def _find_min_node(self,root):
        current=root
        while current.left is not None:
            current=current.left 
        return current    
    def _height_bst(self,root):

        if root is None:
            return 0
        r=self._height_bst(root.right)
        l=self._height_bst(root.right)
        return 1+max(r,l)

    def transversal(self):
        self._transversal(self.root)
    def search(self,target):
        count=0
        count_r=self._search(self.root,target,count)
        return count_r
    def remove(self,target):
        self.root=self._remove(self.root,target)

    def height_bst(self):
        return self._height_bst(self.root)    


def main ():
    bst=BST()
    bst.insert(5)
    bst.insert(2)
    bst.insert(10)
    bst.insert(12)
    bst.insert(1)
    bst.insert(9)

    bst.transversal()
    count=bst.search(12)
   # print(  count)
    bst.remove(5)
    print("\n")
    print("*"*20)
    bst.transversal()
    print("\n")
    print("*"*20)
    print( bst.height_bst())


if __name__=="__main__":
    main()