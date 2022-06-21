import a3
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


class TestA3(unittest.TestCase):

    def test_y(self):
        self.assertAlmostEqual(a3.y(1000,0.02,10),1221.40,1) 
        self.assertAlmostEqual(a3.y(500,1.4,5),548316.57,1) 
        self.assertAlmostEqual(a3.y(7500,.09,3),9824.73,1) 

    def test_N(self):
        self.assertAlmostEqual(a3.N(500,100,4)/(1e176),2.61,1) 
        self.assertAlmostEqual(a3.N(250,30,2)/(1e28),2.86,1) 
        self.assertAlmostEqual(a3.N(100,14,1)/(1e8),1.20,1) 

    def test_N_t(self):
        self.assertEqual(a3.N_t(1000),72) 
        self.assertEqual(a3.N_t(75),69) 
        self.assertEqual(a3.N_t(50),54) 

    def test_K(self):
        shift = 1e4
        self.assertAlmostEqual(a3.K(1)*shift,69.2,1) 
        self.assertAlmostEqual(a3.K(2)*shift,62.9,1) 
        self.assertAlmostEqual(a3.K(3)*shift,49.5,1) 


    def test_r(self):
        self.assertAlmostEqual(a3.r(4),1219.53,2) 
        self.assertAlmostEqual(a3.r(5),1183.8,2) 
        self.assertAlmostEqual(a3.r(6),1158.17,2) 


    def test_W(self):
        self.assertEqual(a3.W(10,1),5744) 
        self.assertEqual(a3.W(10,2),4015) 
        self.assertEqual(a3.W(20,1.5),6461) 

    def test_dep(self):
        self.assertEqual(a3.dep(20000,1000,5),3800.0) 
        self.assertEqual(a3.dep(10000,500,10),950.0) 
        self.assertEqual(a3.dep(40000,2000,3),12667.0) 

    def test_L(self):
        self.assertEqual(a3.L(33.8,512,0.515),995) 
        self.assertEqual(a3.L(30.8,512,0.515),826) 
        self.assertEqual(a3.L(25.8,512,0.515),580) 

    def test_q(self):
        self.assertEqual(a3.q(1,3,-4),(1.0,-4.0)) 
        left,right = a3.q(2,-4,3)
        lr, li = left.real, left.imag
        self.assertAlmostEqual(lr,1.0,1)
        self.assertAlmostEqual(li*100,70.71,2)
        rr, ri =  right.real, right.imag
        self.assertAlmostEqual(rr,1.0,1)
        self.assertAlmostEqual(ri*100,-070.71,2)

        left,right = a3.q(9,12,4)
        self.assertAlmostEqual(left*100,-66.67,1)
        self.assertAlmostEqual(right*100,-66.67,1)

        left,right = a3.q(3,4,2)
        lr, li = left.real, left.imag
        self.assertAlmostEqual(lr*100,-66.67,1)
        self.assertAlmostEqual(li*100,47.14,2)
        rr, ri =  right.real, right.imag
        self.assertAlmostEqual(rr*100,-66.67,1)
        self.assertAlmostEqual(ri*100,-47.14,2)
        
    def test_checkout(self):
    
        x1 = [[1, 1.45, 1],[3, 4.24, 1], [2, 14.00, 0], [4, 1.25, 1]]
        x2 = [[3, 2.05, 1],[1, 4.74, 0], [2, 4.00, 1], [5, 4.25, 1]]
        x3 = [[1, 2.05, 0],[1, 4.74, 1], [2, 4.00, 0], [5, 4.25, 0]]
    
        self.assertAlmostEqual(a3.checkout(x1),48.51,1) 
        self.assertAlmostEqual(a3.checkout(x2),42.62,1) 
        self.assertAlmostEqual(a3.checkout(x3),36.37,1)    

    def test_e(self):

        s1 = [[1,0,0],[1,1,1],[1,1,0]]
        s2 = [[1]]
        s3 = [[0]]
        s4 = [[1,1],[1,1],[1,1],[1,0]]
        s5 = [[1],[0],[0]]
        s6 = [[1,0,0,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,0,1],[1,0,0,1,1,1,1,1,0,1]]
        
        self.assertEqual(a3.open_seat_count(s1),3) 
        self.assertEqual(a3.open_seat_count(s2),0) 
        self.assertEqual(a3.open_seat_count(s3),1) 
        self.assertEqual(a3.open_seat_count(s4),1) 
        self.assertEqual(a3.open_seat_count(s5),2) 
        self.assertEqual(a3.open_seat_count(s6),9)

    def test_stats(self):

        er_msg0 = "Data Error: 0 values"
        er_msg1 = "Data Error: 0 in data"
        vlst = [[[], er_msg0], [[34,24.3],29.15], \
        [[2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400],2530.0]]
        for i,j in vlst:
            if isinstance(j,str):
                self.assertEqual(a3.arithmetic_mean(i), j)
            else:
                self.assertAlmostEqual(a3.arithmetic_mean(i),j,2)
        self.assertEqual(a3.geo_mean([]), er_msg0)
        self.assertAlmostEqual(a3.geo_mean([3,5,6,6,7,10,12]),6.43,2)
        self.assertEqual(a3.har_mean([1,2.3,0,5]), er_msg1)
        self.assertEqual(a3.har_mean([]), er_msg0)
        self.assertAlmostEqual(a3.har_mean([2,4,8]),3.43,2)
        self.assertAlmostEqual(a3.har_mean([3,5,6,6,7,10,12]),5.87,2)
        self.assertEqual(a3.RMS_mean([]), er_msg0)
        self.assertAlmostEqual(a3.RMS_mean([3,5,6,6,7,10,12]),7.55,2) 


    def test_ISBN(self):
        ilist = ["0-691-11321-1", "0-691-12797-2", "0-324-33333-8"]
        self.assertTrue(a3.valid_ISBN(ilist[0]))
        self.assertTrue(a3.valid_ISBN(ilist[1]))
        self.assertFalse(a3.valid_ISBN(ilist[2]))
        
    def test_business(self):
        self.assertEqual(a3.profit(13,10,1000,0),-1000)
        self.assertEqual(a3.profit(13,10,1000,334), 2)
        self.assertEqual(a3.break_even(13,10,1000),334)
        self.assertEqual(a3.profit(13,10,1000,a3.break_even(13,10,1000)), 2)
        self.assertEqual(a3.profit(10,0,10,1),0)
        self.assertEqual(a3.break_even(10,0,10),1)

    def test_realestate(self):
        house1 = [[300000,2.9,30],1248.69, 149528.4]
        house2 = [[100000,6.0,30],599.55,115838.0]
        self.assertAlmostEqual(a3.Mortgage(house1[0]),house1[1],2)
        self.assertAlmostEqual(a3.total_paid(house1[0]), house1[2],2)
        self.assertAlmostEqual(a3.Mortgage(house2[0]),house2[1],2)
        self.assertAlmostEqual(a3.total_paid(house2[0]), house2[2],2)

if __name__=="__main__":
    unittest.main()

