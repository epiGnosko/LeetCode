class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() < 2) return s.length();
        int len = 0;
        int start = 0;
        int end = 0;
        while(end < s.length()-1){
            for (int i = start; i <= end; i++){
                if (s[end + 1] == s[i]){
                    start++;
                    end--;
                }
            }
            end++;
            if (end - start + 1 > len) len = end - start + 1;
        }
        return len;
    }
};
