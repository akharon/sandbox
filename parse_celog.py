#!/usr/bin/python 

import unittest

class CelogElement:
    def __init__(self, id, name, baseprio):
        self.id = id
        self.name = name
        self.baseprio = baseprio
        self.prio = []

class MyCelogList:

    def __init__(self):
        self.lst = []
        
    def search(self, id):
        for element in self.lst:
            if id == element.id:
                return element
        return None

    def add(self, id, name, baseprio):
        if None == self.search(id) :
            element = CelogElement(id, name, baseprio)
            self.lst.append(element)
            return True
        return False
        
    def add_prio(self, id, prio):
        element = self.search(id)
        if(len(element.prio) < 10) :
            if prio not in element.prio:
                element.prio.append(prio)
                return True
        else :
            print "Exceeded prio assingment limit"
            
        return False
    
    def length(self):
        return len(self.lst)
    
class ParseFile(unittest.TestCase):
    
    def test_empty(self):
        lst = MyCelogList()
        self.assertEqual(lst.length(), 0)

    def test_add(self):
        lst = MyCelogList()
        lst.add(4567889, "ThreadX", 128)
        self.assertEqual(lst.length(), 1)

    def test_search(self):
        lst = MyCelogList()
        lst.add(4567889, "ThreadX", 128)
        self.assertEqual( lst.search(4567889).name, "ThreadX")
        
    def test_prio_length(self):
        lst = MyCelogList()
        lst.add(4567889, "ThreadX", 128)
        lst.add_prio(4567889, 255)
        self.assertEqual( len(lst.search(4567889).prio), 1)

    def test_prio(self):
        lst = MyCelogList()
        lst.add(4567889, "ThreadX", 128)
        lst.add_prio(4567889, 255)
        self.assertEqual( lst.search(4567889).prio[0], 255)

        
if __name__ == "__main__":
    unittest.main()