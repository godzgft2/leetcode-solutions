# LeetCode: 1475. Final Prices With a Special Discount in a Shop

# Adjusts list of prices to have discount of the next element that 
# is equal to or less than current element

def finalPrices(self, prices: List[int]) -> List[int]:
    ans = [0] * len(prices)
    for i in range(len(prices)):
        curr = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] <= prices[i]:
                curr -= prices[j]
                break
        ans[i] = curr
    
    return ans
