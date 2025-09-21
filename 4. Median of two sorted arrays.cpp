class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int total = nums1.size() + nums2.size();
        int medianPos1 = (total - 1) / 2;
        int medianPos2 = total / 2;

        int i = 0, j = 0;
        int median1 = 0, median2 = 0;

        for (int curr = 0; curr <= medianPos2; curr++) {
            int val;
            if (i < nums1.size() && (j >= nums2.size() || nums1[i] < nums2[j])) {
                val = nums1[i++];
            } 
            else {
                val = nums2[j++];
            }
            if (curr == medianPos1) median1 = val;
            if (curr == medianPos2) median2 = val;
        }
        return (total % 2 == 0) ? (median1 + median2) / 2.0 : median2;
    }
};