
# Assignment5

## Canvas Score: 77/100
The score in Canvas is out of 100 and is the final grade, but for readability, the test case values have been scaled to whole numbers, and this information is presented below. 


Breakdown Score: 68/89 

Username: rclauss

Commit hash used for grading: 1a0b2894a3a4cb3ecd4a0ea8b5134a19aeeb533d



## Problem Breakdown 

### Problem 1: 18/18
- log_2: 6/6.0
- makeProbability: 6/6.0
- entropy: 6/6.0 


### Problem 2: 9/17
- magick: 9/17.0 


### Problem 3: 14/18
- is_magic_square: 9/9.0
- generate_3_square: 5/9.0 


### Problem 4: 10/18
- encrypt: 5/9.0
- decrypt: 5/9.0 


### Problem 5: 17/18
- make_number: 9/9.0
- convert: 8/9.0 


### Problem 6: 0/0
 
 

## Test Results


---
**entropy**
 
Passed: True
Input: ([12, 100, 60, 47, 47, 86, 79, 58, 71, 46],)
Solution: -3665.09 
Student Result: -3665.086197971561

 
Passed: True
Input: ([43],)
Solution: -233.33 
Student Result: -233.3293844521902

 
Passed: True
Input: ([91, 59, 97, 93],)
Solution: -2187.62 
Student Result: -2187.6185672956285

 
Passed: True
Input: ([19, 39, 18, 47, 40, 44, 37, 100, 5],)
Solution: -1944.8 
Student Result: -1944.8027843415828

 
Passed: True
Input: ([39, 88, 13, 69, 27, 47],)
Solution: -1633.6 
Student Result: -1633.6022114165005


---
**magick**
 
Passed: False
Input: (91,)
Solution: 91.0 
Student Result: 103.0

 
Passed: False
Input: (18,)
Solution: 18.0 
Student Result: 30.0

 
Passed: False
Input: (78,)
Solution: 78.0 
Student Result: 90.0

 
Passed: False
Input: (41,)
Solution: 41.0 
Student Result: 53.0

 
Passed: False
Input: (88,)
Solution: 88.0 
Student Result: 100.0


---
**log_2**
 
Passed: True
Input: (69,)
Solution: 6.10852445677817 
Student Result: 6.10852445677817

 
Passed: True
Input: (37,)
Solution: 5.20945336562895 
Student Result: 5.20945336562895

 
Passed: True
Input: (57,)
Solution: 5.832890014164742 
Student Result: 5.832890014164742

 
Passed: True
Input: (70,)
Solution: 6.129283016944967 
Student Result: 6.129283016944967

 
Passed: True
Input: (40,)
Solution: 5.321928094887363 
Student Result: 5.321928094887363


---
**make_number**
 
Passed: True
Input: (10, 2)
Solution: ['1010', 2] 
Student Result: ['1010', 2]

 
Passed: True
Input: (50, 5)
Solution: ['200', 5] 
Student Result: ['200', 5]

 
Passed: True
Input: (1830, 3)
Solution: ['2111210', 3] 
Student Result: ['2111210', 3]

 
Passed: True
Input: (888, 9)
Solution: ['1186', 9] 
Student Result: ['1186', 9]


---
**makeProbability**
 
Passed: True
Input: (['d', 'h', 'y', 's', 't', 'a', 'r', 'o', 'u', 'z', 'a', 'w', 'b', 't', 'p', 'o', 'd', 'j', 'h', 'k', 'c', 'v', 'q', 'c', 'x', 'x', 's', 'z', 'e', 'a', 'q', 'c', 'k', 'a', 'd', 'o', 'r', 'e', 'a', 'e', 'r', 'h', 'r', 'g', 'j', 'y', 'o', 'c', 'r', 'c', 'i', 'o', 'u', 'b', 'q', 'a', 'b', 'i', 'b', 's', 'v', 'b', 'a', 'r', 's', 'v', 'u', 'i', 'b', 's', 'f', 'x', 'g', 'k', 'l'],)
Solution: [0.04, 0.04, 0.02666666666666667, 0.06666666666666667, 0.02666666666666667, 0.09333333333333334, 0.08, 0.06666666666666667, 0.04, 0.02666666666666667, 0.013333333333333334, 0.08, 0.013333333333333334, 0.02666666666666667, 0.04, 0.06666666666666667, 0.04, 0.04, 0.04, 0.04, 0.02666666666666667, 0.04, 0.013333333333333334, 0.013333333333333334] 
Student Result: [0.04, 0.04, 0.02666666666666667, 0.06666666666666667, 0.02666666666666667, 0.09333333333333334, 0.08, 0.06666666666666667, 0.04, 0.02666666666666667, 0.013333333333333334, 0.08, 0.013333333333333334, 0.02666666666666667, 0.04, 0.06666666666666667, 0.04, 0.04, 0.04, 0.04, 0.02666666666666667, 0.04, 0.013333333333333334, 0.013333333333333334]

 
Passed: True
Input: (['g', 'a', 'z', 'w', 'c', 'x', 'k', 'i', 't', 'r', 'n', 'b', 'w', 'k', 'g', 'm', 'i', 'e', 'd', 'i', 'z', 'g', 'k', 'i', 't', 'n', 'd', 'b', 'z', 'i', 'z', 'v', 'v', 'p', 'x', 'n', 'x', 'j', 't', 'v', 'q', 'u', 'o', 'g', 'g', 'd', 'f', 'q', 'z', 'a', 'y', 'o', 'n', 'i', 'w', 'c', 'f', 'o', 'p', 'j', 'j', 'r', 't', 'd', 'y', 's', 'f', 'p', 'q', 's', 'o', 'k', 'q', 'l', 's', 'u', 'e', 'x', 's', 'l', 'i', 'n', 'd', 'r', 's', 'm', 'a', 'j', 'u', 'b', 'p', 'r', 'r', 'r', 'z', 'b', 'r'],)
Solution: [0.05154639175257732, 0.030927835051546393, 0.061855670103092786, 0.030927835051546393, 0.020618556701030927, 0.041237113402061855, 0.041237113402061855, 0.07216494845360824, 0.041237113402061855, 0.07216494845360824, 0.05154639175257732, 0.041237113402061855, 0.020618556701030927, 0.020618556701030927, 0.05154639175257732, 0.030927835051546393, 0.041237113402061855, 0.041237113402061855, 0.041237113402061855, 0.030927835051546393, 0.041237113402061855, 0.030927835051546393, 0.020618556701030927, 0.05154639175257732, 0.020618556701030927] 
Student Result: [0.05154639175257732, 0.030927835051546393, 0.061855670103092786, 0.030927835051546393, 0.020618556701030927, 0.041237113402061855, 0.041237113402061855, 0.07216494845360824, 0.041237113402061855, 0.07216494845360824, 0.05154639175257732, 0.041237113402061855, 0.020618556701030927, 0.020618556701030927, 0.05154639175257732, 0.030927835051546393, 0.041237113402061855, 0.041237113402061855, 0.041237113402061855, 0.030927835051546393, 0.041237113402061855, 0.030927835051546393, 0.020618556701030927, 0.05154639175257732, 0.020618556701030927]

 
Passed: True
Input: (['q', 'z', 'l', 'z', 'w', 'd', 'm', 'k', 'b', 'r', 'n', 'z', 'j', 'j', 't', 'v', 'e', 'x', 'z', 'd', 'c', 'm', 'v', 'y', 'i', 'r', 'n', 'f', 'r', 'v', 'p', 'b', 'f', 'd', 'b', 'a', 'e', 'v', 'v', 'k', 'n', 'm', 'f', 'n', 's', 'g', 's', 't', 'r', 'u', 'e', 't', 'y', 'y', 'o', 'v', 's', 'q', 'i', 't', 'k', 'm', 'd', 'h', 'h', 'g', 'd', 'a', 'z', 'a', 'w', 'x', 'm', 'x', 'd', 'n', 'q', 'f', 'o', 'm', 't', 'e', 'a', 'a', 'p', 'h', 'y', 'v', 'x'],)
Solution: [0.033707865168539325, 0.056179775280898875, 0.011235955056179775, 0.02247191011235955, 0.06741573033707865, 0.06741573033707865, 0.033707865168539325, 0.033707865168539325, 0.0449438202247191, 0.056179775280898875, 0.02247191011235955, 0.056179775280898875, 0.07865168539325842, 0.0449438202247191, 0.0449438202247191, 0.011235955056179775, 0.0449438202247191, 0.02247191011235955, 0.0449438202247191, 0.02247191011235955, 0.056179775280898875, 0.033707865168539325, 0.02247191011235955, 0.011235955056179775, 0.02247191011235955, 0.033707865168539325] 
Student Result: [0.033707865168539325, 0.056179775280898875, 0.011235955056179775, 0.02247191011235955, 0.06741573033707865, 0.06741573033707865, 0.033707865168539325, 0.033707865168539325, 0.0449438202247191, 0.056179775280898875, 0.02247191011235955, 0.056179775280898875, 0.07865168539325842, 0.0449438202247191, 0.0449438202247191, 0.011235955056179775, 0.0449438202247191, 0.02247191011235955, 0.0449438202247191, 0.02247191011235955, 0.056179775280898875, 0.033707865168539325, 0.02247191011235955, 0.011235955056179775, 0.02247191011235955, 0.033707865168539325]

 
Passed: True
Input: (['b', 'u', 'd', 't', 'f', 'q', 'n', 'l', 'q', 'v', 'b', 'd', 'q', 'z'],)
Solution: [0.14285714285714285, 0.07142857142857142, 0.14285714285714285, 0.07142857142857142, 0.07142857142857142, 0.21428571428571427, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142] 
Student Result: [0.14285714285714285, 0.07142857142857142, 0.14285714285714285, 0.07142857142857142, 0.07142857142857142, 0.21428571428571427, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142]

 
Passed: True
Input: (['a', 'i', 'r', 's', 'n', 's', 'v', 'p', 'b', 'd', 'l', 'q', 'd', 'q', 'r', 'w', 'v', 't', 'd', 'i', 'j', 'q', 'a', 'u', 'f', 'n', 'w', 'h', 'b'],)
Solution: [0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.034482758620689655, 0.06896551724137931, 0.10344827586206896, 0.034482758620689655, 0.10344827586206896, 0.06896551724137931, 0.034482758620689655, 0.034482758620689655, 0.034482758620689655, 0.034482758620689655, 0.034482758620689655] 
Student Result: [0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.06896551724137931, 0.034482758620689655, 0.06896551724137931, 0.10344827586206896, 0.034482758620689655, 0.10344827586206896, 0.06896551724137931, 0.034482758620689655, 0.034482758620689655, 0.034482758620689655, 0.034482758620689655, 0.034482758620689655]


---
**generate_3_square**
 
Passed: False
Input: ()
Solution: [[[1, 6, 5], [8, 4, 0], [3, 2, 7]], [[1, 8, 3], [6, 4, 2], [5, 0, 7]], [[3, 2, 7], [8, 4, 0], [1, 6, 5]], [[3, 8, 1], [2, 4, 6], [7, 0, 5]], [[5, 0, 7], [6, 4, 2], [1, 8, 3]], [[5, 6, 1], [0, 4, 8], [7, 2, 3]], [[7, 0, 5], [2, 4, 6], [3, 8, 1]], [[7, 2, 3], [0, 4, 8], [5, 6, 1]]] 
Student Result: [[(2, 7, 6), (9, 5, 1), (4, 3, 8)], [(2, 9, 4), (7, 5, 3), (6, 1, 8)], [(4, 3, 8), (9, 5, 1), (2, 7, 6)], [(4, 9, 2), (3, 5, 7), (8, 1, 6)], [(6, 1, 8), (7, 5, 3), (2, 9, 4)], [(6, 7, 2), (1, 5, 9), (8, 3, 4)], [(8, 1, 6), (3, 5, 7), (4, 9, 2)], [(8, 3, 4), (1, 5, 9), (6, 7, 2)]]


---
**add_**
 
Passed: True
Input: (['10', 10], ['10', 2], 8)
Solution: ['14', 8] 
Student Result: ['14', 8]


---
**is_magic_square**
 
Passed: True
Input: ([[8, 1, 6], [3, 5, 7], [4, 9, 2]],)
Solution: True 
Student Result: True

 
Passed: True
Input: ([[8, 3, 4], [1, 5, 9], [6, 7, 2]],)
Solution: True 
Student Result: True

 
Passed: True
Input: ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],)
Solution: False 
Student Result: False

 
Passed: True
Input: ([[8, 1, 6], [3, 5, 7], [4, 2, 2]],)
Solution: False 
Student Result: False

 
Passed: True
Input: ([[8, 1, 6], [3, 8, 7], [4, 9, 8]],)
Solution: False 
Student Result: False


---
**encrypt_sentence**
 
Passed: True
Input: ('this is an interesting problem', 5)
Solution: ymnxenxefsensyjwjxynsleuwtgqjr 
Student Result: ymnxenxefsensyjwjxynsleuwtgqjr

 
Passed: True
Input: ('i wonder how the midterm will go', 5)
Solution: neatsijwemtaeymjerniyjwreanqqelt 
Student Result: neatsijwemtaeymjerniyjwreanqqelt

 
Passed: True
Input: ('this is the best class ever', 3)
Solution: wklvclvcwkhcehvwcfodvvchyhu 
Student Result: wklvclvcwkhcehvwcfodvvchyhu

 
Passed: True
Input: ('writing test code is my favorite activity ever', 2)
Solution: ytkvkpibvguvbeqfgbkubo{bhcxqtkvgbcevkxkv{bgxgt 
Student Result: ytkvkpibvguvbeqfgbkubo{bhcxqtkvgbcevkxkv{bgxgt

 
Passed: True
Input: ('hi', 1)
Solution: ij 
Student Result: ij


---
**encrypt**
 
Passed: False
Input: ('h', 17)
Solution: y 
Student Result: h

 
Passed: False
Input: ('o', 20)
Solution: h 
Student Result: o

 
Passed: False
Input: ('e', 14)
Solution: s 
Student Result: e

 
Passed: False
Input: ('q', 26)
Solution: p 
Student Result: q

 
Passed: False
Input: ('m', 22)
Solution: h 
Student Result: m


---
**decrypt**
 
Passed: False
Input: ('z', 25)
Solution: a 
Student Result: z

 
Passed: False
Input: ('b', 7)
Solution: v 
Student Result: b

 
Passed: False
Input: ('g', 6)
Solution: a 
Student Result: g

 
Passed: False
Input: ('d', 14)
Solution: q 
Student Result: d

 
Passed: False
Input: ('q', 8)
Solution: i 
Student Result: q


---
**mul_**
 
Passed: True
Input: (['10', 10], ['10', 2], 8)
Solution: ['24', 8] 
Student Result: ['24', 8]


---
**decrypt_sentence**
 
Passed: True
Input: ('ymnxenxefsensyjwjxynsleuwtgqjr', 5)
Solution: this is an interesting problem 
Student Result: this is an interesting problem

 
Passed: True
Input: ('neatsijwemtaeymjerniyjwreanqqelt', 5)
Solution: i wonder how the midterm will go 
Student Result: i wonder how the midterm will go

 
Passed: True
Input: ('wklvclvcwkhcehvwcfodvvchyhu', 3)
Solution: this is the best class ever 
Student Result: this is the best class ever

 
Passed: True
Input: ('ytkvkpibvguvbeqfgbkubo{bhcxqtkvgbcevkxkv{bgxgt', 2)
Solution: writing test code is my favorite activity ever 
Student Result: writing test code is my favorite activity ever

 
Passed: True
Input: ('ij', 1)
Solution: hi 
Student Result: hi


---
**convert**
 
Passed: False
Input: (['10', 10], 16)
Solution: ['10', 16] 
Student Result: ['01', 16]

 
Passed: True
Input: (['101010', 2], 8)
Solution: ['52', 8] 
Student Result: ['52', 8]

 
Passed: True
Input: (['555', 6], 10)
Solution: ['215', 10] 
Student Result: ['215', 10]

