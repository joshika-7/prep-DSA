from typing import List


class Solution:

    def partition(self, l:int, r:int, nums: List[int]) -> int:
        pivot=nums[l] #taking the pivot as first/left most element
        i=l
        j=r

        while i<j: #as long as i doesn't cross j

            while i<=r and nums[i]<=pivot:
                i+=1 #keep incrementing till i finds a number greater than pivot.

            while j>=l and nums[j]>pivot:
                j-=1 #keep decrementing until j finds a element smaller than pivot

            if i<j:
                nums[i], nums[j] =  nums[j], nums[i]

        #if i crosses j it means we found the pivot position j so we swap pivot with element in j index

        nums[l], nums[j] = nums[j], nums[l]

        return j #return the pivot sorted position

    def quick_sort(self, l:int, r:int, nums:List[int]) -> List[int]:

        if l<r:
            j = self.partition(l=l, r=r, nums=nums)
            self.quick_sort(l=l, r=j-1, nums=nums)
            self.quick_sort(l=j+1, r=r, nums=nums)

        return nums

    def sort_array(self, nums:List[int]) -> List[int]:

        sorted_arr = self.quick_sort(l=0, r=len(nums)-1, nums=nums)
        return sorted_arr

obj=Solution()
print(obj.sort_array(nums = [10,9,1,1,1,2,3,1]))




