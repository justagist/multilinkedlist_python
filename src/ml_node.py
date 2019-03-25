


class MLNode:

    def __init__(self, element):

        '''             
            A Multi-Linked list node class interface. Each object of this type is a node which has two
            independent pairs of forward and backward pointers and thus can be on two independent
            lists (list1 and list2) at the same time.
            
            @Param element: The base element contained in this data structure: normally a String or Integer
            
        '''

        self._item = element

        self._prev1 = self._next1 = self._prev2 = self._next2 = self

    @property
    def prev1(self):
        return self._prev1

    @prev1.setter
    def prev1(self, val):
        self._prev1 = val
    
    @property
    def next1(self):
        return self._next1

    @next1.setter
    def next1(self, val):
        self._next1 = val

    @property
    def prev2(self):
        return self._prev2

    @prev2.setter
    def prev2(self, val):
        self._prev2 = val
    
    @property
    def next2(self):
        return self._next2

    @next2.setter
    def next2(self, val):
        self._next2 = val
    
    @property
    def element(self):
        return self._item
    

    def remove1(self):

        '''
            Remove this node from list1, list2 is not affected, this nodes next1 and prev1 references are reset to this node 
        
            @Return         this node

        '''

        self._prev1.next1 = self._next1
        self._next1.prev1 = self._prev1

        self._next1 = self._prev1 = self

        return self

    def remove2(self):

        '''
            Remove this node from list2, list1 is not affected, this nodes next2 and prev2 references are reset to this node 
        
            @Return         this node

        '''

        self._prev2.next2 = self._next2
        self._next2.prev2 = self._prev2

        self._next2 = self._prev2 = self

        return self

    def add_after1(self, target):
        '''
            Inserts this node onto list1 immediately after target,
            after first removing it from its original position in list1

            @Param target   the node after which this node should be inserted on list1
            @Return         this node
            
        '''
        self.remove1()

        self._prev1 = target
        self._next1 = target.next1

        self._next1.prev1 = self
        self._prev1.next1 = self

        return self


    def add_after2(self, target):
        '''
            Inserts this node onto list2 immediately after target,
            after first removing it from its original position in list2

            @Param target   the node after which this node should be inserted on list2
            @Return         this node
            
        '''
        self.remove2()

        self._prev2 = target
        self._next2 = target.next2

        self._next2.prev2 = self
        self._prev2.next2 = self

        return self


    def add_before1(self, target):
        '''
            Inserts this node onto list1 immediately before target,
            after first removing it from its original position in list1

            @Param      target the node before which this node should be inserted on list1
            @Return     this node
        '''

        self.remove1()

        self._next1 = target
        self._prev1 = target.prev1

        self._next1.prev1 = self
        self._prev1.next1 = self

        return self


    def add_before2(self, target):
        '''
            Inserts this node onto list2 immediately before target,
            after first removing it from its original position in list2

            @Param      target the node before which this node should be inserted on list2
            @Return     this node
        '''

        self.remove2()

        self._next2 = target
        self._prev2 = target.prev2

        self._next2.prev2 = self
        self._prev2.next2 = self

        return self

