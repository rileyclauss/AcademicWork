package rclauss.c212.lab11;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

class MathSetTest{



    @Test
    void testSet(){
        MathSet set1 = new MathSet();
        set1.addAll(Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15));
        MathSet set2 = new MathSet();
        set2.addAll(Arrays.asList(1,3,5,7,9,11,13,15,17,19));
        // Intersection should yield all odd numbers from 1 to 15 --
        MathSet result = new MathSet();
        result = set1.intersection(set2);
        assertEquals(Arrays.asList(1,3,5,7,9,11,13,15), result.getSet());
        //Union should yield all numbers 1 through 15, as well as 17 and 19
        result = set1.union(set2);
        assertEquals(Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19), result.getSet());
        //Complement should yield all even numbers from 1 through 15, but not 17 and 19
        result = set1.complement(set2);
    }
    

}