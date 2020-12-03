#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    int i,j,len;
    len = nums.size();
    for(i=0; i<len; i++)
    {
        for(j=i+1; j<len; j++)
        {
            if(nums[i] + nums[j] == target)
            {
                return {i, j};
            }
        }
    }
    return {i, j};
}

void test_0001() {
    vector<int> nums={2,7,11,15}, result=twoSum(nums, 9);
    cout << "{" << result[0] << ", " << result[1] << "}" << endl; // {0, 1}
}