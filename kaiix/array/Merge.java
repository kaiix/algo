package array;

public class Merge {

    public static void merge(int A[], int m, int B[], int n) {
        int i = 0, j = 0;
        while (i < m && j < n) {
            if (A[i] <= B[j]) {
                i++;
            } else {
                shiftArray(A, i, m-i-1);
                A[i++] = B[j++];
                m++;
            }
        }
        
        while (j < n) {
            A[i++] = B[j++];
        }
    }
    
    private static void shiftArray(int[] A, int start, int count) {
        for (int i = count; i >= 0; i--) {
            A[start+i+1] = A[start+i];
        }
    }
    
    public static void main(String []args){
        int[] A, B;
        
        A = new int[] {1, 2, 3, -1, -1};
        B = new int[] {4, 5};
        merge(A, 3, B, 2);
        printArray(A, 5);

        A = new int[] {1, 3, 5, -1, -1};
        B = new int[] {2, 4};
        merge(A, 3, B, 2);
        printArray(A, 5);

        A = new int[] {1, 3, 8, -1, -1};
        B = new int[] {4, 5};
        merge(A, 3, B, 2);
        printArray(A, 5);
        
        A = new int[] {-1, -1};
        B = new int[] {2, 3};
        merge(A, 0, B, 2);
        printArray(A, 2);

        A = new int[] {1, -1};
        B = new int[] {2};
        merge(A, 1, B, 1);
        printArray(A, 2);
    }

    private static void printArray(int[] A, int len) {
        for (int i = 0; i < len; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }
}
