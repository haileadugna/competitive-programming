class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[][] map = new int[nums.length][2];
        for (int i = 0 ; i < nums.length; i ++){
            map[i][0] = nums[i];
            map[i][1] = i;
            
            // map.put(i, nums[i]);
        }
        
        int[] res = new int[2];
        Arrays.sort(map, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        // for (int[] row : map) {
        //     for (int element : row) {
        //         System.out.print(element + " ");
        //     }
        //     System.out.println();
        // }

        int i = 0;
        int e = nums.length -1;
        while( i < e){
            if (map[i][0] + map[e][0] == target){

                res[0] = map[i][1];
                res[1] = map[e][1];
                return res;
            } else if (map[i][0] + map[e][0] > target){
                e = e- 1;
            } else {
                i++;
            }
        }
        return res;
    }
}