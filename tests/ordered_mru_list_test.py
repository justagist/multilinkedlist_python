import unittest
from src import MLNode, OrderedMRUList

import logging

# fmt = '[%(levelname)s] -- %(lineno)d: %(message)s\n'
# logging.basicConfig(format=fmt, level=logging.DEBUG)

class OrderedMRUListUnitTest(unittest.TestCase):

    def test_initialise_list(self):
        oml = OrderedMRUList()

        self.assertEqual(True, oml.is_empty_ordered(),"Intialization of OrderedMRUList failed")
        self.assertEqual(True, oml.is_empty_mru(),"Intialization of OrderedMRUList failed")
        self.assertEqual(None, oml.get_first_ordered(),"After initialization, get_first_ordered")
        self.assertEqual(None, oml.get_first_mru(),"After initialization, get_first_mru")

    def test_add_ordered(self):
        oml = OrderedMRUList()
        oml.add("E").add("A").add("C").add("B").add("D")
        e1 = oml.get_first_ordered()  # A
        e2 = oml.get_next_ordered(e1) # B
        e3 = oml.get_next_ordered(e2) # C
        e4 = oml.get_next_ordered(e3) # D
        e5 = oml.get_next_ordered(e4) # E
        e6 = oml.get_next_ordered(e5) # None
        
        ordered = "%s %s %s %s %s %s"%(e1.element, e2.element, e3.element,e4.element, e5.element, "None" if e6 == None else e6.element)
        
        self.assertEqual("A B C D E None", ordered,"Adding to OrderedMRUList, ordered part")

        self.assertEqual(False, oml.is_empty_ordered(),"Adding to OrderedMRUList, Not is_empty_ordered")

    def test_add_mru(self):
        oml = OrderedMRUList()
        oml.add("E").add("A").add("C").add("B").add("D")
        e1 = oml.get_first_mru()  # A
        e2 = oml.get_next_mru(e1) # B
        e3 = oml.get_next_mru(e2) # C
        e4 = oml.get_next_mru(e3) # D
        e5 = oml.get_next_mru(e4) # E
        e6 = oml.get_next_mru(e5) # None
        
        mru = "%s %s %s %s %s %s"%(e1.element, e2.element, e3.element,e4.element, e5.element, "None" if e6 == None else e6.element)
        
        self.assertEqual("D B C A E None", mru,"Adding to OrderedMRUList, mru part")

        self.assertEqual(False, oml.is_empty_ordered(),"Adding to OrderedMRUList, Not is_empty_mru")

    def test_touch(self):
        oml = OrderedMRUList()
        oml.add("E").add("D").add("C").add("B").add("A")
        e1 = oml.get_first_mru() # A
        e2 = oml.get_next_mru(e1)# B
        e3 = oml.get_next_mru(e2)# C
        e4 = oml.get_next_mru(e3)# D
        e5 = oml.get_next_mru(e4)# E
        e6 = oml.get_next_mru(e5)# None
        
        oml.touch(e1)# make sure touching the first on the MRU list also works
        oml.touch(e2)
        oml.touch(e4)
        oml.touch(e2)
        
        e1 = oml.get_first_mru() # B
        e2 = oml.get_next_mru(e1)# D
        e3 = oml.get_next_mru(e2)# A
        e4 = oml.get_next_mru(e3)# C
        e5 = oml.get_next_mru(e4)# E
        e6 = oml.get_next_mru(e5)# None

        mru = "%s %s %s %s %s %s"%(e1.element, e2.element, e3.element, e4.element, e5.element, "None" if e6 == None else e6.element)
        
        self.assertEqual("B D A C E None", mru,"Touching elements, MRU part")

        e1 = oml.get_first_ordered() # A
        e2 = oml.get_next_ordered(e1)# B
        e3 = oml.get_next_ordered(e2)# C
        e4 = oml.get_next_ordered(e3)# D
        e5 = oml.get_next_ordered(e4)# E
        e6 = oml.get_next_ordered(e5)# None

        ordered = "%s %s %s %s %s %s"%(e1.element, e2.element, e3.element,e4.element, e5.element, "None" if e6 == None else e6.element)

        self.assertEqual("A B C D E None", ordered,"Touching elements, Ordered part")

    def test_remove(self):

        oml = OrderedMRUList()
        self.assertIsNotNone(oml,"Intialization of OrderedMRUList failed")

        oml.add("E")
        oml.add("D")
        oml.add("C")
        oml.add("B")
        oml.add("A")

        e1 = oml.get_first_ordered()  # A
        self.assertIsNotNone(e1,"Adding to and getting from OrderedMRUList before removing failed")
        e2 = oml.get_next_ordered(e1) # B
        self.assertIsNotNone(e2,"Adding to and getting from OrderedMRUList before removing failed")
        e3 = oml.get_next_ordered(e2) # C
        self.assertIsNotNone(e3,"Adding to and getting from OrderedMRUList before removing failed")
        e4 = oml.get_next_ordered(e3) # D
        self.assertIsNotNone(e3,"Adding to and getting from OrderedMRUList before removing failed")
        e5 = oml.get_next_ordered(e4) # E
        self.assertIsNotNone(e5,"Adding to and getting from OrderedMRUList before removing failed")
        
        oml.remove(e3) # remove C
        oml.remove(e1) # remove A
        oml.remove(e5) # remove E
        
        x1 = oml.get_first_ordered()  # B
        self.assertIsNotNone(x1,"Getting from OrderedMRUList after removing from Ordered part failed")
        x2 = oml.get_next_ordered(x1) # D
        self.assertIsNotNone(x2,"Getting from OrderedMRUList after removing Ordered part failed")
        x3 = oml.get_next_ordered(x2) # None
        self.assertIsNotNone(x3,"Getting from OrderedMRUList after removing Ordered part failed")
        
        ordered = "%s %s %s"%(x1.element, x2.element, "None" if x3 == None else x3.element)
        
        self.assertEqual("B D None", ordered,"Removing from OrderedMRUList, Ordered part")
        
        x1 = oml.get_first_mru()  # B
        self.assertIsNotNone(x1,"Getting from OrderedMRUList after removing from Mru part failed")
        x2 = oml.get_next_mru(x1) # D
        self.assertIsNotNone(x2,"Getting from OrderedMRUList after removing from Mru part failed")
        x3 = oml.get_next_mru(x2) # None
        self.assertIsNotNone(x3,"Getting from OrderedMRUList after removing from Mru part failed")

        mru = "%s %s %s"%(x1.element, x2.element, "None" if x3 == None else x3.element)
        
        self.assertEqual("B D None", ordered,"Removing from OrderedMRUList, MRU part")

        oml.remove(e4)
        oml.remove(e2)
        
        self.assertTrue("After removing all from OrderedMRUList, Ordered part, is_empty_ordered() should be true", oml.is_empty_ordered())
        self.assertTrue("After emoving all from OrderedMRUList, Mru part, is_empty_mru() should be true", oml.is_empty_mru())


if __name__ == '__main__':
    unittest.main()
