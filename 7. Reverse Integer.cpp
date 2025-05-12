class Solution {
public:
    int reverse(int x) {
        int p = 0;
        while(x){
           if(p>INT_MAX/10 || p<INT_MIN/10) return 0;
           p = p*10+x%10;
           x/=10;
        }
        return p;
    }
};
