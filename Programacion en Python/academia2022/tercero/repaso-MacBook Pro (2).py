def numoscilante(num):
    nums = str(num)
    if len(nums)>2:
        for i in range(len(nums)-2):
            if (nums[i]>nums[i+1] and nums[i+1]<nums[i+2]) or (nums[i]<nums[i+1] and nums[i+1]>nums[i+2]):
                pass
            else:
                return "No es ocilante"
        return "Es oscilante"
    elif len(nums)==2:
        if nums[0]!=nums[1]:
            return "Es oscilante"
        else:
            return "No es ocilante"
    else:
        return "No se puede calcular"


print(numoscilante(1))