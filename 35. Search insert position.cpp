class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        int mid = (start + end) / 2;

        while (start < end){
            if (nums[mid] == target){
                return mid;
            } else if (nums[mid] > target){
                end = mid;
            } else if (nums[mid] < target){
                start = mid + 1;
            }
            mid = (start + end) / 2;
        }

        if (target > nums[mid]){
            return mid + 1;
        } else {
            return mid;
        }
    }
};