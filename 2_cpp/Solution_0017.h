vector<string> vectorCombine(vector<string> v, string s) {
    vector<string> result = {};
    for (int i=0; i<v.size(); i++) {
        for (int j=0; j<s.size(); j++) result.push_back(v[i] + s[j]);
    }
    return result;
}

string mapping(char digit) {
    string s;
    switch (digit) {
        case '2': s = "abc"; break;
        case '3': s = "def"; break;
        case '4': s = "ghi"; break;
        case '5': s = "jkl"; break;
        case '6': s = "mno"; break;
        case '7': s = "pqrs"; break;
        case '8': s = "tuv"; break;
        case '9': s = "wxyz"; break;
    }
    return s;
}

vector<string> letterCombinations(string digits) {
    vector<string> result = {};
    if (!digits.size()) return result;
    result = {""};
    for (int i=0; i<digits.size(); i++) result = vectorCombine(result, mapping(digits[i]));
    return result;
}

void test_0017() {
    vector<string> s=letterCombinations("23");
    cout << '{';
    for (int i=0; i<s.size(); i++) cout << '\"' << s[i] << "\", ";
    cout << "\b\b}" << endl;
}