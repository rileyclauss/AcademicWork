package rclauss.c212.lab6;

import java.util.List;
import java.util.ArrayList;


public class StringLinkedList implements StringCollection{

    private String value;
    private StringLinkedList nextElement;


    public static void main(String[] args){
        StringLinkedList s = new StringLinkedList("z");
        s.add("y");
        s.remove("z");
    }

    StringLinkedList(String value){
        this.value = value;
        this.nextElement = null;
    }
    StringLinkedList(String value, StringLinkedList nextElement){
        this.value = value;
        this.nextElement = nextElement;
    }

    public StringLinkedList getNextElement(){
        return nextElement;
    }
    public String getValue(){
        return value;
    }

    public boolean isLastElementInList(){
        if (nextElement == null){
            return true;
        }
        else{
            return false;
        }
    }

    @Override
    public int getSize() {
        if (isLastElementInList()){
            return 1;
        }
        else if (value != null){
            return 1 + nextElement.getSize();
        }
        else{
            return 0 + nextElement.getSize();
        }
        
    }

    @Override
    public void add(String e) {
        if (isLastElementInList()){
            nextElement = new StringLinkedList(e);
        }
        else{
            nextElement.add(e);
        }
        
    }

    @Override
    public boolean contains(String e) {
        if (isLastElementInList()){
            return value.contains(e) ? true:false;
        }
        else{
            if (value.contains(e)){
                return true;
            }
            else{
                return nextElement.contains(e);
            }
        }
    }


    @Override
    public boolean remove(String e) {
        
        if (isLastElementInList()){
            if (value.equals(e)){
                value = null;
                return true;
            }
            else return false;
        }
        else if (nextElement.isLastElementInList()){
            if (nextElement.getValue().equals(e)){
                nextElement = null;
                return true;
            }
            else if (value.equals(e)){
                value = nextElement.getValue();
                nextElement = null;
                return true;
            }
            else return false;
        }
        else{
            if (nextElement.getValue().equals(e)){
                nextElement = nextElement.getNextElement();
                return true;
            }
            else return nextElement.remove(e);
        }

    }

    @Override
    public String getFirst(){
        return value;
    }
    @Override
    public void addAllFromCollectionString(StringCollection collection) {
        if (collection.getSize() == 0){
            throw new IllegalArgumentException();
        }
        else{
            if (isLastElementInList()){
                if (collection.getSize() > 1){
                    nextElement = new StringLinkedList(collection.getFirst());
                    collection.remove(collection.getFirst());
                    nextElement.addAllFromCollectionString(collection);
                }
                else{
                    nextElement = new StringLinkedList(collection.getFirst());
                }
            }
            else{
                nextElement.addAllFromCollectionString(collection);
            }
        }
    }

    @Override
    public List<String> toList() {
        if (isLastElementInList()){
            List<String> n = new ArrayList<String>();
            n.add(value);
            return n;
        }
        else{
            List<String> m = new ArrayList<String>();
            m.add(value);
            m.addAll(nextElement.toList());
            return m;
        }
    }

}