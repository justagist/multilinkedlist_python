
from src import MLNode

class OrderedMRUList:

    def __init__(self):
        '''
            A multi-linked list interface of a class that implements an ordered list and a most
            recently used (MRU) list, where list1 is used
            for the ordered list and list2 is used for the most recently used list.
              
        '''
        self._head_ordered = MLNode(None)
        self._head_mru = MLNode(None)

    def is_empty_ordered(self):

        if self._head_ordered == self._head_ordered.next1 == self._head_ordered.prev1:
            return True

        return False

    def is_empty_mru(self):

        if self._head_ordered == self._head_ordered.next1 == self._head_ordered.prev1:
            return True

        return False

    def touch(self, target):
        '''
            Removes the target node from its current position in the MRU list and puts it at the front
            of the MRU list. The ordered list is unaffected.

            @Param target       the node to move
            @Return this        OrderedMRUList object, so that further calls on it can be chained
            
        '''
        if self._head_mru.next2 != target:
            target = target.remove2()
            target.add_after2(self._head_mru)
            # target.next2 = self._head_mru
            # self._head_mru = target.next2
        return self

    def get_first_ordered(self):
        '''
            Get the first node on the ordered list

            @Return     the first node of the ordered list, or None if the list is empty 
            
        '''
        if self.is_empty_ordered():
            return None
        return self._head_ordered.next1

    def get_first_mru(self):
        '''
            Get the first node on the mru list

            @Return     the first node of the mru list, or None if the list is empty 
            
        '''
        if self.is_empty_mru():
            return None
        return self._head_mru.next2

    def get_next_ordered(self, current):
        '''
            Get the next node in order after the current node on the ordered list

            @Param current      the node on the ordered list preceeding the one to return
            @Return             the next ordered node, or None if there is none 
            
        '''
        if current.next1 is None:
            return None
        return current.next1

    def get_next_mru(self, current):
        '''
            Get the next node in order after the current node on the mru list

            @Param current      the node on the mru list preceeding the one to return
            @Return             the next mru node, or None if there is none 
            
        '''
        if current.next2 is None:
            return None
        return current.next2

    def remove(self, target):
        '''
            Remove the target node from both ordered and MRU lists

            @Param target       the node to remove
            @Return this        OrderedMRUList object, so that further calls on it can be chained
            
        '''
        target.remove1().remove2()
        return self

    def add(self, element):
        '''
            Add an element of the base element class type in a new node to the list.
            The new node is added to the ordered list in the correct order as defined
            by the comparable method of the base type (String or Integer), and is added 
            to the front of the MRU list

            @Param element      The element to be wrapped in a new MLNode node and added to the list
            @Return this        OrderedMRUList object, so that further calls on it can be chained
        
        '''
        new_node = MLNode(element)

        next_ordered = self._head_ordered.next1 # ----- works due to the mutable property of objects. Modifying this modifies the original object of self as well

        while next_ordered != self._head_ordered and element > next_ordered.element:
            next_ordered = next_ordered.next1

        new_node.add_before1(next_ordered)

        self.touch(new_node)

        return self
