public class Data_structure1 {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int key = 10;

        System.out.println("key is " + file(arr, key));
    }

    public static String file(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (key == arr[i]) {
                return "found";
            }
        }
        return "not found";
    }
}

    

