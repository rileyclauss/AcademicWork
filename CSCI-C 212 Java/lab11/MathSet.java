import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.Set;

public class MathSet implements Set<Integer>{


    private ArrayList<Integer> set;

    public ArrayList<Integer> getSet(){
        return this.set;
    }

    public MathSet intersection(MathSet that){
        MathSet retSet = new MathSet();
        for (int i : this.getSet()){
            for (int j : that.getSet()){
                if (i == j){
                    retSet.add(i);
                }
            }
        }
        return this;
    }
    public MathSet union(MathSet that){
        MathSet retSet = new MathSet();
        for (int i : this.getSet()){
            retSet.add(i);
        }
        for (int j : that.getSet()){
            retSet.add(j);
        }
        return this;
    }
    public MathSet complement(MathSet that){
        MathSet x = new MathSet();
        x.addAll(this.getSet());
        x.removeAll(that.getSet());
        return x;
    }

    @Override
    public int size() {
        return set.size();
    }

    @Override
    public boolean isEmpty() {
        return set.isEmpty();
    }

    @Override
    public boolean contains(Object o) {
        return set.contains(o);
    }

    @Override
    public Iterator<Integer> iterator() {
        return set.iterator();
    }

    @Override
    public Object[] toArray() {
        return set.toArray();
    }

    @Override
    public Object[] toArray(Object[] a) {
        return a;
    }

    @Override
    public boolean add(Integer e) {
        if (set.contains(e)){
            return false;
        }
        else return set.add(e);
    }

    @Override
    public boolean remove(Object o) {
        return set.remove(o);
    }

    @Override
    public boolean containsAll(Collection c) {
        for (Object o : c){
            if (!c.contains(o)) return false;
        }
        return true;
    }

    @Override
    public boolean addAll(Collection c) {
        for (Object o : c){
            if (!set.contains(o)) set.add((Integer)o);
        }
        return true;
    }

    @Override
    public boolean retainAll(Collection c) {

        set.retainAll(c);
/*
        MathSet that = new MathSet();
        that.addAll(c);
        that = this.intersection(that);
        this.set = that.getSet(); */
        return true;
        
    }

    @Override
    public boolean removeAll(Collection c) {
        set.removeAll(c);
        return true;
    }

    @Override
    public void clear() {
        set.clear();
    }
    
    
}