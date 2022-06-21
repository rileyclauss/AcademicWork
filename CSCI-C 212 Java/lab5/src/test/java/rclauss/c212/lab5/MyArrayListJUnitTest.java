package rclauss.c212.lab5;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class MyArrayListJUnitTest{
    @Test
    void testMyArrayList(){
        MyArrayList test = new MyArrayList();
        assertEquals(true, test.isEmpty());
        for (int i = 0;i<10;i++){
            test.add(i);
        }
        assertEquals(false, test.isEmpty());

        assertEquals("{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",test.toString() );
        test.add(10);
        assertEquals("{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }",test.toString() );
        test.remove(0);
        assertEquals("{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }",test.toString() );
        assertEquals(10, test.getSize());
        assertEquals(true, test.contains(5));
        assertEquals(false, test.contains(80));
        assertEquals(3, test.indexOf(4));
        assertEquals(-1, test.indexOf(80));

    }
}