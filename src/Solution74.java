import java.util.Arrays;
public class Solution74 {
    public boolean searchMatrix(int[][] matrix, int target) {

        int newArray[] = new int [matrix.length];
        for (int i = 0; i < matrix.length; i ++) {
            newArray[i] = matrix[i][0];
        }
        int index = binarySearch1(newArray, 0, matrix.length - 1, target);
        if (index == -1) return false;
        return binarySearch2(matrix[index], target);
    }

    public int binarySearch1(int [] array, int i, int j,  int target) {
        int mid = (i + j) / 2;
        if (i == j) {
            if (array[mid] > target) return -1;
            else return mid;
        }
        if (array[mid] == target) return mid;
        else if (array[mid] < target) {
            if (array[mid + 1] > target) return mid;
            else {
                return binarySearch1(array, mid + 1, j,  target);
            }
        }
        else {
            if (array[mid - 1] < target) return mid - 1;
            else {
                return binarySearch1(array, i, mid - 1, target);
            }
        }
    }

    public boolean binarySearch2(int [] array, int target) {
        int i = 0, j = array.length - 1;
        int mid = (i + j) / 2;
        if (array[mid] == target) return true;
        else if (array[mid] < target) {
            if (mid == j) return false;
            else {
                int newArray[] = Arrays.copyOfRange(array, mid +1, j +1);
                return binarySearch2(newArray, target);
            }
        }
        else {
            if (mid == i) return false;
            else {
                int newArray[] = Arrays.copyOfRange(array, i, mid);
                return binarySearch2(newArray, target);
            }
        }
    }

}
