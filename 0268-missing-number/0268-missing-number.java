class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int value = 0;
        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            seen.add(num);
        }
        for(int i=0; i<=n; i++) {
            if (seen.contains(i) == false) {
                value = i;
            }
        }
        return value;
    }
}