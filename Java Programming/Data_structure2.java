public class Data_structure2 {
    public static void main(String[] args) {
        int[] arr = {2, 2, 2, 5, 6, 7, 2};
        int key = 2;
        System.out.print("The number is " + key + " and it repeats " + linearsearch(arr, key) + " times.");
    }

    public static int linearsearch(int[] arr, int key) {
        int counter = 0;
        for (int i = 0; i < arr.length; i++) {
            if (key == arr[i]) {
                counter++;
            }
        }
        return counter;
    }
}

