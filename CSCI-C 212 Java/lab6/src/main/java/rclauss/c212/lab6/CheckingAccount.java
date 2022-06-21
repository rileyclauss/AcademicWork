package rclauss.c212.lab6;

public class CheckingAccount extends BankAccount{

    public CheckingAccount(String accountOwnerName, double currentAccountBalance) {
        super(accountOwnerName, currentAccountBalance);
    }

    @Override
    double withdraw(double withdrawAmount, int currentMonth) {
        if (withdrawAmount <= 0)
            throw new IllegalArgumentException("Withdrawal amount cannot be 0.");
        else if (withdrawAmount > currentAccountBalance && currentAccountBalance > 0){
            currentAccountBalance = 0;
            return currentAccountBalance;
        }
        else{
            currentAccountBalance -= withdrawAmount;
            return withdrawAmount;
        }
    }

    @Override
    void transferMoney(double amountToTransfer, BankAccount accountToTransferTo, int currentMonth) {
        if (amountToTransfer <= 0)
            throw new IllegalArgumentException("Transfer amount cannot be 0.");
        accountToTransferTo.deposit(amountToTransfer*0.97);
    }

}