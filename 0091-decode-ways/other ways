//Approach-1 (Using Recursion + Memoization)
//T.C : O(n) after memoization (without memoization - O(2^n)
//S.C : O(101) ~= O(1)
class Solution {
public:
    int t[101];
    int solve(int i, string &s, int &n) {
        if(t[i] != -1) {
            return t[i];
        }

        if(i == n) {
            return t[i] = 1; //one valid split done
        }

        if(s[i] == '0') {
            return t[i] = 0; //not possible to split
        }

        int result     = solve(i+1, s, n);
        
        if(i+1 < n) {
            if(s[i] == '1' || (s[i] == '2' && s[i+1] <= '6'))
                result += solve(i+2, s, n);
        }

        
        return t[i] = result;

    }

    int numDecodings(string s) {
        int n = s.length();
        memset(t, -1, sizeof(t));
        return solve(0, s, n);
        

    }
};

//Approach-2 (Bottom Up Way-1)
//T.C : O(n)
//S.C : O(n)
class Solution {
public:
    int bottom_up_1(string&s, int n) {
        //simply simulate the memoized version
        vector<int> t(n+1, 0);
        //t[i] = ways to decode string from index i to n
        t[n] = 1;
        
        for(int i = n-1; i>=0; i--) {
            if(s[i] == '0')
                t[i] = 0;
            else {
                t[i] = t[i+1];
                if(i < n-1 && (s[i] == '1' || (s[i] == '2' && s[i+1] < '7')))
                    t[i] += t[i+2];
            }
        }
        return t[0];
    }
    
    int numDecodings(string &s) {
        int n = s.length();
        return bottom_up_1(s, n);
    }
};


//Approach-3 (Using Bottom Up Way-2)
//T.C : O(n)
//S.C : O(n)
class Solution {
public:
    int bottom_up_2(string&s, int n) {
        vector<int> t(n+1, 0);
        //t[i] = ways to decode string of length i
        t[0] = 1;
        t[1] = s[0]=='0'?0:1;
        
        for(int i = 2; i<=n; i++) {            
            if(s[i-1] != '0')
                t[i] += t[i-1];
                
            if(s[i-2] == '1' || (s[i-2] == '2' && s[i-1] < '7'))
                t[i] += t[i-2];
            
        }
        return t[n];
    }
    
    int numDecodings(string &s) {
        int n = s.length();
        return bottom_up_2(s, n);
    }
};
