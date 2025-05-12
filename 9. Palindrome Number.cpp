class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return 0;
        int n = x,p=0;
        while(n){
            if( p > INT_MAX/10 || p < INT_MIN/10) return 0;
            p = p*10 + n% 10 ;
            n/=10;
        }
        if (p==x) return 1;
        return 0;
    }
};
