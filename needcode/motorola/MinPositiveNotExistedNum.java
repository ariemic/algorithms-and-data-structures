package motorola;

import java.util.Arrays;

public class MinPositiveNotExistedNum {
    public int solution(int[] A) {
        int[] sortedPositive = Arrays.stream(A)
                .distinct()
                .sorted()
                .peek(System.out::println)
                .filter(num -> num > 0)
                .toArray();
        int size = sortedPositive.length;
        if(size == 0 || sortedPositive[0] > 1) return 1;
        for(int i=0; i < size-1; i++){
            if(sortedPositive[i+1] - sortedPositive[i] != 1){
                return sortedPositive[i]+1;
            }
        }
        return sortedPositive[size - 1] + 1;
    }

    public int chatSolution(int[] A) {
        int n = A.length;
        boolean[] present = new boolean[n + 1]; // Track numbers from 1 to n

        // Mark numbers that are present in the array
        for (int num : A) {
            if (num > 0 && num <= n) {
                present[num] = true;
            }
        }

        // Find the first number missing from the array
        for (int i = 1; i <= n; i++) {
            if (!present[i]) {
                return i;
            }
        }

        // If all numbers from 1 to n are present, return n + 1
        return n + 1;
    }

    public static void main(String[] args) {

    }

}
