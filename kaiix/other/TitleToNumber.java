package random;

/*
 * https://oj.leetcode.com/problems/excel-sheet-column-number/
 */

public class TitleToNumber {
    public static int titleToNumber(String str) {
        str = str.toUpperCase();
        int result = 0;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            result = result * 26 + (ch - 'A' + 1);
        }
        return result;
    }

    public static void main(String []args){
        System.out.println(titleToNumber("A"));
        System.out.println(titleToNumber("Z"));
        System.out.println(titleToNumber("AA"));
        System.out.println(titleToNumber("AB"));
        System.out.println(titleToNumber("AZ"));
    }
}
