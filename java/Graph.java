import java.util.*;

public class Graph {
    private static ArrayList<List<Integer>> ke = new ArrayList<>(1000);
    private static boolean[] visited = new boolean[1000];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        for (int i = 0; i <= n; i++) {
            ke.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            ke.get(y).add(x);
            ke.get(x).add(y);

        }
        visited = new boolean[n + 1];
        Arrays.fill(visited, false);

        sc.close();
        // dfs(s);
        dfs(s);
        for (int i = 0; i <= n; i++) {
            if (visited[i] == false) {
                System.out.println("No");
            }
        }

    }

    public static void dfs(int u) {
        System.out.print(u + " ");
        visited[u] = true;
        for (int v : ke.get(u)) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    public static void bfs(int u) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(u);
        visited[u] = true;
        while (!q.isEmpty()) {
            int v = q.poll();
            System.out.print(v + " ");
            for (int x : ke.get(v)) {
                if (!visited[x]) {
                    q.offer(x);
                    visited[x] = true;
                }
            }
        }
    }

}
