def removeElement(self, nums, val):
    j=0
    for i in range(0, len(nums),1):
        if nums[i]!=val:
            nums [i], nums [j]-nums [j],nums[i]
            j=j+1
    return j