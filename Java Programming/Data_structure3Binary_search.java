public class Data_structure3Binary_search {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int search_key = 1;
        System.out.println(binarySearch(array, search_key));
    }

    public static int binarySearch(int[] arr, int key) {
        int lower = 0;
        int upper = arr.length - 1;

        while (lower <= upper) {
            int index = (lower + upper) / 2;
            if (key == arr[index]) {
                return index; 
            } else if (key > arr[index]) {
                lower = index + 1; 
            } else {
                upper = index - 1; 
            }
        }

        return -1; 
    }
}




