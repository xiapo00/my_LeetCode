int abs(int a) {
    if(a > 0) return a;
    return -a;
}

int threeSumClosest(vector<int>& nums, int target) {
    int result = nums[0]+nums[1]+nums[2];
    if(nums.size() == 3) return result;
    for(int i=0; i<nums.size(); i++) {
        for(int j=i+1; j<nums.size(); j++) {
            for(int k=j+1; k<nums.size(); k++) {
                if(abs(nums[i]+nums[j]+nums[k]-target) < abs(result-target)) result = nums[i]+nums[j]+nums[k];
            }
        }
    }
    return result;
}

void test_0016() {
    vector<int> a = {-1, 2, 1, -4};
    cout << threeSumClosest(a, 1) << endl; // 2
}