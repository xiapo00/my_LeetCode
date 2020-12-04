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

int lengthOfLongestSubstring(string s) {
    int i=0, len=s.size(), j=1;
    if(len < 2) return len;
    while(i+j<len) {
        if(!hasRepeat(s.substr(i, j+1))) j++;
        else i++;
    }
    return j;
}

void test_0003() {
    string s = "abcabcbb";
    cout << lengthOfLongestSubstring(s) << endl; // 3
}