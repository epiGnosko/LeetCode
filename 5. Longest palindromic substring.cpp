class Solution {
public:
    string longestPalindrome(string s) {
        string processed = "#";
        for (char c : s)
            processed += c, processed += '#';

        int n = processed.size(), center = 0, right = 0, max_len = 0, start = 0;
        vector<int> p(n, 0);

        for (int i = 0; i < n; i++) {
            if (i < right)
                p[i] = min(right - i, p[2 * center - i]); // Mirror from left

            // Expand around i
            int l = i - p[i] - 1, r = i + p[i] + 1;
            while (l >= 0 && r < n && processed[l] == processed[r]) {
                p[i]++;
                l--;
                r++;
            }

            // Update rightmost palindrome
            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }

            // Track longest
            if (p[i] > max_len) {
                max_len = p[i];
                start = (i - max_len) / 2; // Convert to original indices
            }
        }

        return s.substr(start, max_len);
    }
};