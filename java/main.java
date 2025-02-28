import java.util.*;

public class main {
    public static int[] canCompleteCircuit(int[] gas, int[] cost) {
        int[] arr = new int[gas.length];
        arr[0] = gas[0];
        for (int i = 1; i < arr.length; i++) {
            arr[i] = arr[i - 1] + gas[i];
        }
        return arr;
    }

    public static int[] costCongdon(int[] gas, int[] cost) {
        for (int i = 1; i < gas.length; i++) {
            cost[i] = cost[i - 1] + cost[i];
        }
        return cost;
    }

    public static void main(String[] args) {
        int[] gas = { 3, 1, 1 };
        int[] cost = { 1, 2, 2 };
        int[] arr = canCompleteCircuit(gas, cost);
        int[] costCd = costCongdon(gas, cost);
        if (arr[arr.length - 1] < costCd[costCd.length - 1]) {
            System.out.println("Sai");
        } else {
            for (int i = 0; i < gas.length; i++) {
                if (arr[i] >= costCd[i] && i == 0) {
                    System.out.println(gas.length - 1);
                    break;
                } else {
                    System.out.println(i - 1);
                }
            }
        }
    }
}
