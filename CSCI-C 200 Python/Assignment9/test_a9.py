import a9
import unittest
from datetime import date

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

class MyTester(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(a9.distance((4,0),(0,3)), 5)

    def test_brute(self): 
        x = [(5,5),(50,50),(75,75),(4,4)]  
        y = sorted(a9.brute(x)[0:2])
        self.assertEqual(y, [(4, 4), (5, 5)])

    def test_productivity(self):
        self.assertAlmostEqual(a9.productivity(55),883.30,1)
      
    def test_nn(self):
        x = [1,2,3,4,5,6,7,8,9,10]
        y = 5
        z = 3
        self.assertEqual(sorted(a9.nn(x,y,z)), sorted([5, 6, 4]))

        x = [1.6,2,3]
        y = 2
        z = 2
        self.assertEqual(sorted(a9.nn(x,y,z)), sorted([2, 1.6]))


        x = [1,2,3,3]
        y = 2
        z = 3
        self.assertIn(sorted(a9.nn(x,y,z)), [[1,2,3],[2,3,3]])

    def test_bank(self):
        today = str(date.today())[0:11]
        x,y,a = a9.Bank("x",10,20), a9.Bank("y",1,2), a9.Bank("a",0,0)
        z = x.cut_check(5)
        y.deposit(z, "checking")
        self.assertEqual(z, (1,5,0))
        self.assertEqual(y.checking, 6)   
        self.assertEqual(x.checks_written, [['#100', today, 5, 'Acct: 1']])
        x.cut_check(25)
        x.cut_check(25)
        self.assertIn("$50", x.__str__())

if __name__=="__main__":
    unittest.main()

