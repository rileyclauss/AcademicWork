package rclauss.c212.lab6;

import java.util.List;

public interface StringCollection{
    int getSize();
    void add(String e);
    boolean contains(String e);
    boolean remove(String e);
    String getFirst();
    void addAllFromCollectionString(StringCollection collection);
    List<String> toList();
}