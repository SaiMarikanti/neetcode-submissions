class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product =  [ 1 for i in range(len(nums))]
        prefix_product[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_product[i]=prefix_product[i-1]*nums[i]

        suffix_product =  [ 1 for i in range(len(nums))]
        suffix_product[len(nums)-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            suffix_product[i] = suffix_product[i+1]*nums[i]
      

        ans = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i>0 and i<len(nums)-1:
                ans[i] = prefix_product[i-1]*suffix_product[i+1]
            elif i == 0:
                ans[i] = suffix_product[i+1]
            else:
                ans[i] = prefix_product[i-1]
        return ans