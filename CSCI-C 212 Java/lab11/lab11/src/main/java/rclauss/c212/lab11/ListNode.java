package rclauss.c212.lab11;

import java.util.ArrayList;

public class ListNode {

    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
    void setNext(ListNode next) {
        this.next = next;
    }
    int size(ListNode node) {
        int count = 0;
        ListNode temp = node;
        while (temp != null) {
            temp = temp.next;
            count++;
        }
        return count;
    }

    void printNode(ListNode n) {
        while (n != null) {
            System.out.print(n.val + "->");
            n = n.next;
        }
        System.out.println("null");
    }


    public static void main(String[] args) {

        ListNode one = new ListNode(1);
        ListNode two = new ListNode(2, one);
        ListNode three = new ListNode(3, two);
        ListNode four = new ListNode(4, three);
        ListNode five = new ListNode(5, four);
        five.printNode(five);
        five = reverseList(five, 0, 4);
        five.printNode(five);
        five = reverseList(five, 0,2);
        five.printNode(five);
        ifCycleInNode(five);
        one.setNext(five);
        ifCycleInNode(five);
    }

    //reverse the given node from
    // for example:
    // input 5->4->3->2->1, 0 , 1 , return 4->5->3->2->1
    // input 5->4->3->2->1, 0 , 4 , return 1->2->3->4->5
    // input 5->4->3->2->1, 0 , 5, return null, and print ”either start or end is wrong”.
    // input 5->4->3->2->1, 5 , 0, return null, and print ”end can't be smaller than start”
    // input 5->4->3->2->1, 6 , 0, return null, and print ”either start or end is wrong”.
    // hint: You would need to implement a helper function to reverse the ListNode,
    // then use the helper function in reverseList(ListNode node, int start,int end);
    public static ListNode reverseList(ListNode head, int start, int end) {
        if (end <= start) {
            System.out.println("End cannot be smaller than or equal to start.");
            return null;
        } else if (end > head.size(head) || start > head.size(head)) {
            System.out.println("Either start or end is wrong.");
            return null;
        }
        //list nodes for the total list
        ListNode prev = null;
        ListNode curr = head;

        for (int i = 0; i < start; i++) {
            prev = curr;    //skip ahead to the starting index of the list
            curr = curr.next;//so we only reverse in our given range
        }

        ListNode subHead = curr;    //this is the subLinked List that we want to reverse
        ListNode subTail = null;    //after the reversal, the head will be the tail and the tail will be the head

        for (int i = 1; curr != null && i <= end - start + 1; i++) { //For the range of start to end (+1 to account for indexing)
            ListNode next = curr.next;      //the next node is stored
            curr.next = subTail;        //we set the next node on the end,
            subTail = curr;             //and add the current to the end(effectively the next)
            curr = next;                //then iterate to the next in 'correct' order
        }

        if (subHead != null) {      //it should never be empty, but if it is then skip
            subHead.next = curr;    //the last node should be set to the rest of the linked list
            if (prev == null) {     //if we started reversing the list at the beginning,
                head = subTail; //  set the head to the subTail, which, now reversed, is the first element in the sublist
            } else {
                prev.next = subTail;    //otherwise rejoin the sublist to the rest of the list
            }
        }

        return head;                    //and return the head of the whole list
    }

    
    //check if there is a cycle in the list, which means there is an infinite loop inside
    //the argument.
    //example:
    //input: 1->2->3->4->3->4->3->4->... , return true
    //input: 1->2->3, return false
    public static Boolean ifCycleInNode(ListNode node) {
        ArrayList<Integer> hashes = new ArrayList<Integer>(); //This collects the hash of each ListNode object
        int x = 0;      
        while (node != null){
            x = System.identityHashCode(node);      //collect the identityHashCode
            if (hashes.contains(x)){                //if it's already in the list, then it's already been visited
                System.out.println("Recursive link to node of value " + node.val);  //which means there's a loop
                return true;                                                        //return true
            }
            hashes.add(x);      //otherwise, add it to the list
            node = node.next;   //and continue.
        }   //if there are no loops, then node will eventually point to null and the while loop will terminate
        System.out.println("No recursive links.");
        return false;
    }

}