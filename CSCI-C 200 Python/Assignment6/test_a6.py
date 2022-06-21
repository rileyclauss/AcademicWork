import a6
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

bambie = [99,0,18273645,22,27]
thumper = [True, True, True, False, True]
d,c = "d","c"
xbook1 = [[d, 895],[c,7500],[d,339],[c,234],[d,6400],[d,100]]
xbook2 = [[d, 95],[c,500],[d,39],[c,234],[d,600],[d,10]]
s1 = "ATCGATTGAGCTCTAGCG"
s2 = "TAGCTAACTCGAGATCGC"
s3 = "TAACGAACTGGAGACCGC"
answer = "--*-*----*----*---"
xlst = [[1,2,3], "123", (1,2,3), {1,2,3}, {1:1, 2:2, 3:3}]

class MyTester(unittest.TestCase):

    def test_F(self):
        self.assertEqual(a6.F(5,5,5),135)
        self.assertEqual(a6.Ft(5,5,5),135)
        self.assertEqual(a6.F(1,2,3),102)
        self.assertEqual(a6.Ft(1,2,3),102)
        self.assertEqual(a6.F(5,4,2),120)
        self.assertEqual(a6.Ft(5,4,2),120)
    def test_B(self):
        self.assertEqual(a6.B(3),35)
        self.assertEqual(a6.Bt(3),35)
        self.assertEqual(a6.B(4),55)
        self.assertEqual(a6.Bt(4),55)
    
    def test_g(self):
        self.assertEqual(a6.gsf(2,3,5),242)
        self.assertEqual(a6.g(2,3,5),242)
        self.assertEqual(a6.gsf_close(2,3,5),242.0)
        
    def test_x(self):
        self.assertEqual(a6.xt(3),16)
        self.assertEqual(a6.xt(4),25)
        self.assertEqual(a6.x(3),16)
        self.assertEqual(a6.x(4),25)

    def test_div_9(self):
        for i,j in zip(bambie,thumper):
            self.assertEqual(a6.div_9(i),j)
            
    def test_iterable(self):
        for i in xlst:
            self.assertEqual(a6.length_l(i),3)
            self.assertEqual(a6.length_r(i),3)
        

    def test_cicero(self):
        self.assertEqual(a6.cicero(38),"XXXVIII")
        self.assertEqual(a6.cicero(86),"LXXXVI")
        self.assertEqual(a6.cicero(100),"C")
    
    def test_b(self):
        self.assertEqual(a6.bk(xbook1), True)
        self.assertEqual(a6.bk(xbook2), False)
        self.assertEqual(a6.bkr(xbook1), True)
        self.assertEqual(a6.bkr(xbook2), False)
   
    def test_DNA(self):
        self.assertEqual(a6.make_pairing(s1),s2)
        self.assertEqual(a6.findError(s1,s3), answer)


if __name__=="__main__":
    print("Running Test Code")
    unittest.main()

