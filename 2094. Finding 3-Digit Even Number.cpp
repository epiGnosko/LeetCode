class Solution {
public:
    bool can_construct(int i, vector<int>& digits) {
        int ones = i % 10;
        int tens = (i / 10) % 10;
        int hundereds = i / 100;
        bool b_ones = false;
        bool b_tens = false;
        bool b_hundereds = false;
        for (auto x : digits) {
            if (x == ones && !b_ones) {
                b_ones = true;
                continue;
            }
            if (x == tens && !b_tens) {
                b_tens = true;
                continue;
            }
            if (x == hundereds && !b_hundereds) {
                b_hundereds = true;
                continue;
            }
        }
        return (b_ones && b_tens && b_hundereds);
    }

    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> ans;
        int i = 100;
        while (i < 999) {
            if (can_construct(i, digits)) {
                ans.push_back(i);
            }
            i += 2;
        }
        return ans;
    }
};
