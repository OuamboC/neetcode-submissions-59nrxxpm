class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Declare result as result = list()
        result = list()
        # Step 2: Sorted nums
        sorted_nums = sorted(nums)
        # Step 3: Outer loop with duplicate skip
        for i in range(len(sorted_nums)): #  Loop through sorted_nums
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue # Skip 
            # Set left and right
            left = i + 1
            right = len(sorted_nums) -1
            #While loop with the three cases
            while(left < right):
                if sorted_nums[i] + sorted_nums[left] + sorted_nums[right] == 0: 
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    # Move left up
                    left = left + 1
                    # Move right down
                    right = right -1
                    while (left < right and sorted_nums[left] == sorted_nums[left -1]):
                        left = left + 1
                    while (left < right and sorted_nums[right] == sorted_nums[right + 1]):
                        right = right - 1
                elif(sorted_nums[i] + sorted_nums[left] + sorted_nums[right] > 0): #Decrease right to 1
                    right = right - 1
                else :  #sorted_nums[i] + sorted_nums[left] + sorted_nums[right] < 0: () increase left to 1)
                    left = left + 1
        return result
       
                 

        

        


        