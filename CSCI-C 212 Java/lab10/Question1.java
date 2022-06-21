class Question1 {

    public static void main(String[] args) {

        int intNotPalindrome = 30482, intPalindrome = 3040403;
        String strNotPalindrome = "palindrome", strPalindrome = "racecar";


        System.out.println("Iterative: ");
        System.out.println(isIntPalindromeIterative(intNotPalindrome) ? "" + intNotPalindrome + " is a palindrome" : "" + intNotPalindrome + " is not a palindrome");
        System.out.println(isIntPalindromeIterative(intPalindrome) ? "" + intPalindrome + " is a palindrome" : "" + intPalindrome + " is not a palindrome");
        System.out.println(isStrPalindromeIterative(strNotPalindrome) ? strNotPalindrome + " is a palindrome" : strNotPalindrome + " is not a palindrome");
        System.out.println(isStrPalindromeIterative(strPalindrome) ? strPalindrome + " is a palindrome" : strPalindrome + " is not a palindrome");

        System.out.println("\nRecursive:");

        System.out.println(isIntPalindromeRecursive(intNotPalindrome) ? "" + intNotPalindrome + " is a palindrome" : "" + intNotPalindrome + " is not a palindrome");
        System.out.println(isIntPalindromeRecursive(intPalindrome) ? "" + intPalindrome + " is a palindrome" : "" + intPalindrome + " is not a palindrome");
        System.out.println(isStrPalindromeRecursive(strNotPalindrome) ? strNotPalindrome + " is a palindrome" : strNotPalindrome + " is not a palindrome");
        System.out.println(isStrPalindromeRecursive(strPalindrome) ? strPalindrome + " is a palindrome" : strPalindrome + " is not a palindrome");



    }

    static Boolean isIntPalindromeIterative(int num) {
        int rem, inpNum, revNum;
        revNum = 0;
        inpNum = num;
        while (num > 0) {
            rem = num % 10;
            revNum = revNum * 10 + rem;
            num /= 10;
        }

        return (revNum == inpNum);
    }

    static Boolean isStrPalindromeIterative(String str) {

        String revStr = "", inpStr = str;
        while (str.length() > 0) {
            revStr += str.charAt(str.length() - 1);
            str = str.substring(0, str.length() - 1);
        }
        return (revStr.equals(inpStr));

    }

    static Boolean isIntPalindromeRecursive(int num) {

        int revNum = rev(num, 0);
        return (revNum == num);

    }

    static int rev(int num, int rem) {
        if (num == 0)
            return rem;
        rem = (rem * 10) + (num % 10);
        num /= 10;

        return rev(num, rem);
    }

    static Boolean isStrPalindromeRecursive(String str){
        if (str.length() <= 1) return true;
        if(str.charAt(0) == str.charAt(str.length()-1))
            return isStrPalindromeRecursive(str.substring(1, str.length()-1));
        return false;
    }

    
}