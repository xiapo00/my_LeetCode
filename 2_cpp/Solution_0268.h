int missingNumber(vector<int>& nums) { // Something wrong here, remain to be fixed
    int l = nums.size();
    if (l==1) return !nums[0];
    vector<int> table;
    table.reserve(l+1);
    for (int i=0; i<l+1; i++) table[i] = i;
    for (int i=0; i<l; i++) table[nums[i]] = 1;
    for (int i=0; i<l+1; i++) if (table[i] != 1) return i;
    return 0;
}

void test_0268() {
    vector<int> nums = {3, 0, 1};
    cout << missingNumber(nums) << endl; // 2
    nums = {0, 1};
    cout << missingNumber(nums) << endl; // 2
    nums = {0};
    cout << missingNumber(nums) << endl; // 1
}