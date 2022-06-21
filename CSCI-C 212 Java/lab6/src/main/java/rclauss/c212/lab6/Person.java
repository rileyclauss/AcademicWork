package rclauss.c212.lab6;


public abstract class Person {
    protected String firstName;
    protected String lastName;
    protected String birthDate;
    public Person(String firstName, String lastName, String birthDate){
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
    }
    public Person(){
        this("First", "Last", "01/01/1970");
    }
    public String getFirstName(){
        return firstName;
    }
    public void setFirstName(String fName){
        firstName = fName;
    }
    public String getLastName(){
        return lastName;
    }
    public void setLastName(String lName){
        lastName = lName;
    }
    public String getBirthDate(){
        return birthDate;
    }
    public void setBirthDate(String bDate){
        birthDate = bDate;
    }

}
