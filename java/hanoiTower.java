public class HanoiTower {
    public static void Recursion(int n, char start, char end, char between) {
        if (n == 0) {
            return;
        }
        Recursion(n - 1, start, end, between);
        System.out.println("Move disk" + n + " From rod" + start + " To rod " + end);
        Recursion(n - 1, between, end, start);
    }

    public static void main(String[] args) {
        int N = 3;
        Recursion(N, 'A', 'B', 'C');
    }
}
