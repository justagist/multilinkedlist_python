import unittest
from src import MLNode

import logging

# fmt = '[%(levelname)s] -- %(lineno)d: %(message)s\n'
# logging.basicConfig(format=fmt, level=logging.DEBUG)

class MLNodeUnitTest(unittest.TestCase):

    def test_initialise_node(self):
        
        n = MLNode('abc')
        self.assertEqual("abc", n.element,"Initialization of MLNode failed on item")
        self.assertEqual(n, n.prev1,"Initialization of MLNode failed on prev1")
        self.assertEqual(n, n.next1,"Initialization of MLNode failed on next1")
        self.assertEqual(n, n.prev2,"Initialization of MLNode failed on prev2")
        self.assertEqual(n, n.next2,"Initialization of MLNode failed on next2")

    def test_add_element(self):

        n0 = MLNode(0)
        n1 = MLNode(1)
        n2 = MLNode(2)
        n3 = MLNode(3)
        
        n3.add_after1(n0)  # 0-3, 1, 2
        n2.add_before1(n3) # 0-2-3. 1
        n1.add_after1(n0)  # 0-1-2-3
        
        n3.add_before2(n0)  # 3-0, 1, 2
        n2.add_after2(n3) # 3-2-0. 1
        n1.add_before2(n0)  # 3-2-1-0
        
        self.assertEqual(n3, n0.prev1, "adding1")
        self.assertEqual(n0, n1.prev1, "adding1")
        self.assertEqual(n1, n2.prev1, "adding1")
        self.assertEqual(n2, n3.prev1, "adding1")
        self.assertEqual(n1, n0.next1, "adding1")
        self.assertEqual(n2, n1.next1, "adding1")
        self.assertEqual(n3, n2.next1, "adding1")
        self.assertEqual(n0, n3.next1, "adding1")
        
        
        self.assertEqual(n1, n0.prev2,"adding2")
        self.assertEqual(n2, n1.prev2,"adding2")
        self.assertEqual(n3, n2.prev2,"adding2")
        self.assertEqual(n0, n3.prev2,"adding2")
        self.assertEqual(n3, n0.next2,"adding2")
        self.assertEqual(n0, n1.next2,"adding2")
        self.assertEqual(n1, n2.next2,"adding2")
        self.assertEqual(n2, n3.next2,"adding2")

    def test_add_element_without_removing1(self):

        n0 = MLNode(0)
        n1 = MLNode(1)
        n2 = MLNode(2)
        
        n1.add_after1(n0)  
        n2.add_after1(n1)  # 0-1-2

        n1.add_after1(n2)  # 0-2-1
        
        self.assertEqual(n2.element, n0.next1.element,"adding After Without Removing 1")
        self.assertEqual(n1.element, n2.next1.element,"adding After Without Removing 1")
        self.assertEqual(n0.element, n1.next1.element,"adding After Without Removing 1")

        n1.add_before1(n2) # 0-1-2

        self.assertEqual(n1.element, n0.next1.element,"adding Before Without Removing 1")
        self.assertEqual(n2.element, n1.next1.element,"adding Before Without Removing 1")
        self.assertEqual(n0.element, n2.next1.element,"adding Before Without Removing 1")


    def test_add_element_without_removing2(self):

        n0 = MLNode(0)
        n1 = MLNode(1)
        n2 = MLNode(2)
        
        n1.add_after2(n0)  
        n2.add_after2(n1)  # 0-1-2

        n1.add_after2(n2)  # 0-2-1
        
        self.assertEqual(n2.element, n0.next2.element,"adding After Without Removing 1")
        self.assertEqual(n1.element, n2.next2.element,"adding After Without Removing 1")
        self.assertEqual(n0.element, n1.next2.element,"adding After Without Removing 1")

        n1.add_before2(n2) # 0-1-2

        self.assertEqual(n1.element, n0.next2.element,"adding Before Without Removing 1")
        self.assertEqual(n2.element, n1.next2.element,"adding Before Without Removing 1")
        self.assertEqual(n0.element, n2.next2.element,"adding Before Without Removing 1")

    def test_remove_element(self):

        n0 = MLNode(0)
        n1 = MLNode(1)
        n2 = MLNode(2)
        
        n1.add_after1(n0)
        n2.add_after1(n1)
        
        n1.add_after2(n0)
        n2.add_after2(n1)
        
        x1 = n1.remove1()  # list 1: 0-2, 1
        x2 = n2.remove2()  # list 2: 0-1, 2

        self.assertEqual(n1, x1,"Remove1 returning argument")
        self.assertEqual(n1, x1.next1,"Remove1 returning argument")
        self.assertEqual(n1, x1.prev1,"Remove1 returning argument")
        
        self.assertEqual(n2, x2,"Remove2 returning argument")
        self.assertEqual(n2, x2.next2,"Remove2 returning argument")
        self.assertEqual(n2, x2.prev2,"Remove2 returning argument")
        
        self.assertEqual(n2, n0.next1,"Remove1 remaining list")
        self.assertEqual(n0, n2.next1,"Remove1 remaining list")
        self.assertEqual(n2, n0.prev1,"Remove1 remaining list")
        self.assertEqual(n0, n2.prev1,"Remove1 remaining list")

        self.assertEqual(n1, n0.next2,"Remove2 remaining list")
        self.assertEqual(n0, n1.next2,"Remove2 remaining list")
        self.assertEqual(n1, n0.prev2,"Remove2 remaining list")
        self.assertEqual(n0, n1.prev2,"Remove2 remaining list")


if __name__ == '__main__':
    unittest.main()



