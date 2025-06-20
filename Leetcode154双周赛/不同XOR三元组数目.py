#由于可以取等号以及异或值可以交换，所以就是任取三个
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        if n==2:
            return 2
        return 1<<n.bit_length()