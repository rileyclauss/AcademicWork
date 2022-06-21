import a7
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

xtest1  = [[1,2],[2,3],[3,4]]
vtest1 = 53065.129

testwords = ["", "nolemonnomelon","ratsliveonnoevilstar","abba","madamimadamm"]
testans = [True, True, True, True, False]

testnlst = [587657752,11,22,2728,31415,1358016]
test11ans = [True, True, True, True, False, True ]

testx1 = [1,2,3,4,5,6,7,8,9,10]
testy1 = 5
testz1 = 3
testw1 = [5,4,6]

testx2 = [586, 352, 747, 555, 944, 590, 549, 463, 657, 603] 
testy2 = 985 
testz2 = 4
testw2 = [944, 747, 657, 603]

class MyTester(unittest.TestCase):

    def test_d(self):
        self.assertEqual(a7.d(3),40)
        self.assertEqual(a7.d(4),121) 

    def test_cr(self):
        self.assertEqual(a7.cr(3,1),3)
        self.assertEqual(a7.cr(4,0),1)
        self.assertEqual(a7.cr(4,2),6)

    def test_B(self):
        self.assertAlmostEqual(a7.B(2),0.166,2)
        self.assertAlmostEqual(a7.B(4),-0.033,2)
        
    #def test_G(self):
    #    self.assertAlmostEqual(a7.error(xtest1),vtest1,2)
    
    def test_A(self):
        self.assertEqual(a7.a(3),-1)
        self.assertEqual(a7.am(5),-2)
    
    def test_covid(self):
        dic = a7.get_dic("Assignment7/us-counties.csv")
        state_pop = a7.get_state_pop("Assignment7/sp.csv")
        self.assertEqual(a7.ccc(dic,(0,2))[(0,2)],896)
        self.assertEqual(a7.scd("Alabama", dic),8166)
        self.assertEqual(a7.usdd(dic,state_pop)["Texas"], 0.103)

    def test_div_11(self):
        for i,j in zip(testnlst,test11ans):
            self.assertEqual(a7.div_11(i),j)

    


if __name__=="__main__":
    unittest.main()

