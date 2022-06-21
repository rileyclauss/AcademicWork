package rclauss.c212.lab6;

import java.util.ArrayList;
import java.util.List;


public class StringSet implements StringCollection{

    private ArrayList<String> elements;

    StringSet(){
        this.elements = new ArrayList<String>();
    }

    @Override
    public int getSize() {
        return elements.size();
    }

    @Override
    public void add(String e) {
        if (elements.contains(e) == false){
            elements.add(e);
        }        
    }

    @Override
    public boolean contains(String e) {
        return elements.contains(e);
    }

    @Override
    public boolean remove(String e) {
        return elements.remove(e);

    }

    @Override
    public String getFirst() {
        return elements.get(0);
    }

    @Override
    public void addAllFromCollectionString(StringCollection collection) {
        elements.addAll(collection.toList());
    }

    @Override
    public List<String> toList() {
        return elements;
    }

}