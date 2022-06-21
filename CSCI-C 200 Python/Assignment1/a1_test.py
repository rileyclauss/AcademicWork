import assignment1_1
import assignment1_2

import unittest
import random as rn
import math 

#DATA
input = [0,1]

class MyTests(unittest.TestCase):

    def test_myAnd(self):
        for i in input:
            for j in input:
                self.assertEqual(assignment1_1.myAnd(i,j),i and j)
       
    def test_myOr(self):
        for i in input:
            for j in input:
                self.assertEqual(assignment1_1.myOr(i,j),i or j)

    def test_myNot(self):
        for i in input:
            self.assertEqual(assignment1_1.myNot(i),not i)

    def test_myNand(self):
        for i in input:
            for j in input:
                self.assertEqual(assignment1_1.myNand(i,j),not (i and j))

    def test_myNor(self):
        for i in input:
            for j in input:
                self.assertEqual(assignment1_1.myNor(i,j),not (i or j))

    def test_myImplication(self):
        for i in input:
            for j in input:
                self.assertEqual(assignment1_1.myImplication(i,j),(not i) or j)

    def test_DeMorganNand(self):
        for i in input:
            for j in input:
                self.assertEqual(assignment1_1.DeMorganNand(i,j),not (not i and not j))

    def test_myPlus(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(-50,50)
            self.assertEqual(assignment1_2.myPlus(x,y),x + y)

    def test_myMinus(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(-50,50)
            self.assertEqual(assignment1_2.myMinus(x,y),x - y)

    def test_myDivide(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(1,50)
            self.assertEqual(assignment1_2.myDivide(x,y),x/y)

    def test_myProduct(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(-50,50)
            self.assertEqual(assignment1_2.myProduct(x,y),x*y)

    def test_myExponent(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(-50,50)
            self.assertEqual(assignment1_2.myExponent(x,y),x**y)

    def test_myRoot(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(1,50)
            self.assertEqual(assignment1_2.myRoot(x,y),x**(1/y))

    def test_myLog(self):
        #make sure don't ask math.log(1,1)
        for i in range(10):
            x,y = rn.randint(1,50), rn.randint(2,50)
            self.assertEqual(assignment1_2.myLog(x,y),math.log(x,y))

    def test_myAbs(self):
        for i in range(10):
            x = rn.randint(-50,50)
            self.assertEqual(assignment1_2.myAbs(x),abs(x))

    def test_myExp(self):
        for i in range(10):
            x = rn.randint(-50,50)
            self.assertEqual(assignment1_2.myExp(x),math.exp(x))

    def test_myFloor(self):
        for i in range(10):
            x,y = rn.randint(-50,50), rn.randint(1,50)
            self.assertEqual(assignment1_2.myFloor(x/y),math.floor(x/y))


if __name__=="__main__":
    unittest.main()

