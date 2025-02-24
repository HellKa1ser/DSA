public class Test {
    public static int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int result = 0;
        boolean[] vis = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (vis[i]) {
                continue;
            }
            result++;
            dfs(isConnected, i, n, vis);
        }
        return result;
    }

    public static void dfs(int[][] isConnected, int curr, int n, boolean[] vis) {
        vis[curr] = true;
        for (int i = 0; i < n; i++) {
            if (vis[i] || isConnected[curr][i] == 0) {
                continue;
            }
            dfs(isConnected, curr, i, vis);
        }
    }

    public static void main(String[] args) {
        int[][] n = { { 1, 1, 0 }, { 1, 1, 0 }, { 0, 0, 1 } };
        System.err.println(findCircleNum(n));
    }
}
