package rclauss.c212.lab4;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Unit test for simple App.
 */
class lab4exercisesTest {
    /**
     * Rigorous Test.
     */
    @Test
    void testlab4exercises() {
        assertEquals(lab4exercises.exponentCalculator(1,1), 1);
        assertEquals(lab4exercises.exponentCalculator(4, 0), 1);
        assertEquals(lab4exercises.exponentCalculator(4, 7), 16384);
        assertEquals(lab4exercises.exponentCalculator(4, -1), -1); //-1 is the flag for a negative exponent and will print error

        /** the lab manual says to write a JUnit test for exercise 4, but **
         ** ex4 is a void return method, so there's nothing to test.      **/

    }
}
