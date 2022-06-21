import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.*;

public class MouseListenerImplementation extends JPanel {

    public int count;
    public MouseListenerImplementation() {
        this.count = 0;
        addMouseListener(new MyMouseListener());
        setBackground(Color.magenta);
        setPreferredSize(new Dimension(400, 400));
    }

    private class MyMouseListener implements MouseListener {
        public void mousePressed(MouseEvent e) {
            System.out.println("Mouse pressed " + (++count) + " times.");
        }
        public void mouseClicked(MouseEvent e) {
            System.out.println("The truth is out there.");
        }
        public void mouseReleased(MouseEvent e) {
            System.out.println("("+e.getX()+", "+e.getY()+") - Mouse was released.");
        }
        public void mouseEntered(MouseEvent e) {}
        public void mouseExited(MouseEvent e) {}

        /*Everytime the user pressesthe mouse, it should increment a counter by 1 and
print that to the console.
○ Everytime the user releasesthe mouse, it should print the (x, y) coordinates to
the console in the form: “(x, y) - Mouse was released”.
○ Everytime the user clicksthe mouse, print out a message of your choice. One
example could be “I love java! I know MouseListeners and Interfaces!” */
    }

}