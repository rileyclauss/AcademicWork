import as8
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")



class MyTester(unittest.TestCase):

    def test_s(self):
        self.assertEqual(as8.cost(100),52000)
        self.assertEqual(as8.cost(150),77000) 
        self.assertEqual(as8.revenue(100),100000)
        self.assertEqual(as8.revenue(150),75000) 
        self.assertEqual(as8.profit(100),48000)
        self.assertEqual(as8.profit(150),-2000) 
        
    def test_B(self):
        g = lambda x: x**3 - x + 1
        self.assertAlmostEqual(abs(as8.bisect(g,-10.0,10.0,.001)),1.32,1)
      
    def test_S(self):
        g = lambda x: x**3 - x + 1
        self.assertAlmostEqual(abs(as8.secant(g,-10.0,10.0,.0001)),1.324,2)   
    
    def test_I(self):
        g = lambda x: x**3 - x + 1
        self.assertAlmostEqual(as8.simpson(g,0,5,10),148.75,2)

    def test_H(self):
        Htest = [[4, 1, 4], [4, 2, 6], [4, 3, 2], [4, 4, 8]]
        for i,j,k in Htest:
            self.assertEqual(as8.V(i,j),k)
            self.assertEqual(as8.Vm(i,j),k)
            self.assertEqual(as8.Vh(i,j),k)

if __name__=="__main__":
    unittest.main()

