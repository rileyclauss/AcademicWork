/*Create a class called MouseListenerDemo that will hold your main method. This
method will be used to run your program. The main method should do the following:
○ Create a JPanel and add the panel to the JFrame.
○ Register your MouseListenerImplementation to the JPanel.
○ Display the frame to the user. Make sure the details provided below actually
occur when the user interacts with the JPanel.*/

import java.awt.*;

import javax.swing.*;



public class MouseListenerDemo{


    public static void main(String[] args) {
        JFrame frame = new JFrame("MouseListenerDemo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.getContentPane().add(new MouseListenerImplementation());
        frame.pack();
        frame.setVisible(true);

    }

    

}
