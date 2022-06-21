import java.awt.*;
import javax.swing.*;

public class FlagDisplay{
    public static void main(String[] args){
        JFrame frame = new JFrame("Flag of Javia");                 //create the frame,
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Flag f = new Flag();                                        //create a new flag from an inner class
        frame.setMinimumSize(new Dimension(314,237));               //set dimensions that allow the content of the frame to be 300x200, accommodating for the top bar and sides
        frame.add(f);               //add the flag to the frame
        frame.pack();
        frame.setVisible(true);     //make the frame visible
    }
    public static class Flag extends JComponent{
        public void paintComponent(Graphics g){
            g.setColor(Color.black);        //paint something similar to the german flag
            g.fillRect(0, 0, 300, 50);      //with an extra band and some extra flair
            g.setColor(Color.red);
            g.fillRect(0,50,300, 50);
            g.setColor(Color.orange);
            g.fillRect(0, 100, 300, 50);
            g.setColor(Color.yellow);
            g.fillRect(0, 150, 300, 50);
            g.fillRect(0, 0, 75, 50);
            g.setColor(Color.orange);
            g.fillRect(75, 50, 75, 50);
            g.setColor(Color.red);      
            g.fillRect(150, 100, 75, 50);
            g.setColor(Color.black);
            g.fillRect(225, 150, 75, 50);
        }
    }
}