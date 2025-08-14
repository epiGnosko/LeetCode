class Solution {
public:
    char kthCharacter(int k) {
        int x = 512;
        char ans = 'a';
        while (k > 1){
            if (k > x){
                k -= x;
                ans ++;
            }
            x /= 2;
        }
        return ans;
    }
};