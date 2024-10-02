package motorola;

import java.util.*;
import java.util.function.Predicate;

public class Positive0Negative {
    // [+, 0, -, ...
    public int solutionDiff(int[] A) {
        int cnt = 0;

        List<Predicate<Integer>> conditions = new ArrayList<>();
        conditions.add(num -> num > 0);
        conditions.add(num -> num == 0);
        conditions.add(num -> num < 0);

        for(int i = 0; i < A.length; i++){
            System.out.println(A[i]);
            if(!conditions.get(i%3).test(A[i])){
                if(A[i] == 0) return -1;
                cnt++;
            }
        }

        return cnt;

    }

   // [+, 0, -, 0 , +, 0, -, ....
    public int solution(int[] A) {
        int cnt = 0;


        List<Predicate<Integer>> conditions = new ArrayList<>();
        conditions.add(num -> num > 0);
        conditions.add(num -> num < 0);

        for(int i = 0; i < A.length; i++){
            if(i % 2 == 1) {
                if(A[i] != 0){
                    cnt++;
                }

            }
            else{
                if(A[i] == 0) return -1;
                int flag = i/2;
                if(!conditions.get(flag%2).test(A[i])){
                    cnt++;
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) {
        Positive0Negative main = new Positive0Negative();
//        System.out.println(main.solution(new int[]{1, 0, 3, 4, 5, 0, 6})); // Oczekiwane: -1
//        System.out.println(main.solution(new int[]{7, 4, -3, 0, -5, 1, 0})); // Oczekiwane: 0
//        System.out.println(main.solution(new int[]{-5, 0, 3, 0})); // Oczekiwane: -1
//        System.out.println(main.solution(new int[]{1, 2, 3, -1, 0, 5, -2})); // Oczekiwane: 2
    }
}
