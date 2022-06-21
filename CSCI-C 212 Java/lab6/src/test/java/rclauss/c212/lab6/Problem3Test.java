package rclauss.c212.lab6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


class Problem3Test {

    @Test
    void test(){
        StringLinkedList s = new StringLinkedList("a");
        s.add("b");
        s.add("c");
        StringSet l = new StringSet();
        l.add("a");
        l.add("b");
        l.add("c");
        assertEquals(l.toList(), s.toList());
        s.remove("b");
        l.remove("b");
        assertEquals(l.toList(), s.toList());
        StringLinkedList a = new StringLinkedList("z");
        a.add("y");
        StringLinkedList b = new StringLinkedList("x");
        b.add("w");
        a.addAllFromCollectionString(b);
        l.remove("a");
        l.remove("c");
        l.add("z");
        l.add("y");
        l.add("x");
        l.add("w");
        assertEquals(l.toList(), a.toList());
        assertEquals(true, a.contains("z"));
        assertEquals(4, a.getSize());
        assertEquals(true, l.contains("z"));
        assertEquals(4, l.getSize());

    }

}