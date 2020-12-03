#include <string>
using namespace std;

bool isIn(char c, string s) {
    for(int i=0; i<s.size(); i++) {
        if(s[i] == c) return 1;
    }
    return 0;
}

bool hasRepeat(string s) {
    string Collection="";
    for(int i=0; i<s.size(); i++) {
        if(isIn(s[i], Collection)) return 1;
        else Collection += s[i];
    }
    return 0;
}

int lengthOfLongestSubstring(string s) { // unfinished yet
    int i=0, len=s.size(), j=1;
    int maybe=1;
    if(len < 2) return len;
    while(i+j<=len) {
        while(!hasRepeat(s.substr(i, j))) {
            j++;
        }
        if (j > maybe) maybe = j;
        i += j;
        j = 1;
    }
    return maybe;
}

void test_0003() {
    string s = "abcabcbb";
    cout << lengthOfLongestSubstring(s) << endl; // 3
}