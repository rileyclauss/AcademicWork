import a2_assignment
import unittest

print("__________________________________________")
print("KEY")
print(". = passed")
print("F = failed on value") 
print("0 = unrecoverable error")
print("__________________________________________")


class TestA1(unittest.TestCase):
    def test_s(self):
        for i,j in zip([25,35,45,70,55],[25,36,48,75,60]):
            self.assertEqual(a2_assignment.s(i),j)

    def test_E(self):
        i = [.1,.5,10,15,100]
        v = [9000000000000000.0, 4.5e+16, 9e+17, 1.35e+18, 9e+18]
        s = [15,16,17,18,18]
        for i,j,s in zip(i,v,s):
            s = 10**(s-1)
            self.assertAlmostEqual(a2_assignment.E(i)/s,j/s,3)

    def test_f(self):
        x = [(1, 7.50, 10, 200), (1, 20.00, 10, 200), (3, 20.00, 10, 200), (3, 20.00, 35, 200)]
        y = [False, True, False, True]
        for i,j in zip(x,y):
            self.assertEqual(a2_assignment.f(*i),j)
 
    def test_law_of_cosines(self):
        x = [(50,3,4), (47,9,10), (90,5,5)]
        y = [3.09, 7.63, 7.07]
        for i,j in zip(x,y):
            self.assertAlmostEqual(a2_assignment.law_cosines(*i),j,2)

    def test_max_(self):
        x = [(1,2),(2,1),(2,2)]
        y = [(1,2,3),(3,2,1),(1,3,2),(3,3,3)]
        for i in x:
            self.assertEqual(a2_assignment.max(*i),2)
        for i in y:
            self.assertEqual(a2_assignment.max_3(*i),3)
        for i in y:
            self.assertEqual(a2_assignment.max_3h(*i),3)

    def test_color_wheel(self):
        x = [("yellow", "blue","green"),("blue", "yello","unknown"), \
             ("yellow", "yellow","yellow"),("orange", "yellow","unknown")]
        for i in x:
            self.assertEqual(a2_assignment.color_wheel(*i[0:2]),i[2])

    def test_cost_per_inch(self):
        x = [(18,10,12,7,18),(18,10,12,5,18),(18,10,12,4,12)]
        for i in x:
            self.assertEqual(a2_assignment.cost_per_inch(*i[0:4]),i[4])
        

if __name__=="__main__":
    unittest.main()