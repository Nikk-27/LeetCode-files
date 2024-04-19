public class Problem11 {
    public static void main(String[] args) {
        // Define the input array of heights
        int[] heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};

        // Create an instance of Solution
        Solution solution = new Solution();

        // Call the maxArea method with the input array
        int maxArea = solution.maxArea(heights);

        // Print the maximum water container area
        System.out.println("Maximum Water Container Area: " + maxArea);
    }
}


class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxarea = 0;

        while(left < right){
            int currentarea = Math.min(height[left], height[right]) * (right - left);
            maxarea = Math.max(maxarea, currentarea);

            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return maxarea;
    }
}

