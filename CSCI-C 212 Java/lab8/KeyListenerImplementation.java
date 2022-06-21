import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.*;

import javax.swing.*;

public class KeyListenerImplementation extends JPanel {
    public int count;
    public KeyListenerImplementation() {
        this.count = 0;
        addKeyListener(new MyKeyListener());
        setBackground(Color.magenta);
        setFocusable(true);
        setPreferredSize(new Dimension(400, 400));
        System.out.println("Hello world.");
    }

    private class MyKeyListener implements KeyListener {
        public void keyPressed(KeyEvent e){
            System.out.println("You have pressed the keyboard " + (++count) + " times." );
        }
        public void keyTyped(KeyEvent e){
            if (e.getKeyChar() == 'e'){
                System.exit(0);
            }
            else if(e.getKeyChar() == 'h'){
                System.out.println("Hello World");
            }
            else{
                System.out.println(e.getKeyChar());
            }
        }
        public void keyReleased(KeyEvent e){
            System.out.println("" + e.getKeyChar() + ", " + e.getKeyCode());
        }
    }
}