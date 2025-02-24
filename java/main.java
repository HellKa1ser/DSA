import java.util.*;

public class main {
    private static final int GRID_SIZE = 0;

    public static void main(String[] args) {

    }

    public static boolean checkValidNumInRow(int[][] board, int row, int num) {
        for (int i = 0; i < GRID_SIZE; i++) {
            if (board[row][i] == num) {
                return true;
            }
        }
        return false;
    }

    public static boolean checkValidNumInCol(int[][] board, int col, int num) {
        for (int i = 0; i < GRID_SIZE; i++) {
            if (board[i][col] == num) {
                return true;
            }
        }
        return false;
    }

    public static boolean checkValidNumInBox(int[][] board, int row, int num, int col) {
        int currentRow = row - row % 3;
        int currentCol = col - col % 3;
        for (int i = currentRow; i < currentRow + 3; i++) {
            for (int j = currentCol; j < currentRow; j++) {
                if (board[i][j] == num) {
                    return true;
                }
            }
        }
        return false;
    }

    public static boolean checkValidPlacement(int[][] board, int row, int col, int num) {
        return !checkValidNumInRow(board, row, num) && !checkValidNumInCol(board, col, num)
                && !checkValidNumInBox(board, row, num, col);
    }

    public static boolean backtracking(int[][] board) {
        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                if (board[col][row] == 0) {
                    for (int num = 1; num < 10; num++) {
                        if (checkValidPlacement(board, row, col, num)) {
                            board[row][col] = num;
                            if (backtracking(board)) {
                                return true;
                            }
                        }
                    }
                }
                return false;
            }
        }
        return true;
    }
}
