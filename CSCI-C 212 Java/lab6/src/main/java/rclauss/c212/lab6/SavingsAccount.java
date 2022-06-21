package rclauss.c212.lab6;

public class SavingsAccount extends BankAccount{

    private int withdrawalsThisMonth;
    private int currentMonth;

    public SavingsAccount(String accountOwnerName, double currentAccountBalance, int currentMonth) {
        super(accountOwnerName, currentAccountBalance);
        this.withdrawalsThisMonth = 0;
        this.setCurrentMonth(currentMonth);

    }
    public int getCurrentMonth() {
        return currentMonth;
    }
    public void setCurrentMonth(int currentMonth) {
        this.currentMonth = currentMonth;
    }
    public int getTotalWithdrawalsThisMonth(){
        return withdrawalsThisMonth;
    }
    public void setTotalWithdrawalsThisMonth(int totalWithdrawals){
        this.withdrawalsThisMonth = totalWithdrawals;
    }
    @Override
    double withdraw(double withdrawAmount, int currentMonth) {
        if (withdrawAmount <= 0)
            throw new IllegalArgumentException("Withdrawal amount cannot be 0.");
        else if (withdrawalsThisMonth >= 6)
            throw new IllegalArgumentException("Too many transfers this month.");
        else if (withdrawAmount > currentAccountBalance && currentAccountBalance > 0){
            double temp = currentAccountBalance;
            currentAccountBalance = 0;
            withdrawalsThisMonth++;
            return temp;
        }
        else{
            currentAccountBalance -= withdrawAmount;
            withdrawalsThisMonth++;
            return withdrawAmount;
        }
        
    }

    @Override
    void transferMoney(double amountToTransfer, BankAccount accountToTransferTo, int currentMonth) {
        if (amountToTransfer <= 0)
            throw new IllegalArgumentException("Withdrawal amount cannot be 0.");
        else if (withdrawalsThisMonth >= 6)
            throw new IllegalArgumentException("Too many transfers this month.");
        else if (amountToTransfer > currentAccountBalance){
            double temp = currentAccountBalance;
            currentAccountBalance = 0;
            withdrawalsThisMonth++;
            accountToTransferTo.deposit(temp);
        }
        else{
            withdrawalsThisMonth++;
            currentAccountBalance -= amountToTransfer;
            accountToTransferTo.deposit(amountToTransfer);
        }
    }

}