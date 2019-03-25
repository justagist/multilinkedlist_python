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
        self.assertEqual(None, oml.get_first_ordered(),"After initialization, getFirstOrdered")
        self.assertEqual(None, oml.get_first_mru(),"After initialization, getFirstMru")

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

    


if __name__ == '__main__':
    unittest.main()
