package leetcode.java;

public class matrix {
    public static boolean searchMatrix(int[][] matrix, int target) {
        int right = -1;
        int left = 0;
        int a[] = new int[matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            if (target < matrix[i][matrix[0].length - 1]) {
                a = matrix[i];
                right = a.length - 1;
                break;
            }
        }
        while (left < right) {
            int mid = (left + right) / 2;
            if (a[mid] == target) {
                return true;
            } else if (a[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] matrix = {
                { 1, 3, 5, 7 },
                { 10, 11, 16, 20 },
                { 23, 30, 34, 60 }
        };
        int target = 7;
        if (searchMatrix(matrix, target)) {
            System.out.println("Đã tìm thấy");
        } else {
            System.out.println("ko tìm thấy");
        }
    }
}
