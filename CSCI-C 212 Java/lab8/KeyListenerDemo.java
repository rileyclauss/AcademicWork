import java.awt.*;
import javax.swing.*;


public class KeyListenerDemo{
    public static void main(String[] args) {
        JFrame frame = new JFrame("KeyListenerDemo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.getContentPane().add(new KeyListenerImplementation());
        frame.pack();
        frame.setVisible(true);

    }
}
