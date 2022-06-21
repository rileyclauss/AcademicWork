package com.example.week2;

import java.awt.Rectangle;
/**
 * Hello world!
 */
public final class App {
    private App() {
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        Rectangle box = new Rectangle(5, 10, 20, 30);
        System.out.println("Box 1" + box.toString());
        Rectangle box2 = box;
        System.out.println("Box 2" + box2.toString());
    }
}
