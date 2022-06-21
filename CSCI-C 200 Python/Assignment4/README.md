
# Assignment4

## Canvas Score: 99/100
The score in Canvas is out of 100 and is the final grade, but for readability, the test case values have been scaled to whole numbers, and this information is presented below. 


Breakdown Score: 91/92 

Username: rclauss

Commit hash used for grading: 2aa909a30c1219808b83964f1dce1599f1f79f74



## Problem Breakdown 

### Problem 1: 10/10
- square: 5/5.0
- block: 5/5.0 


### Problem 2: 10/10
- purchase: 5/5.0
- how_much: 5/5.0 


### Problem 3: 10/10
- find_num_min: 10/10.0 


### Problem 4: 0/0
 


### Problem 5: 10/10
- increase: 10/10.0 


### Problem 6: 10/10
- letter_count: 10/10.0 


### Problem 7: 12/12
- dot_prod: 2/2.0
- scalar_vec: 2/2.0
- euc_len: 2/2.0
- ang_vec: 2/2.0
- unit_vec: 2/2.0
- vec_op: 2/2.0 


### Problem 8: 10/10
- tree_age: 5/5.0
- noninvasive_tree_age: 5/5.0 


### Problem 9: 9/10
- make_unique: 2/2.0
- partition: 1/2.0
- occurs_at_index: 2/2.0
- intersect: 2/2.0
- optimum: 2/2.0 


### Problem 10: 10/10
- sigma: 2/2.0
- sigma_square: 2/2.0
- sigma_product: 2/2.0
- separate: 2/2.0
- make_linear: 2/2.0 
 

## Test Results


---
**euc_len**
 
Passed: True
Input: ([1, 1, 1],)
Solution: 1.7320508075688772 
Student Result: 1.7320508075688772

 
Passed: True
Input: ([5, 3, 6],)
Solution: 8.366600265340756 
Student Result: 8.366600265340756

 
Passed: True
Input: ([90, 20],)
Solution: 92.19544457292888 
Student Result: 92.19544457292888

 
Passed: True
Input: ([4, 3, 2, 17, 8],)
Solution: 19.544820285692065 
Student Result: 19.544820285692065


---
**make_linear**
 
Passed: True
Input: ([[43, 99], [21, 65], [25, 79], [42, 75], [57, 87], [59, 81]],)
Solution: (0.3852249832102082, 65.1415715245131) 
Student Result: (0.3852249832102082, 65.1415715245131)

 
Passed: True
Input: ([[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]],)
Solution: (0.8, 0.4) 
Student Result: (0.8, 0.4)


---
**make_unique**
 
Passed: True
Input: ([1, 0, 1, 0, 'dog', 'cat', 'cat', (1,), (1,), (2,)],)
Solution: [1, 0, 'dog', 'cat', (1,), (2,)] 
Student Result: [1, 0, 'dog', 'cat', (1,), (2,)]

 
Passed: True
Input: ([[], [], '', '', (), ()],)
Solution: [[], '', ()] 
Student Result: [[], '', ()]

 
Passed: True
Input: (['a', 'a', 'a', 'a', 'b', 'c'],)
Solution: ['a', 'b', 'c'] 
Student Result: ['a', 'b', 'c']

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],)
Solution: [1, 2, 3, 4, 5, 6] 
Student Result: [1, 2, 3, 4, 5, 6]


---
**search_me_me_bee**
 
Passed: False
Input: ()
Solution: [[['M', 5], ['B', 1], ['E', 0]]] 
Student Result: [['M', 5], ['E', 0], ['B', 1]]


---
**noninvasive_tree_age**
 
Passed: True
Input: ([12, 10], 'White Oak')
Solution: 123 
Student Result: 123

 
Passed: True
Input: ([5, 5], 'Red Oak')
Solution: 42 
Student Result: 42


---
**sigma**
 
Passed: True
Input: ([0, 1, 2, 2, 3, 1, 2, 3, 1, 1, 0, 1],)
Solution: 17 
Student Result: 17

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 0, 1, 1, 1, 1, 1, 1, 1],)
Solution: 28 
Student Result: 28

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 7, 9],)
Solution: 37 
Student Result: 37

 
Passed: True
Input: ([5, 4, 3, 2, 1],)
Solution: 15 
Student Result: 15


---
**sigma_square**
 
Passed: True
Input: ([0, 1, 2, 2, 3, 1, 2, 3, 1, 1, 0, 1],)
Solution: 35 
Student Result: 35

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 0, 1, 1, 1, 1, 1, 1, 1],)
Solution: 98 
Student Result: 98

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 7, 9],)
Solution: 221 
Student Result: 221

 
Passed: True
Input: ([5, 4, 3, 2, 1],)
Solution: 55 
Student Result: 55


---
**letter_count**
 
Passed: True
Input: ('We the People of the United States in Order to form a more perfect Union establish Justice insure domestic Tranquility',)
Solution: {'w': 1, 'e': 15, 't': 12, 'h': 3, 'p': 3, 'o': 8, 'l': 3, 'f': 3, 'u': 5, 'n': 6, 'i': 9, 'd': 3, 's': 7, 'a': 4, 'r': 7, 'm': 3, 'c': 3, 'b': 1, 'j': 1, 'q': 1, 'y': 1} 
Student Result: {'w': 1, 'e': 15, 't': 12, 'h': 3, 'p': 3, 'o': 8, 'l': 3, 'f': 3, 'u': 5, 'n': 6, 'i': 9, 'd': 3, 's': 7, 'a': 4, 'r': 7, 'm': 3, 'c': 3, 'b': 1, 'j': 1, 'q': 1, 'y': 1}

 
Passed: True
Input: ('the quick brown fox jumped over the lazy dog',)
Solution: {'t': 2, 'h': 2, 'e': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 2, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'g': 1} 
Student Result: {'t': 2, 'h': 2, 'e': 4, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 2, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'g': 1}

 
Passed: True
Input: ('O brave new world that has such people in it',)
Solution: {'o': 3, 'b': 1, 'r': 2, 'a': 3, 'v': 1, 'e': 4, 'n': 2, 'w': 2, 'l': 2, 'd': 1, 't': 3, 'h': 3, 's': 2, 'u': 1, 'c': 1, 'p': 2, 'i': 2} 
Student Result: {'o': 3, 'b': 1, 'r': 2, 'a': 3, 'v': 1, 'e': 4, 'n': 2, 'w': 2, 'l': 2, 'd': 1, 't': 3, 'h': 3, 's': 2, 'u': 1, 'c': 1, 'p': 2, 'i': 2}


---
**occurs_at_index**
 
Passed: True
Input: ([0, 1, 0, 1, 1], 1)
Solution: [1, 3, 4] 
Student Result: [1, 3, 4]

 
Passed: True
Input: ([0, 1, 0, 1, 1], 2)
Solution: [] 
Student Result: []

 
Passed: True
Input: ([0, 1, 0, 1, 1], 0)
Solution: [0, 2] 
Student Result: [0, 2]


---
**increase**
 
Passed: True
Input: ([0, 1, 2, 2, 3, 1, 2, 3, 1, 1, 0, 1],)
Solution: 4 
Student Result: 4

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 0, 1, 1, 1, 1, 1, 1, 1],)
Solution: 7 
Student Result: 7

 
Passed: True
Input: ([1, 2, 3, 4, 5, 6, 7, 9],)
Solution: 7 
Student Result: 7

 
Passed: True
Input: ([5, 4, 3, 2, 1],)
Solution: 0 
Student Result: 0


---
**block**
 
Passed: True
Input: (4,)
Solution: ****
****
****
****
 
Student Result: ****
****
****
****


 
Passed: True
Input: (6,)
Solution: ******
******
******
******
******
******
 
Student Result: ******
******
******
******
******
******


 
Passed: True
Input: (3,)
Solution: ***
***
***
 
Student Result: ***
***
***


 
Passed: True
Input: (5,)
Solution: *****
*****
*****
*****
*****
 
Student Result: *****
*****
*****
*****
*****


 
Passed: True
Input: (8,)
Solution: ********
********
********
********
********
********
********
********
 
Student Result: ********
********
********
********
********
********
********
********



---
**find_num_min**
 
Passed: True
Input: ([1, 6, 3, 0],)
Solution: (0, 1) 
Student Result: (0, 1)

 
Passed: True
Input: ([-10, -1, 0, 6, 2],)
Solution: (-10, 1) 
Student Result: (-10, 1)

 
Passed: True
Input: ([100, 95, 82, 79, 91],)
Solution: (79, 1) 
Student Result: (79, 1)

 
Passed: True
Input: ([104305, 9482, 9304, 347812],)
Solution: (9304, 1) 
Student Result: (9304, 1)

 
Passed: True
Input: ([0, 0, 0, 0, 0],)
Solution: (0, 5) 
Student Result: (0, 5)


---
**ang_vec**
 
Passed: True
Input: ([1, 1, 1], [1, 2, 3])
Solution: 22.21 
Student Result: 22.207654298596477

 
Passed: True
Input: ([5, 3, 6], [1, 1, 1])
Solution: 14.96 
Student Result: 14.963217433307127

 
Passed: True
Input: ([90, 20], [10, 10])
Solution: 32.47 
Student Result: 32.47119229084849

 
Passed: True
Input: ([4, 3, 2, 17, 8], [6, 2, 8, 14, 0])
Solution: 32.97 
Student Result: 32.97263556600837


---
**palindrome**
 
Passed: True
Input: ('Step on no pets.',)
Solution: True 
Student Result: True

 
Passed: True
Input: ('Was it a cat I saw?',)
Solution: True 
Student Result: True

 
Passed: True
Input: ('A',)
Solution: True 
Student Result: True

 
Passed: True
Input: ('Eva, can I see bees in a cave?',)
Solution: True 
Student Result: True

 
Passed: True
Input: ('racecar',)
Solution: True 
Student Result: True

 
Passed: True
Input: ('Oreos yum!',)
Solution: False 
Student Result: False


---
**purchase**
 
Passed: True
Input: ({'act': 10000, 'holdings': {'gold': (0, 0), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}, 'silver', 100)
Solution: True 
Student Result: True

 
Passed: True
Input: ({'act': 10000, 'holdings': {'gold': (0, 0), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}, 'gold', 1)
Solution: True 
Student Result: True

 
Passed: True
Input: ({'act': 10000, 'holdings': {'gold': (0, 0), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}, 'platinum', 2)
Solution: True 
Student Result: True


---
**tree_age**
 
Passed: True
Input: ([12, 10], 0.5, 0.2)
Solution: 120 
Student Result: 120

 
Passed: True
Input: ([19, 3], 0.2, 0.3)
Solution: 121 
Student Result: 121

 
Passed: True
Input: ([55, 9], 0.9, 0.5)
Solution: 211 
Student Result: 211

 
Passed: True
Input: ([5, 5], 0.1, 0.1)
Solution: 102 
Student Result: 102


---
**partition**
 
Passed: False
Input: ([1, 1, 1, 9, 12, 90], 2)
Solution: [[1, 1], [1, 9], [12, 90]] 
Student Result: [[1, 1], [1, 1], []]

 
Passed: False
Input: ([5, 2, 6, 4, 1], 3)
Solution: [[5, 2, 6], [4, 1]] 
Student Result: [[1], [4, 1]]

 
Passed: False
Input: ([90, 20, 10, 15], 1)
Solution: [[90], [20], [10], [15]] 
Student Result: [[], [], [], []]

 
Passed: True
Input: ([4, 3, 2, 17, 8], 0)
Solution: [] 
Student Result: []


---
**sigma_product**
 
Passed: True
Input: ([1, 1, 1], [1, 1, 1])
Solution: 3 
Student Result: 3

 
Passed: True
Input: ([5, 3, 6], [1, 1, 1])
Solution: 14 
Student Result: 14

 
Passed: True
Input: ([90, 20], [10, 10])
Solution: 1100 
Student Result: 1100

 
Passed: True
Input: ([4, 3, 2, 17, 8], [6, 2, 8, 14, 0])
Solution: 284 
Student Result: 284


---
**square**
 
Passed: True
Input: (4,)
Solution: ****
*  *
*  *
****
 
Student Result: ****
*  *
*  *
****


 
Passed: True
Input: (6,)
Solution: ******
*    *
*    *
*    *
*    *
******
 
Student Result: ******
*    *
*    *
*    *
*    *
******


 
Passed: True
Input: (3,)
Solution: ***
* *
***
 
Student Result: ***
* *
***


 
Passed: True
Input: (5,)
Solution: *****
*   *
*   *
*   *
*****
 
Student Result: *****
*   *
*   *
*   *
*****


 
Passed: True
Input: (8,)
Solution: ********
*      *
*      *
*      *
*      *
*      *
*      *
********
 
Student Result: ********
*      *
*      *
*      *
*      *
*      *
*      *
********



---
**optimum**
 
Passed: True
Input: ([1, 1, 1, 9, 12, 90], 1)
Solution: 90 
Student Result: 90

 
Passed: True
Input: ([5, 2, 6, 4, 1], 0)
Solution: 1 
Student Result: 1

 
Passed: True
Input: ([90, 20, 10, 15], 1)
Solution: 90 
Student Result: 90

 
Passed: True
Input: ([4, 3, 2, 17, 8], 0)
Solution: 2 
Student Result: 2


---
**separate**
 
Passed: True
Input: ([],)
Solution: [] 
Student Result: []

 
Passed: True
Input: ([[1], [2], [3], [4], [5]],)
Solution: [[1, 2, 3, 4, 5]] 
Student Result: [[1, 2, 3, 4, 5]]

 
Passed: True
Input: ([[1, 10], [2, 20]],)
Solution: [[1, 2], [10, 20]] 
Student Result: [[1, 2], [10, 20]]

 
Passed: True
Input: ([[1, 10, 100], [2, 20, 200], [3, 30, 300]],)
Solution: [[1, 2, 3], [10, 20, 30], [100, 200, 300]] 
Student Result: [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

 
Passed: True
Input: ([[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]],)
Solution: [[1, 2, 4, 3, 5], [1, 3, 3, 2, 5]] 
Student Result: [[1, 2, 4, 3, 5], [1, 3, 3, 2, 5]]


---
**search_go_to_out**

Passed: False
Input: ()
Reason: unsupported operand type(s) for -: 'list' and 'list'


---
**how_much**
 
Passed: True
Input: ({'act': 10000, 'holdings': {'gold': (0, 0), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}, 'silver')
Solution: 362.0 
Student Result: 362.0

 
Passed: True
Input: ({'act': 10000, 'holdings': {'gold': (0, 0), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}, 'gold')
Solution: 5.0 
Student Result: 5.0

 
Passed: True
Input: ({'act': 10000, 'holdings': {'gold': (0, 0), 'silver': (0, 0), 'platinum': (0, 0), 'paladium': (0, 0)}}, 'platinum')
Solution: 7.0 
Student Result: 7.0


---
**unit_vec**
 
Passed: True
Input: ([1, 1, 1],)
Solution: [0.5773502691896258, 0.5773502691896258, 0.5773502691896258] 
Student Result: [0.5773502691896258, 0.5773502691896258, 0.5773502691896258]

 
Passed: True
Input: ([5, 3, 6],)
Solution: [0.5976143046671968, 0.3585685828003181, 0.7171371656006362] 
Student Result: [0.5976143046671968, 0.3585685828003181, 0.7171371656006362]

 
Passed: True
Input: ([90, 20],)
Solution: [0.9761870601839526, 0.21693045781865616] 
Student Result: [0.9761870601839526, 0.21693045781865616]

 
Passed: True
Input: ([4, 3, 2, 17, 8],)
Solution: [0.20465780403866032, 0.15349335302899525, 0.10232890201933016, 0.8697956671643063, 0.40931560807732065] 
Student Result: [0.20465780403866032, 0.15349335302899525, 0.10232890201933016, 0.8697956671643063, 0.40931560807732065]


---
**vec_op**
 
Passed: True
Input: ([1, 1, 1], [1, 1, 1], '+')
Solution: [2, 2, 2] 
Student Result: [2, 2, 2]

 
Passed: True
Input: ([5, 3, 6], [1, 1, 1], '+')
Solution: [6, 4, 7] 
Student Result: [6, 4, 7]

 
Passed: True
Input: ([90, 20], [10, 10], '-')
Solution: [80, 10] 
Student Result: [80, 10]

 
Passed: True
Input: ([4, 3, 2, 17, 8], [6, 2, 8, 14, 0], '-')
Solution: [-2, 1, -6, 3, 8] 
Student Result: [-2, 1, -6, 3, 8]


---
**scalar_vec**
 
Passed: True
Input: ([1, 1, 1], 8)
Solution: [8, 8, 8] 
Student Result: [8, 8, 8]

 
Passed: True
Input: ([5, 3, 6], 3)
Solution: [15, 9, 18] 
Student Result: [15, 9, 18]

 
Passed: True
Input: ([90, 20], 17)
Solution: [1530, 340] 
Student Result: [1530, 340]

 
Passed: True
Input: ([4, 3, 2, 17, 8], 0)
Solution: [0, 0, 0, 0, 0] 
Student Result: [0, 0, 0, 0, 0]


---
**intersect**
 
Passed: True
Input: ([], [1])
Solution: [] 
Student Result: []

 
Passed: True
Input: ([2], [])
Solution: [] 
Student Result: []

 
Passed: True
Input: ([1, 1], [1, 1, 2])
Solution: [1] 
Student Result: [1]

 
Passed: True
Input: ([2, 1, 2, 3], [3, 1, 3])
Solution: [1, 3] 
Student Result: [1, 3]


---
**reverse**
 
Passed: True
Input: ('abc',)
Solution: cba 
Student Result: cba

 
Passed: True
Input: (120,)
Solution: 21 
Student Result: 21

 
Passed: True
Input: ((1, 2, 3),)
Solution: (3, 2, 1) 
Student Result: (3, 2, 1)

 
Passed: True
Input: ([1, 2, 3],)
Solution: [3, 2, 1] 
Student Result: [3, 2, 1]


---
**dot_prod**
 
Passed: True
Input: ([1, 1, 1], [1, 1, 1])
Solution: 3 
Student Result: 3

 
Passed: True
Input: ([5, 3, 6], [1, 1, 1])
Solution: 14 
Student Result: 14

 
Passed: True
Input: ([90, 20], [10, 10])
Solution: 1100 
Student Result: 1100

 
Passed: True
Input: ([4, 3, 2, 17, 8], [6, 2, 8, 14, 0])
Solution: 284 
Student Result: 284

