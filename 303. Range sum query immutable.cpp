class NumArray {
public:
    vector<int> prefix_sum;

    NumArray(vector<int>& nums) {
        int sum = 0;
        for (auto a : nums){
            sum += a;
            prefix_sum.push_back(sum);
        }
    }
    
    int sumRange(int left, int right) {
        return prefix_sum[right] - ((left)?prefix_sum[left-1]:0);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */