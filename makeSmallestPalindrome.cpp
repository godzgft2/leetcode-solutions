//LeetCode: 2697. Lexicographically Smallest Palindrome
//Runtime 31ms, Beats 76.93%
//Memory 18.72MB, Beats 54.72%

//Given a string of lowercase letters, replace characters to make
//lexographically smallest palindrome

string makeSmallestPalindrome(string s) {
    if (s.length() == 1) return s;
    int l = 0, r = s.length()-1;
    while (l < r) {             //left and right pointers
        if (s[l] != s[r]) {     //opposite chars are not same
            if (s[l] < s[r]) {  //left is lexographically smaller
                s[r] = s[l];
            }
            else {              //right is lexographically smaller
                s[l] = s[r];
            }
        }
        l++;
        r--;
    }
    return s;
}
