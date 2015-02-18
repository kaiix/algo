package string;

/*
 * https://oj.leetcode.com/problems/string-to-integer-atoi/
 */

public class Atoi2 {
    public static int atoi(String str) {
        str = str.trim();
        if (str.length() == 0) {
            return 0;
        }

        boolean isNegative = false;
        if (str.charAt(0) == '-' || str.charAt(0) == '+') {
            isNegative = (str.charAt(0) == '-');
            if (str.length() > 1) {
                str = str.substring(1);
            }
        }

        int result = 0;
        for (int i = 0; i < str.length(); i++) {
            int val = str.charAt(i) - '0';
            if (val > 9 || val < 0) {
                break;
            }
            if (result > 214748364) {
                return isNegative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            } else if (result == 214748364 && val > 7) {
                return isNegative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            } else {
                result = result * 10 + val;
            }
        }
        if (isNegative) {
            result = 0 - result;
            return result;
        } else {
            return result;
        }
    }

    public static void main(String []args){
        System.out.println(atoi("-"));
        System.out.println(atoi("+123"));
        System.out.println(atoi("abcabcbb"));
        System.out.println(atoi("0"));
        System.out.println(atoi("123"));
        System.out.println(atoi("-1"));
        System.out.println(atoi("-123"));
        System.out.println(atoi("123abc"));
        System.out.println(atoi("   123"));
        System.out.println(atoi("+-2"));
        System.out.println(atoi("2147483648"));
        System.out.println(atoi("-2147483648"));
        System.out.println(atoi("-2147483649"));
        System.out.println(atoi("10522545459"));
    }
}

