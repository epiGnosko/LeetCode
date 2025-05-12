class Solution {
public:
    int calcindex(int i, int numRows){
        i = i % (2* numRows - 2);
        if (i < numRows) return i;
        return 2 * numRows - i - 2;
    }

    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        vector<string> parts(numRows);
        for (int i = 0; i < s.size(); i++){
            parts[calcindex(i,numRows)] += s[i];
        }
        for (int i = 1; i < numRows; i++){
            parts[0] += parts[i];
        }
        return parts[0];
    }
};
