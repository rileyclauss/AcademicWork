package rclauss.c212.lab5;

public final class MyArrayList{

    private int size;
    private int length = 16;
    private int[] data;

    public MyArrayList(){
        data = new int[length];
        size = 0;
    }

    public void add(int n){
        if (size == length){
            increaseArray();
        }
        data[size] = n;
        size++;
    }
    private void increaseArray(){
        int[] tmp = new int[length + 1];
        for (int i = 0;i<length;i++){
            tmp[i] = data[i];
        }
        data = tmp;
        length++;
    }
    public void remove(int index){
        if (index < size){
            int[] temp = new int[size-1];
            int j = 0;
            for (int i = 0;i<size;i++){
                if (i!= index){
                    temp[j++] = data[i];
                }
            }
            size--;
            length--;
            data = new int[size];
            data = temp;
        }
    }
    public String toString(){
        String retStr = "{ ";
        for (int i = 0; i<size;i++){
            if (i == size-1){
                retStr += data[i] + " }";
            }
            else{
                retStr += data[i] + ", ";
            }
        }
        return retStr;
    }
    public int getSize(){
        return size;
    }
    public boolean isEmpty(){
        if (size == 0){
            return true;
        }
        else{
            return false;
        }
    }
    public boolean contains(int n){
        boolean ret = false;
        for (int i = 0;i<size;i++){
            if (data[i] == n){
                ret = true;
            } 
        }
        return ret;
    }
    public int indexOf(int n){
        int ret = -1;
        for (int i = 0;i<size;i++){
            if (data[i] == n){
                ret = i;
            } 
        }
        return ret;
    }
}