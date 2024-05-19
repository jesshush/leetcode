# Val is removed
# Excludes val in count
class Solution(object):
    def removeElement(nums, val):
        nums = [int(x) for x in input("Enter the numbers in the array").split()]
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1
        return count    
solution = Solution()       
val = int(input("Enter the number to be removed ")) 
result = solution.removeElement(val)

# Print the length of the modified array
print("Length of array after removing is: " , result)


