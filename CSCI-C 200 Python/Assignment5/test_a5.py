import a5
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

s1 = ['a','b','a','b','a','b','b','b']
s2 = [(1),(2),(3),(4)]
s3 = [1]
s4 = [1,2]
xlst = [s1,s2,s3,s4]
elst = [0.9544340029249649, 2.0, -0.0, 1.0]

ms1 = [[4, 9, 2],[3,5,7],[8,1,6]]
ms2 = [[4, 9, 2],[3,5,7],[8,2,6]]

class MyTester(unittest.TestCase):

        def test_Problem1(self):
                for i,j in zip(xlst, elst):
                        self.assertAlmostEqual(a5.entropy(a5.makeProbability(i)),j,1)
        
        def test_Problem3(self):
                s1 = [[2,7,6],[9,5,1],[4,3,8]] #True
                s2 = [[8,1,6],[3,5,7],[4,9,2]] #True
                s3 = [[8,6,1],[3,6,7],[4,9,2]] #False
                s4 = [[1,1,1],[1,1,1],[1,1,1]] #False
                s = [s1,s2,s3,s4]
                an = [True, True, False, False]
        
                for i,j in zip(s,an):
                        self.assertEqual(a5.is_magic_square(i), j)
        
        def test_Problem4(self):
                xs = "the quick brown fox jumps over the lazy dog"
                ys = "two roads diverged in a yellow wood"
                shift = rn.randint(1,10)
                self.assertEqual(a5.decrypt_sentence(a5.encrypt_sentence(xs, shift), shift),xs)
                self.assertEqual(a5.decrypt_sentence(a5.encrypt_sentence(ys, shift), shift),ys)
                
        def test_Problem5(self):
                n1,n2,n3,n4 = 5,4,3,4
                base2, base10, base3, base4 = 2,10,3,4

                x1 = a5.make_number(n1,base2)
                y1 = a5.make_number(n2,base2)
                zz = a5.make_number(4,base3)
                yy = a5.make_number(3,base4)
                self.assertEqual(x1,['101', 2])
                self.assertEqual(y1, ['100', 2])
                self.assertEqual(a5.convert(x1,base10),['5', 10] )
                self.assertEqual(a5.add_(x1,y1,base10), ['9', 10])
                self.assertEqual(a5.mul_(zz,yy,10), ['12', 10])        
    
        def test_Problem6(self):
                tiny_FASTA0 = ["nothing", "CCACTGCACTCA"] 
                tiny_protein0 = "PLHS"
                tiny_FASTA1 = ["nothing", "GACTAA"]
                tiny_protein1 = "D-"
                actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

                self.assertEqual(a5.translate(tiny_FASTA0), tiny_protein0)
                self.assertEqual(a5.translate(tiny_FASTA1), tiny_protein1)
                self.assertEqual(a5.protein, actual)


            


if __name__=="__main__":
    unittest.main()

