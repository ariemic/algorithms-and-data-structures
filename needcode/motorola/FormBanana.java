package motorola;


public class FormBanana {
    public int solution(String S) {
        int countB = 0, countA = 0, countN = 0;

        // Count occurrences of B, A, N
        for (char ch : S.toCharArray()) {
            if (ch == 'B') countB++;
            else if (ch == 'A') countA++;
            else if (ch == 'N') countN++;
        }

        // Calculate the maximum number of times "BANANA" can be formed
        int maxB = countB / 1;
        int maxA = countA / 3;
        int maxN = countN / 2;

        return Math.min(maxB, Math.min(maxA, maxN));
    }

    public static void main(String[] args) {
        FormBanana sol = new FormBanana();
        System.out.println(sol.solution("NAABXAN")); // Output: 1
        System.out.println(sol.solution("NAANAAXNABABYNNBZ")); // Output: 2
        System.out.println(sol.solution("QABAAAWOBL")); // Output: 0
    }

}
