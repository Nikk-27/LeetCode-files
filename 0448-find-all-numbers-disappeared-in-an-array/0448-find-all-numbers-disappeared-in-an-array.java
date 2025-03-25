class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        HashSet<Integer> set = new HashSet<>();
        ArrayList<Integer> al = new ArrayList<>();

        for (int num : nums){
            set.add(num);
        }

        for (int i=1; i<=n; i++) {
            if (!set.contains(i)){
                al.add(i);
            }
        }
        return al;
    }
}

// Tc = O(N)
// SC = O(N)