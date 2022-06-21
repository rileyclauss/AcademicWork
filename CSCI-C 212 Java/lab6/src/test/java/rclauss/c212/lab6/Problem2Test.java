package rclauss.c212.lab6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Problem2Test {
    
    @Test
    void test2() {
        SavingsAccount s = new SavingsAccount("Riley Clauss", 1600.00, 10);
        assertThrows(IllegalArgumentException.class, () -> {s.deposit(0);});
        assertEquals("Riley Clauss", s.getAccountOwnerName());
        assertEquals(1600.0, s.getCurrentAccountBalance());
        s.withdraw(1500.0, 10);
        assertEquals(100.0, s.getCurrentAccountBalance());
        assertEquals(1, s.getTotalWithdrawalsThisMonth());
        s.deposit(1200.0);
        assertEquals(1300.0, s.getCurrentAccountBalance());
        for (int i = 0; i < 5; i++) 
            s.withdraw(1, 10);
        assertEquals(6, s.getTotalWithdrawalsThisMonth());
        assertThrows(IllegalArgumentException.class, ()->{s.withdraw(1, 10);});
        assertEquals(1295.0, s.getCurrentAccountBalance());
        CheckingAccount c = new CheckingAccount("Riley Clauss", 400);
        assertThrows(IllegalArgumentException.class, ()->{s.transferMoney(1000, c, 10);});
        s.setTotalWithdrawalsThisMonth(0);
        s.transferMoney(1000, c, 10);
        assertEquals(1400.0, c.getCurrentAccountBalance());
        c.transferMoney(1400, s, 10);
        assertEquals(1653, s.getCurrentAccountBalance());
        
    }
}
