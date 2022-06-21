package rclauss.c212.lab6;

public abstract class BankAccount{
    protected String accountOwnerName;
    protected double currentAccountBalance;
    
    public BankAccount(String accountOwnerName, double currentAccountBalance){
        this.accountOwnerName = accountOwnerName;
        this.currentAccountBalance = currentAccountBalance;
    }
    double getCurrentAccountBalance(){
        return currentAccountBalance;
    }
    void setCurrentAccountBalance(double cAccountBalance){
        currentAccountBalance = cAccountBalance;
    }
    String getAccountOwnerName(){
        return accountOwnerName;
    }
    double deposit(double amtToDeposit){
        if (amtToDeposit <= 0){
            throw new IllegalArgumentException("Deposit cannot be 0.");
        }
        currentAccountBalance += amtToDeposit;
        return currentAccountBalance;
    }
    abstract double withdraw(double withdrawAmount, int currentMonth);
    abstract void transferMoney(double amountToTransfer, BankAccount accountToTransferTo, int currentMonth);
}