
prices = [7,1,5,3,6,4]

buy = prices[0]
maxdiff = -10000
for i in range(1,len(prices)):
    if buy > prices[i]:
        buy = prices[i]
    maxdiff = max(maxdiff , (prices[i] - buy))
            
maxdiff