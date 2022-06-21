package rclauss.c212.lab6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


class Problem1Test {
    
    @Test
    void testApp() {
        BasketballAthlete b = new BasketballAthlete("Lebron", "James", "12/30/1984", "2", "Los Angeles Lakers", "Basketball", "Stadium", 5, 10);
        assertEquals(5*10, b.getTotalTimePlayed());
        HockeyAthlete h = new HockeyAthlete("Wayne", "Gretzky", "01/26/1961", "99", "Edmonton Oilers", "Hockey", "Rink", 9, 90);
        assertEquals(9*90, h.getTotalTimePlayed());
        SoccerAthlete s = new SoccerAthlete("Lionel", "Messi", "01/01/1970", "35", "Paris Saint-Germain", "Soccer", "Field", 30, 14);
        assertEquals(30*14, s.getTotalTimePlayed());
    }
}
