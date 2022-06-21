package rclauss.c212.lab5;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class StudentDirectoryJTest{
    @Test
    void testStudentDirectory(){
        Integer[] x = {3,4,8};
        assertArrayEquals(StudentDirectory.search(-1, 11, 80), x);
        Integer[] y = {8};
        assertArrayEquals(StudentDirectory.search(16, 12, 90), y);
        Integer[] z = {1,2,3,4,5,6,7,8};
        assertArrayEquals(StudentDirectory.search(-1, -1, -1), z);
        Integer[] a = {};
        assertArrayEquals(StudentDirectory.search(101, 101, 101), a);
    }
}
